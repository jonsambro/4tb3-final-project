from enum import Enum


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


class Scope(Enum):
    GLOBAL = 0
    LOCAL = 1


class DependencySet:

    def __init__(self, identifier):
        self.modified = identifier
        self.dependencies = set()

    def __add__(self, other):
        self.dependencies.add(other)

