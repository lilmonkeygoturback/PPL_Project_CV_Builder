from CVParser import CVParser
from CVVisitor import CVVisitor as BaseVisitor

class CVToDictVisitor(BaseVisitor):
    def visitCv(self, ctx:CVParser.CvContext):
        return self.visit(ctx.object())

    def visitObject(self, ctx:CVParser.ObjectContext):
        obj = {}
        for pair in ctx.pair():
            key, value = self.visit(pair)
            obj[key] = value
        return obj

    def visitPair(self, ctx:CVParser.PairContext):
        key = self.visit(ctx.STRING())
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
        elif ctx.object_():
            return self.visit(ctx.object_())
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
