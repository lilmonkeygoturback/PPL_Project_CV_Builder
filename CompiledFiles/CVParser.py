# Generated from CV.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5#\n\5\f\5\16\5&\13")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\2\2\65\2\f\3\2\2\2\4\17\3\2\2\2\6\32")
        buf.write("\3\2\2\2\b\36\3\2\2\2\n\60\3\2\2\2\f\r\5\4\3\2\r\16\7")
        buf.write("\2\2\3\16\3\3\2\2\2\17\20\7\3\2\2\20\25\5\6\4\2\21\22")
        buf.write("\7\4\2\2\22\24\5\6\4\2\23\21\3\2\2\2\24\27\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2")
        buf.write("\30\31\7\5\2\2\31\5\3\2\2\2\32\33\7\f\2\2\33\34\7\6\2")
        buf.write("\2\34\35\5\n\6\2\35\7\3\2\2\2\36\37\7\7\2\2\37$\5\n\6")
        buf.write("\2 !\7\4\2\2!#\5\n\6\2\" \3\2\2\2#&\3\2\2\2$\"\3\2\2\2")
        buf.write("$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\b\2\2(\t\3\2\2\2")
        buf.write(")\61\7\f\2\2*\61\7\r\2\2+\61\5\4\3\2,\61\5\b\5\2-\61\7")
        buf.write("\t\2\2.\61\7\n\2\2/\61\7\13\2\2\60)\3\2\2\2\60*\3\2\2")
        buf.write("\2\60+\3\2\2\2\60,\3\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60")
        buf.write("/\3\2\2\2\61\13\3\2\2\2\5\25$\60")
        return buf.getvalue()


class CVParser ( Parser ):

    grammarFileName = "CV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_cv = 0
    RULE_obj = 1
    RULE_pair = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames =  [ "cv", "obj", "pair", "array", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj(self):
            return self.getTypedRuleContext(CVParser.ObjContext,0)


        def EOF(self):
            return self.getToken(CVParser.EOF, 0)

        def getRuleIndex(self):
            return CVParser.RULE_cv

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCv" ):
                return visitor.visitCv(self)
            else:
                return visitor.visitChildren(self)




    def cv(self):

        localctx = CVParser.CvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.obj()
            self.state = 11
            self.match(CVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CVParser.PairContext)
            else:
                return self.getTypedRuleContext(CVParser.PairContext,i)


        def getRuleIndex(self):
            return CVParser.RULE_obj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj" ):
                return visitor.visitObj(self)
            else:
                return visitor.visitChildren(self)




    def obj(self):

        localctx = CVParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(CVParser.T__0)
            self.state = 14
            self.pair()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CVParser.T__1:
                self.state = 15
                self.match(CVParser.T__1)
                self.state = 16
                self.pair()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(CVParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CVParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(CVParser.ValueContext,0)


        def getRuleIndex(self):
            return CVParser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = CVParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(CVParser.STRING)
            self.state = 25
            self.match(CVParser.T__3)
            self.state = 26
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CVParser.ValueContext)
            else:
                return self.getTypedRuleContext(CVParser.ValueContext,i)


        def getRuleIndex(self):
            return CVParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CVParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(CVParser.T__4)
            self.state = 29
            self.value()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CVParser.T__1:
                self.state = 30
                self.match(CVParser.T__1)
                self.state = 31
                self.value()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(CVParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CVParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CVParser.NUMBER, 0)

        def obj(self):
            return self.getTypedRuleContext(CVParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(CVParser.ArrayContext,0)


        def getRuleIndex(self):
            return CVParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CVParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CVParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(CVParser.STRING)
                pass
            elif token in [CVParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(CVParser.NUMBER)
                pass
            elif token in [CVParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.obj()
                pass
            elif token in [CVParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.array()
                pass
            elif token in [CVParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(CVParser.T__6)
                pass
            elif token in [CVParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.match(CVParser.T__7)
                pass
            elif token in [CVParser.T__8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.match(CVParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





