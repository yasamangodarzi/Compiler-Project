# Generated from /home/yasaman/Desktop/compiler_project/Compiler/Grammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammerParser import GrammerParser
else:
    from GrammerParser import GrammerParser

# This class defines a complete generic visitor for a parse tree produced by GrammerParser.

class GrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammerParser#prog.
    def visitProg(self, ctx:GrammerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#func_list.
    def visitFunc_list(self, ctx:GrammerParser.Func_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#func_def.
    def visitFunc_def(self, ctx:GrammerParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#param_list.
    def visitParam_list(self, ctx:GrammerParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#param.
    def visitParam(self, ctx:GrammerParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#data_type.
    def visitData_type(self, ctx:GrammerParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#code_block.
    def visitCode_block(self, ctx:GrammerParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#stmt_list.
    def visitStmt_list(self, ctx:GrammerParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#stmt.
    def visitStmt(self, ctx:GrammerParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#decide.
    def visitDecide(self, ctx:GrammerParser.DecideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#loop_stmt.
    def visitLoop_stmt(self, ctx:GrammerParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#init_stmt.
    def visitInit_stmt(self, ctx:GrammerParser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#post_stmt.
    def visitPost_stmt(self, ctx:GrammerParser.Post_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#var_list.
    def visitVar_list(self, ctx:GrammerParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#var.
    def visitVar(self, ctx:GrammerParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#expr.
    def visitExpr(self, ctx:GrammerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#and.
    def visitAnd(self, ctx:GrammerParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#or.
    def visitOr(self, ctx:GrammerParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#args.
    def visitArgs(self, ctx:GrammerParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#unop.
    def visitUnop(self, ctx:GrammerParser.UnopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammerParser#number.
    def visitNumber(self, ctx:GrammerParser.NumberContext):
        return self.visitChildren(ctx)



del GrammerParser