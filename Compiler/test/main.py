import sys
from antlr4 import *

from Compiler.gen.GrammerLexer import GrammerLexer
from Compiler.gen.GrammerListener import GrammerListener
from Compiler.gen.GrammerParser import GrammerParser


def main(argv):
    input_stream = InputStream("""int main () {
    int b=2;
    }""")
    lexer = GrammerLexer(input_stream)
    tokens_stream = CommonTokenStream(lexer)
    parser = GrammerParser(tokens_stream)
    tree = parser.prog()
    printer = GrammerListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.code)


if __name__ == '__main__':
    main(sys.argv)


