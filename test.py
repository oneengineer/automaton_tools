
print("------------------------")

from automaton_tools.regex_parser import *

from automaton_tools import DFA as MyDFA


def test1():
    myinput = InputStream("(xy|ab)(ef|efq)*w")
    lexer = RegexLexer(myinput)
    stream = CommonTokenStream(lexer)
    parser = RegexParser(stream)
    parser.addErrorListener(AutomatonErrorListener)
    root = parser.root()

    walker = AutomatonVisotor()
    result = walker.visit(root)

    print(result)
    nfa = NFA(result)
    nfa.drawGraph()
    print(nfa.start.id,nfa.end.id)

    dfa = MyDFA(nfa)
    dfa.drawGraph("dfa")

    d2 = dfa.minimize()
    d2.drawGraph("mindfa")

    x = d2.match("233333")
    print("x: ",x)

def test2():
    """construct DFA manually """
    class A2(MyDFA):
        def __init__(self):
            self.states = frozenset([ 0,1,2,3,4,5 ])
            self.transition = set([
                (0, 3,CharSet('0')),
                (3, 0, CharSet('0')),
                (0, 1, CharSet('1')),
                (3, 4, CharSet('1')),
                (1, 2, CharSet('0')),
                (1, 5, CharSet('1')),
                (4, 2, CharSet('0')),
                (4, 5, CharSet('1')),
                (2, 5, CharSet('1')),
                (5, 5, CharSet('1')),
                (5, 5, CharSet('0')),
                (2, 2, CharSet('0')),
            ])
            self.start = 0
            self.end = set([1,2,4])

            self.transMap = {  (id,e):id2  for (id,id2,e) in self.transition }
    t = A2()
    t.drawGraph("c")
    t2 = t.minimize()
    t2.drawGraph("c1")

def test3():
    myinput = "(ab(qef)*(w|qz))|(xy(efq)*(efw|z))"
    myinput = "a|(z+|b)|(cd)|(g|h)"
    myinput = "a{2,3}[b-c]*"
    #myinput = "(ab(qef)*(w|qz))"
    dfa = MyDFA.fromRegex(myinput)
    dfa.drawGraph("dfa")


def test4():
    """test visitor"""
    myinput = "abc12.+qs{2,}(yui){1,2}?"
    #myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    dfa.drawGraph("dfa")
    print(dfa.match("abc"))
    print(dfa.match("yuiyui"))
    print(dfa.match("abc12xxxxxqssyuiyui"))


def test5():
    """test visitor"""
    myinput = ".+([a-c]+|2|3)*$"
    myinput = "[a-b]"
    #myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    dfa.drawGraph("dfa")
    print(dfa.match("ab"))

    myinput = "[^a-b]+"
    #myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    print(dfa.match("ab"))
    print(dfa.match("xx"))

def test6():
    """test visitor"""
    myinput = ".+([a-c]+|2|3)*$"
    myinput = "[a-b]"
    myinput = "[^bc23]+([b-c]+|2|3){3,}$"
    #myinput = "a(wy){1,}?"
    input = InputStream(myinput)
    lexer = RegexLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RegexParser(stream)
    parser.addErrorListener(AutomatonErrorListener)
    root = parser.root()
    visitor = ASTVisitor()
    ast = visitor.visit(root)
    print(ast)

def test_escape():
    """test escapes"""
    myinput = "\\^(abc)+\\&"
    # myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    print(dfa.match("ab"))
    print(dfa.match("abc"))
    print(dfa.match("^abc&"))

#test6()
#test5()
#test2()
#test3()

test_escape()