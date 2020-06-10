# Generated from D:/Python/compilerZerg/src\pl0.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pl0Parser import pl0Parser
else:
    from pl0Parser import pl0Parser

# This class defines a complete generic visitor for a parse tree produced by pl0Parser.

class pl0Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by pl0Parser#program.
    def visitProgram(self, ctx:pl0Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#block.
    def visitBlock(self, ctx:pl0Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#consts.
    def visitConsts(self, ctx:pl0Parser.ConstsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#var.
    def visitVar(self, ctx:pl0Parser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#procedure.
    def visitProcedure(self, ctx:pl0Parser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#statement.
    def visitStatement(self, ctx:pl0Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#assignstmt.
    def visitAssignstmt(self, ctx:pl0Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#callstmt.
    def visitCallstmt(self, ctx:pl0Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#writestmt.
    def visitWritestmt(self, ctx:pl0Parser.WritestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#qstmt.
    def visitQstmt(self, ctx:pl0Parser.QstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#bangstmt.
    def visitBangstmt(self, ctx:pl0Parser.BangstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#beginstmt.
    def visitBeginstmt(self, ctx:pl0Parser.BeginstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#ifstmt.
    def visitIfstmt(self, ctx:pl0Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#whilestmt.
    def visitWhilestmt(self, ctx:pl0Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#condition.
    def visitCondition(self, ctx:pl0Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#expression.
    def visitExpression(self, ctx:pl0Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#term.
    def visitTerm(self, ctx:pl0Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#factor.
    def visitFactor(self, ctx:pl0Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#ident.
    def visitIdent(self, ctx:pl0Parser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pl0Parser#number.
    def visitNumber(self, ctx:pl0Parser.NumberContext):
        return self.visitChildren(ctx)



del pl0Parser