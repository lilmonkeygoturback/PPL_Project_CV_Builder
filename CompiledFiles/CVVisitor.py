# Generated from CV.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CVParser import CVParser
else:
    from CVParser import CVParser

# This class defines a complete generic visitor for a parse tree produced by CVParser.

class CVVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CVParser#cv.
    def visitCv(self, ctx:CVParser.CvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CVParser#obj.
    def visitObj(self, ctx:CVParser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CVParser#pair.
    def visitPair(self, ctx:CVParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CVParser#array.
    def visitArray(self, ctx:CVParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CVParser#value.
    def visitValue(self, ctx:CVParser.ValueContext):
        return self.visitChildren(ctx)



del CVParser