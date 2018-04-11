#!/usr/bin/python3
import os.path
import shutil
import sys
from enum import Enum

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import antlr4

from src.Parallelize.ParallelizeLexer import ParallelizeLexer
from src.Parallelize.ParallelizeListener import ParallelizeListener
from src.Parallelize.ParallelizeParser import ParallelizeParser


class Scope(Enum):
    GLOBAL = 0
    LOCAL = 1


class Var:
    def __init__(self, i, s=1):
        self.identifier = i
        self.scope = s

    def __str__(self):
        return "ID: " + self.identifier

    def __eq__(self, other):
        """Overrides the default implementation"""
        try:
            return self.identifier == other.identifer
        except:
            return False

    def __hash__(self):
        return hash(self.identifier)


class Array(Var):
    def __init__(self, i, index, s=1):
        super().__init__(i, s)
        self.index = index

    def __str__(self):
        return "ID: " + self.identifier + ", INDEX: " + self.index

    def __eq__(self, other):
        """Overrides the default implementation"""
        try:
            return self.index == other.index and self.identifier == other.identifer
        except:
            return False

    def __hash__(self):
        return hash(self.identifier) ^ hash(self.index)


class DependencySet:

    def __init__(self, identifier):
        self.modified = identifier
        self.dependencies = set()

    def __add__(self, other):
        self.dependencies.add(other)


class ForLoopListener(ParallelizeListener):
    scopes = [set()]

    loops = []
    current_statements = []

    loop_contexts = []

    loop_dependency_sets = []
    dependency_sets = []

    def enterFor_loop(self, ctx: ParallelizeParser.For_loopContext):
        self.current_statements = []
        self.scopes.append(set())
        self.dependency_sets = list()
        self.loop_contexts.append(ctx)

    def getVar(self, var_token):
        if var_token.simple:
            return Var(var_token.simple.text, 1)
        else:
            return Array(var_token.IDENT().symbol.text, var_token.rhs().getText())

    def enterAssignment(self, ctx: ParallelizeParser.AssignmentContext):
        # print(ctx.modified)
        if ctx.lhs != None:  # if the variable has been declared
            ds = DependencySet(self.getVar(ctx.lhs))
        else:
            ds = DependencySet(self.getVar(ctx.declaration().variable()))

        def is_ident(x):
            try:
                return isinstance(x, ParallelizeParser.VariableContext)
            except:
                return False

        for i in ctx.rhs().getChildren(is_ident):
            # print(ds.modified + " Depends on " + i.getText())
            ds.dependencies.add(self.getVar(i))

        self.dependency_sets.append(ds)

    def enterDeclaration(self, ctx: ParallelizeParser.DeclarationContext):
        self.scopes[-1].add(ctx.variable())

    def exitFor_loop(self, ctx: ParallelizeParser.For_loopContext):
        self.loops.append(self.current_statements)
        self.loop_dependency_sets.append(self.dependency_sets)
        self.scopes.pop()

    def enterStatement(self, ctx: ParallelizeParser.StatementContext):
        self.current_statements.append(ctx.getText())


def main(argv):
    fname = argv[1]
    input = antlr4.FileStream(fname)
    lexer = ParallelizeLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ParallelizeParser(stream)
    tree = parser.program()
    listener = ForLoopListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)
    for i, l in enumerate(listener.loop_dependency_sets):
        print("Loop " + str(i))
        modified = set()
        referenced = set()
        for s in l:
            if s:
                modified.add(s.modified)
                referenced.update(s.dependencies)
        paralellizable = "#pragma omp parallel for reduction (+:r)"
        for m in modified:
            if isinstance(m, Array):
                for r in referenced:
                    if r.identifier == m.identifier and r.index != m.index:
                        print("Not parallelizable")
                        paralellizable = ""
                        break
            else:
                for r in referenced:
                    if m.identifier == r.identifier:
                        print(m.identifier + " needs to be private")
        if paralellizable:
            new_filename = fname.split('.')[0] + "_par." + fname.split('.')[1]
            shutil.copy2(fname, new_filename)
            f = open(new_filename, "r")
            contents = f.readlines()
            f.close()

            contents.insert(listener.loop_contexts[i].start.line - 1, paralellizable + "\n")
            print(new_filename)
            f = open(new_filename, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()


if __name__ == '__main__':
    main(sys.argv)
