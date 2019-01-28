
from automaton_tools.regex_parser import *

from automaton_tools import DFA as MyDFA



def test_escape():
    """test escapes"""
    myinput = "\\^(abc)+\\&"
    # myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    print(dfa.match("ab"))
    print(dfa.match("abc"))
    print(dfa.match("^abc&"))

    print(dfa.match("^abca&"))

def test_escape2():
    """test escapes"""
    myinput = "(ab){2,3}\\{\\}(\\(|\\))+"
    # myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    print(dfa.match("ab{}()"))
    print(dfa.match("abab{}()"))
    print(dfa.match("ababab{}()"))
    print(dfa.match("abababab{}()"))

    print(dfa.match("abab{}()()"))
    print(dfa.match("abab{{}()"))
    print(dfa.match("abab{}(()"))
    print(dfa.match("abab{})"))


def test_repeat():
    """test escapes"""
    myinput = "(ab){3,}"
    # myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    dfa.drawGraph("repeat")
    print(dfa.match("ab"))
    print(dfa.match("abab"))
    print(dfa.match("ababab"))
    print(dfa.match("abababab"))



def test_repeat2():
    """test escapes"""
    myinput = "a{3,4}"
    # myinput = "a(wy){1,}?"
    dfa = MyDFA.fromRegex(myinput)
    nfa = NFA.fromRegex(myinput)
    nfa.drawGraph("nfa")
    dfa.drawGraph("repeat")
    print(dfa.match("a"))
    print(dfa.match("aa"))
    print(dfa.match("aaa"))
    print(dfa.match("aaaa"))
    print(dfa.match("aaaaa"))



test_repeat2()