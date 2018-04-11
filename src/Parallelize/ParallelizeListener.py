# Generated from /home/jon/PycharmProjects/4tb3-loop-parser/src/Parallelize/Parallelize.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParallelizeParser import ParallelizeParser
else:
    from ParallelizeParser import ParallelizeParser

# This class defines a complete listener for a parse tree produced by ParallelizeParser.
class ParallelizeListener(ParseTreeListener):

    # Enter a parse tree produced by ParallelizeParser#program.
    def enterProgram(self, ctx:ParallelizeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#program.
    def exitProgram(self, ctx:ParallelizeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#for_loop.
    def enterFor_loop(self, ctx:ParallelizeParser.For_loopContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#for_loop.
    def exitFor_loop(self, ctx:ParallelizeParser.For_loopContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#for_loop_header.
    def enterFor_loop_header(self, ctx:ParallelizeParser.For_loop_headerContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#for_loop_header.
    def exitFor_loop_header(self, ctx:ParallelizeParser.For_loop_headerContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#statement.
    def enterStatement(self, ctx:ParallelizeParser.StatementContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#statement.
    def exitStatement(self, ctx:ParallelizeParser.StatementContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#declaration.
    def enterDeclaration(self, ctx:ParallelizeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#declaration.
    def exitDeclaration(self, ctx:ParallelizeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#assignment.
    def enterAssignment(self, ctx:ParallelizeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#assignment.
    def exitAssignment(self, ctx:ParallelizeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#self_assignment.
    def enterSelf_assignment(self, ctx:ParallelizeParser.Self_assignmentContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#self_assignment.
    def exitSelf_assignment(self, ctx:ParallelizeParser.Self_assignmentContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#rhs.
    def enterRhs(self, ctx:ParallelizeParser.RhsContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#rhs.
    def exitRhs(self, ctx:ParallelizeParser.RhsContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#literal.
    def enterLiteral(self, ctx:ParallelizeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#literal.
    def exitLiteral(self, ctx:ParallelizeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ParallelizeParser#variable.
    def enterVariable(self, ctx:ParallelizeParser.VariableContext):
        pass

    # Exit a parse tree produced by ParallelizeParser#variable.
    def exitVariable(self, ctx:ParallelizeParser.VariableContext):
        pass


