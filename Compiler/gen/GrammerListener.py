# Generated from /home/yasaman/Desktop/compiler_project/Compiler/Grammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammerParser import GrammerParser
else:
    from GrammerParser import GrammerParser

# This class defines a complete listener for a parse tree produced by GrammerParser.
class GrammerListener(ParseTreeListener):

    # Enter a parse tree produced by GrammerParser#prog.
    def enterProg(self, ctx:GrammerParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammerParser#prog.
    def exitProg(self, ctx:GrammerParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammerParser#func_list.
    def enterFunc_list(self, ctx:GrammerParser.Func_listContext):
        pass

    # Exit a parse tree produced by GrammerParser#func_list.
    def exitFunc_list(self, ctx:GrammerParser.Func_listContext):
        pass


    # Enter a parse tree produced by GrammerParser#func_def.
    def enterFunc_def(self, ctx:GrammerParser.Func_defContext):
        pass

    # Exit a parse tree produced by GrammerParser#func_def.
    def exitFunc_def(self, ctx:GrammerParser.Func_defContext):
        pass


    # Enter a parse tree produced by GrammerParser#param_list.
    def enterParam_list(self, ctx:GrammerParser.Param_listContext):
        pass

    # Exit a parse tree produced by GrammerParser#param_list.
    def exitParam_list(self, ctx:GrammerParser.Param_listContext):
        pass


    # Enter a parse tree produced by GrammerParser#param.
    def enterParam(self, ctx:GrammerParser.ParamContext):
        pass

    # Exit a parse tree produced by GrammerParser#param.
    def exitParam(self, ctx:GrammerParser.ParamContext):
        pass


    # Enter a parse tree produced by GrammerParser#data_type.
    def enterData_type(self, ctx:GrammerParser.Data_typeContext):
        pass

    # Exit a parse tree produced by GrammerParser#data_type.
    def exitData_type(self, ctx:GrammerParser.Data_typeContext):
        pass


    # Enter a parse tree produced by GrammerParser#code_block.
    def enterCode_block(self, ctx:GrammerParser.Code_blockContext):
        pass

    # Exit a parse tree produced by GrammerParser#code_block.
    def exitCode_block(self, ctx:GrammerParser.Code_blockContext):
        pass


    # Enter a parse tree produced by GrammerParser#stmt_list.
    def enterStmt_list(self, ctx:GrammerParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by GrammerParser#stmt_list.
    def exitStmt_list(self, ctx:GrammerParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by GrammerParser#stmt.
    def enterStmt(self, ctx:GrammerParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammerParser#stmt.
    def exitStmt(self, ctx:GrammerParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammerParser#decide.
    def enterDecide(self, ctx:GrammerParser.DecideContext):
        pass

    # Exit a parse tree produced by GrammerParser#decide.
    def exitDecide(self, ctx:GrammerParser.DecideContext):
        pass


    # Enter a parse tree produced by GrammerParser#loop_stmt.
    def enterLoop_stmt(self, ctx:GrammerParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by GrammerParser#loop_stmt.
    def exitLoop_stmt(self, ctx:GrammerParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by GrammerParser#init_stmt.
    def enterInit_stmt(self, ctx:GrammerParser.Init_stmtContext):
        pass

    # Exit a parse tree produced by GrammerParser#init_stmt.
    def exitInit_stmt(self, ctx:GrammerParser.Init_stmtContext):
        pass


    # Enter a parse tree produced by GrammerParser#post_stmt.
    def enterPost_stmt(self, ctx:GrammerParser.Post_stmtContext):
        pass

    # Exit a parse tree produced by GrammerParser#post_stmt.
    def exitPost_stmt(self, ctx:GrammerParser.Post_stmtContext):
        pass


    # Enter a parse tree produced by GrammerParser#var_list.
    def enterVar_list(self, ctx:GrammerParser.Var_listContext):
        pass

    # Exit a parse tree produced by GrammerParser#var_list.
    def exitVar_list(self, ctx:GrammerParser.Var_listContext):
        pass


    # Enter a parse tree produced by GrammerParser#var.
    def enterVar(self, ctx:GrammerParser.VarContext):
        pass

    # Exit a parse tree produced by GrammerParser#var.
    def exitVar(self, ctx:GrammerParser.VarContext):
        pass


    # Enter a parse tree produced by GrammerParser#expr.
    def enterExpr(self, ctx:GrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammerParser#expr.
    def exitExpr(self, ctx:GrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by GrammerParser#and.
    def enterAnd(self, ctx:GrammerParser.AndContext):
        pass

    # Exit a parse tree produced by GrammerParser#and.
    def exitAnd(self, ctx:GrammerParser.AndContext):
        pass


    # Enter a parse tree produced by GrammerParser#or.
    def enterOr(self, ctx:GrammerParser.OrContext):
        pass

    # Exit a parse tree produced by GrammerParser#or.
    def exitOr(self, ctx:GrammerParser.OrContext):
        pass


    # Enter a parse tree produced by GrammerParser#args.
    def enterArgs(self, ctx:GrammerParser.ArgsContext):
        pass

    # Exit a parse tree produced by GrammerParser#args.
    def exitArgs(self, ctx:GrammerParser.ArgsContext):
        pass


    # Enter a parse tree produced by GrammerParser#unop.
    def enterUnop(self, ctx:GrammerParser.UnopContext):
        pass

    # Exit a parse tree produced by GrammerParser#unop.
    def exitUnop(self, ctx:GrammerParser.UnopContext):
        pass


    # Enter a parse tree produced by GrammerParser#number.
    def enterNumber(self, ctx:GrammerParser.NumberContext):
        pass

    # Exit a parse tree produced by GrammerParser#number.
    def exitNumber(self, ctx:GrammerParser.NumberContext):
        pass



del GrammerParser