from gen.calcLexer import calcLexer
from gen.calcParser import calcParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from gen.calcListener import calcListener

class Interprete(calcListener):
    def exitNum(self, ctx:calcParser.NumContext):
        ctx.valor = int(ctx.NUMERO().getText())

    def exitSuma(self, ctx:calcParser.SumaContext):
        ctx.valor = ctx.exp(0).valor + ctx.exp(1).valor

    def exitMult(self, ctx:calcParser.MultContext):
        ctx.valor = ctx.exp(0).valor * ctx.exp(1).valor

    def exitParens(self, ctx:calcParser.ParensContext):
        ctx.valor = ctx.exp().valor

def main():
    input = FileStream("ejemplo.txt")
    lexer = calcLexer(input)
    stream = CommonTokenStream(lexer)
    parser = calcParser(stream)
    tree = parser.operacion()

    walker = ParseTreeWalker()
    listener = Interprete()
    walker.walk(listener, tree)

    print(tree.getChild(0).valor)


if __name__ == '__main__':
    main()
