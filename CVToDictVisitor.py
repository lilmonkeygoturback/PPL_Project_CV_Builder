import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CompiledFiles'))
from CompiledFiles.CVParser import CVParser
from CompiledFiles.CVVisitor import CVVisitor as BaseVisitor

class CVToDictVisitor(BaseVisitor):
    def visitCv(self, ctx:CVParser.CvContext):
        # Use ctx.obj() instead of ctx.object()
        return self.visit(ctx.obj())

    def visitObj(self, ctx:CVParser.ObjContext):
        obj = {}
        for pair in ctx.pair():
            key, value = self.visit(pair)
            obj[key] = value
        return obj

    def visitPair(self, ctx:CVParser.PairContext):
        key = self._strip_quotes(ctx.STRING().getText())
        value = self.visit(ctx.value())
        return key, value

    def visitArray(self, ctx:CVParser.ArrayContext):
        return [self.visit(v) for v in ctx.value()]

    def visitValue(self, ctx:CVParser.ValueContext):
        if ctx.STRING():
            return self._strip_quotes(ctx.STRING().getText())
        elif ctx.NUMBER():
            num = ctx.NUMBER().getText()
            return float(num) if '.' in num or 'e' in num or 'E' in num else int(num)
        elif ctx.obj():
            return self.visit(ctx.obj())
        elif ctx.array():
            return self.visit(ctx.array())
        elif ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        elif ctx.getText() == 'null':
            return None

    def _strip_quotes(self, s):
        return s[1:-1]
