from gen.mayoLexer import mayoLexer
from gen.mayoParser import mayoParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from gen.mayoListener import mayoListener

class Semantico(mayoListener):
    def __init__(self):
        self.symbolTable = {}

    def enterVardecl(self, ctx:mayoParser.VardeclContext):
        if ctx.VAR().getText() in self.symbolTable:
            raise Exception('Variable {} declarada previamente'.format(ctx.VAR().getText()))
        self.symbolTable[ctx.VAR().getText()] = ctx.TIPO().getText()

    def exitAssign(self, ctx:mayoParser.AssignContext):
        pass

    def exitSuma(self, ctx:mayoParser.SumaContext):
        pass


def main():
    parser = mayoParser(CommonTokenStream(mayoLexer(FileStream("ejemplo.txt"))))
    tree = parser.lenguaje()

    walker = ParseTreeWalker()
    listener = Semantico()
    walker.walk(listener, tree)

    #print(tree.getChild(0).valor)


if __name__ == '__main__':
    main()
