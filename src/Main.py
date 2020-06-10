import antlr4
from src.gen.pl0Lexer import *
from src.gen.pl0Parser import *
from antlr4.tree.Trees import Trees
from src.gen.pl0Listener import pl0Listener
from src.gen.pl0Visitor import pl0Visitor
from antlr4.Token import CommonToken
from src.GeneratedIR import TokenIR

def readFile(filename):
   file = open(filename, 'r')
   goCode = file.read()
   return goCode

def main():

   TestCode = readFile("test.txt")    # Read golang

   lexer = pl0Lexer(antlr4.InputStream(TestCode))
   lexer.removeErrorListeners()

   stream = CommonTokenStream(lexer)
   parser = pl0Parser(stream)

   tree = parser.program()
   printer = pl0Listener()
   walker = ParseTreeWalker()
   walker.walk(printer, tree)
   visitor = pl0Visitor()

   tree = Trees.toStringTree(tree, None, parser)

   print("AST: ")
   print(tree)

   ir = TokenIR(tree)
   print(ir)




if __name__ == '__main__':
   main()