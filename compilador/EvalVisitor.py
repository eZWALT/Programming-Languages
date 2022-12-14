if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


    ArithmeticDicc = {'+': lambda x,y: x+y, '-': lambda a,b: a-b, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '%': lambda x,y: x%y, '^': lambda x,y: x^y}
    LogicDicc = {'<': lambda a,b: a < b, '<=': lambda a,b: a < b, '>': lambda x,y: x > y, '>=': lambda a,b: a >= b, '!=': lambda a,b: a != b, "=": lambda x,y: x == y , "&&": lambda a,b: a and b, '||': lambda a,b: a or b, ':-': lambda a,b: not(a) or b}

class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())        
        print(self.visit(l[0]))

    def visitArithmetic(self, ctx):
        l = list(ctx.getChildren())
        operator = l[1].getText()
        return (ArithmeticDicc[operator] (int(self.visit(l[0].getText()))) (int(self.visit(l[2].getText()))))

    def visitLogic(self,ctx): 
        l = list(ctx.getChildren())
        operator = l[1].getText()
        checknot = l[0].getText()
        if checknot == "!": 
            return not (int(self.visit(l[1].getText())))
        else:            
            return(LogicDicc[operator] (int) (int) )
