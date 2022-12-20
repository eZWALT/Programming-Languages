if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

    FunctionTable = []  #Llista de funcions, que cadascuna està identificada per un nom i els noms de les seves variables internes (tipus de retorn es sempre int)

    SymbolTable = []  #Llista de diccionaris, un diccionari per scope, l'usarem com una pila
    #SymbolTable.append({}) crea un nou scope de variables, si fem un SymbolTable.pop() treu aquest ambit de visibilitat
    ArithmeticDicc = {'+': lambda x,y: x+y, '-': lambda a,b: a-b, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '%': lambda x,y: x%y, '^': lambda x,y: x**y}
    LogicDicc = {'<': lambda a,b: a < b, '<=': lambda a,b: a < b, '>': lambda x,y: x > y, '>=': lambda a,b: a >= b, '!=': lambda a,b: a != b, "=": lambda x,y: x == y , "&&": lambda a,b: a and b, '||': lambda a,b: a or b, ':-': lambda a,b: not(a) or b}

class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())        
        print(self.visit(l[0]))                                                                 #evaluacio del programa


    def visitArithmetic(self, ctx):
        l = list(ctx.getChildren())
        operator = l[1].getText() 
        return (ArithmeticDicc[operator] ((int(self.visit(l[0])) ) ,(int(self.visit(l[2])))))   #nomes hi han operacions aritmetiques binaries

    def visitLogic(self,ctx): 
        l = list(ctx.getChildren())
        operator = l[1].getText()
        checknot = l[0].getText()
        if checknot == "!":                                                                     #cas 1: not llogica
            return not int(self.visit(l[1]))    
        else:            
            return bool(LogicDicc[operator] ((int(self.visit(l[0]))),(int(self.visit(l[2])))) )  #cas 2: diferents operacions binaries com comparacions i portes llogiques

    
    def visitUnary(self,ctx):
        l = list(ctx.getChildren())
        if len(l) != 1:
            return int(self.visit(l[1]))                                                         #cas 1: es tracta d'una expressio parentitzada
        else:
            return int(l[0].getText())                                                           #cas 2: es tracta d'un literal numeric 

    def visitVariable(self,ctx):
        l = list(ctx.getChildren())
        #retorna el valor de la variable 

    def visitBlock(self,ctx):
        l = list(ctx.getChildren())
        for i in l: 
            value = self.visit(i)
            if value != None:   
                return value                                                    #Pel Tractament de funcions, s'han de visitar tots els statements
    
    def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
        l = list(ctx.getChildren())
        function_ID = l[0].getText()        #tots els parametres venen a continuacio
        block 
        parameters = []
        for i in l[1:]:
            if i == l[-1]: 
                block = i
            else:
                parameters.append(i)

        FunctionTable.append((function_ID, parameters,block))
        return None
        
    #esta a mitges!!!! cal que la taula de funcions estigui operativa
    def visitCall(self,ctx):
        l = list(ctx.getChildren())
        ID = l[0].getText()
        if not ID in SymbolTable: 
            Exception 
        else:
            for i in l[1:]:                             #tots els fills, a excepcio del primer són els multiples parametres
                x = 2
    def visitConditional(self,ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:                                  #cas 1: if sense else
            condition = int(self.visit(l[1]))
            if condition != 0: 
                SymbolTable.append({})     
                self.visit(l[2])
                SymbolTable.pop()

        elif len(l) == 5:                                #cas 2: if amb else
            condition = int(self.visit(l[1]))
            if condition != 0: 
                SymbolTable.append({})      
                self.visit(l[2])
                SymbolTable.pop()
            else:
                SymbolTable.append({})     
                self.visit(l[4])
                SymbolTable.pop()

        elif len(l) == 10:                               #cas 3: if amb un else if
            condition1 = int(self.visit(l[1]))
            condition2 = int(self.visit(l[4]))
            if condition1 != 0: 
                SymbolTable.append({})      
                self.visit(l[2])
                SymbolTable.pop()
            elif condition2 != 0:
                SymbolTable.append({})      
                self.visit(l[5])
                SymbolTable.pop()

        else:                                            #cas 4: if amb un else if i també else
            condition1 = int(self.visit(l[1]))
            condition2 = int(self.visit(l[4]))
            if condition1 != 0: 
                SymbolTable.append({})      
                self.visit(l[2])
                SymbolTable.pop()
            elif condition2 != 0:
                SymbolTable.append({})      
                self.visit(l[5])
                SymbolTable.pop()
            else:
                SymbolTable.append({})      
                self.visit(l[7])
                SymbolTable.pop()

        return None        

    def visitLoop(self,ctx):
        l = list(ctx.getChildren())
        if l[0].getText() == "while":               #cas 1: while 
            condition = self.visit(l[1])
            while condition != 0:
                SymbolTable.append({})      
                self.visit(l[2])
                SymbolTable.pop()
                condition = self.visit(l[1])

        elif l[0].getText() == "do":                #cas 2: do while
            self.visit(l[2])
            condition = self.visit(l[3])
            while condition != 0:
                SymbolTable.append({})      
                self.visit(l[1])
                SymbolTable.pop()
                condition = self.visit(l[3])



    def visitAssignment(self,ctx):
        l = list(ctx.getChildren())
        ID = l[0].getText()
        value = l[2]
        SymbolTable[-1][ID] = int(self.visit(value)) #Cal crear, al ultim scope disponible, una nova entrada amb nom ID i valor value
        return None