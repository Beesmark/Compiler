# Generated from D:/Python/compilerZerg/src\pl0.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pl0Parser import pl0Parser
else:
    from pl0Parser import pl0Parser

# This class defines a complete listener for a parse tree produced by pl0Parser.
class pl0Listener(ParseTreeListener):

    # Enter a parse tree produced by pl0Parser#program.
    def enterProgram(self, ctx:pl0Parser.ProgramContext):
        pass

    # Exit a parse tree produced by pl0Parser#program.
    def exitProgram(self, ctx:pl0Parser.ProgramContext):
        pass


    # Enter a parse tree produced by pl0Parser#block.
    def enterBlock(self, ctx:pl0Parser.BlockContext):
        pass

    # Exit a parse tree produced by pl0Parser#block.
    def exitBlock(self, ctx:pl0Parser.BlockContext):
        pass


    # Enter a parse tree produced by pl0Parser#consts.
    def enterConsts(self, ctx:pl0Parser.ConstsContext):
        pass

    # Exit a parse tree produced by pl0Parser#consts.
    def exitConsts(self, ctx:pl0Parser.ConstsContext):
        pass


    # Enter a parse tree produced by pl0Parser#var.
    def enterVar(self, ctx:pl0Parser.VarContext):
        pass

    # Exit a parse tree produced by pl0Parser#var.
    def exitVar(self, ctx:pl0Parser.VarContext):
        pass


    # Enter a parse tree produced by pl0Parser#procedure.
    def enterProcedure(self, ctx:pl0Parser.ProcedureContext):
        pass

    # Exit a parse tree produced by pl0Parser#procedure.
    def exitProcedure(self, ctx:pl0Parser.ProcedureContext):
        pass


    # Enter a parse tree produced by pl0Parser#statement.
    def enterStatement(self, ctx:pl0Parser.StatementContext):
        pass

    # Exit a parse tree produced by pl0Parser#statement.
    def exitStatement(self, ctx:pl0Parser.StatementContext):
        pass


    # Enter a parse tree produced by pl0Parser#assignstmt.
    def enterAssignstmt(self, ctx:pl0Parser.AssignstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#assignstmt.
    def exitAssignstmt(self, ctx:pl0Parser.AssignstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#callstmt.
    def enterCallstmt(self, ctx:pl0Parser.CallstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#callstmt.
    def exitCallstmt(self, ctx:pl0Parser.CallstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#writestmt.
    def enterWritestmt(self, ctx:pl0Parser.WritestmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#writestmt.
    def exitWritestmt(self, ctx:pl0Parser.WritestmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#qstmt.
    def enterQstmt(self, ctx:pl0Parser.QstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#qstmt.
    def exitQstmt(self, ctx:pl0Parser.QstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#bangstmt.
    def enterBangstmt(self, ctx:pl0Parser.BangstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#bangstmt.
    def exitBangstmt(self, ctx:pl0Parser.BangstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#beginstmt.
    def enterBeginstmt(self, ctx:pl0Parser.BeginstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#beginstmt.
    def exitBeginstmt(self, ctx:pl0Parser.BeginstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#ifstmt.
    def enterIfstmt(self, ctx:pl0Parser.IfstmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#ifstmt.
    def exitIfstmt(self, ctx:pl0Parser.IfstmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#whilestmt.
    def enterWhilestmt(self, ctx:pl0Parser.WhilestmtContext):
        pass

    # Exit a parse tree produced by pl0Parser#whilestmt.
    def exitWhilestmt(self, ctx:pl0Parser.WhilestmtContext):
        pass


    # Enter a parse tree produced by pl0Parser#condition.
    def enterCondition(self, ctx:pl0Parser.ConditionContext):
        pass

    # Exit a parse tree produced by pl0Parser#condition.
    def exitCondition(self, ctx:pl0Parser.ConditionContext):
        pass


    # Enter a parse tree produced by pl0Parser#expression.
    def enterExpression(self, ctx:pl0Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by pl0Parser#expression.
    def exitExpression(self, ctx:pl0Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by pl0Parser#term.
    def enterTerm(self, ctx:pl0Parser.TermContext):
        pass

    # Exit a parse tree produced by pl0Parser#term.
    def exitTerm(self, ctx:pl0Parser.TermContext):
        pass


    # Enter a parse tree produced by pl0Parser#factor.
    def enterFactor(self, ctx:pl0Parser.FactorContext):
        pass

    # Exit a parse tree produced by pl0Parser#factor.
    def exitFactor(self, ctx:pl0Parser.FactorContext):
        pass


    # Enter a parse tree produced by pl0Parser#ident.
    def enterIdent(self, ctx:pl0Parser.IdentContext):
        pass

    # Exit a parse tree produced by pl0Parser#ident.
    def exitIdent(self, ctx:pl0Parser.IdentContext):
        pass


    # Enter a parse tree produced by pl0Parser#number.
    def enterNumber(self, ctx:pl0Parser.NumberContext):
        pass

    # Exit a parse tree produced by pl0Parser#number.
    def exitNumber(self, ctx:pl0Parser.NumberContext):
        pass



del pl0Parser