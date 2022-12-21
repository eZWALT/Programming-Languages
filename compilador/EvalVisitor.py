if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

    FunctionTable = {}  #Llista de funcions, que cadascuna està identificada per un nom i els noms de les seves variables internes (tipus de retorn es sempre int)

    SymbolTable = []  #Llista de diccionaris, un diccionari per scope, l'usarem com una pila
    #SymbolTable.append({}) crea un nou scope de variables, si fem un SymbolTable.pop() treu aquest ambit de visibilitat
    ArithmeticDicc = {'+': lambda x,y: x+y, '-': lambda a,b: a-b, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '%': lambda x,y: x%y, '^': lambda x,y: x**y}
    LogicDicc = {'<': lambda a,b: a < b, '<=': lambda a,b: a < b, '>': lambda x,y: x > y, '>=': lambda a,b: a >= b, '!=': lambda a,b: a != b, "=": lambda x,y: x == y , "&&": lambda a,b: a and b, '||': lambda a,b: a or b, ':-': lambda a,b: not(a) or b, '-->': lambda a,b: not(a) or b}

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
            return int(bool(LogicDicc[operator] ((int(self.visit(l[0]))),(int(self.visit(l[2])))) ))  #cas 2: diferents operacions binaries com comparacions i portes llogiques

    #evaluacio de numeros o bé expresions parentitzades
    def visitUnary(self,ctx):
        l = list(ctx.getChildren())
        if len(l) != 1:
            return int(self.visit(l[1]))                                                         #cas 1: es tracta d'una expressio parentitzada
        else:
            return int(l[0].getText())                                                           #cas 2: es tracta d'un literal numeric 

    #evaluacio de true i false
    def visitValues(self, ctx: ExprParser.ValuesContext):
        l = list(ctx.getChildren())
        if l[0].getText() == "true":
            return 1
        else: 
            return 0

    def visitVariable(self,ctx):
        l = list(ctx.getChildren())
        ID = l[0].getText()
        assert (ID in SymbolTable[-1]), "Execution Error: Variable " + ID + " may no exist or may not be used in this scope"
        return int(SymbolTable[-1][ID])

    def visitCall(self,ctx):
        l = list(ctx.getChildren())
        ID = l[0].getText()

        #Creem un nou ambit de visibilitat
        SM = {}
        #A continuacio testejem possibles errores en l'execucio d'una funcio

        assert(ID in FunctionTable), "This function hasn't been declared yet"   
        (block,parameters) = FunctionTable[ID]
        assert (len(l[1:]) == len(parameters)), "Not enough parameters provided in function call: " + ID + " expected: " + len(l[1:]) + " , given: " + len(parameters)

        #Asignem en el ambit local totes les variables amb els noms corresponents als parametres 
        for index in range(0,len(parameters)):                          #tots els fills, a excepcio del primer són els multiplearametres
            SM[parameters[index].getText()] = self.visit(l[index+1])

        #executem la funció 
        SymbolTable.append(SM)
        returnvalue = self.visit(block)
        #Destruim el ambit de visibilitat
        SymbolTable.pop()

        return returnvalue

    def visitBlock(self,ctx):
        l = list(ctx.getChildren())
        for i in l: 
            value = self.visit(i)
            if value != None:   
                return value                                                    #Pel Tractament de funcions, s'han de visitar tots els statements
    
    def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
        l = list(ctx.getChildren())
        function_ID = l[0].getText()        #tots els parametres venen a continuacio
        block = None
        parameters = []
        for i in l[1:]:
            if i == l[-1]: 
                block = i
            else:
                parameters.append(i)

        FunctionTable[function_ID] = (block,parameters) #nova entrada a la taula de funcions
        return None        

    def visitConditional(self,ctx):
        l = list(ctx.getChildren())
        value = None
        if len(l) == 3:                                  #cas 1: if sense else
            condition = int(self.visit(l[1]))
            if condition != 0: 
                value = self.visit(l[2])

        elif len(l) == 5:                                #cas 2: if amb else
            condition = int(self.visit(l[1]))
            if condition != 0: 
               value = self.visit(l[2])
            else: 
               value = self.visit(l[4])

        elif len(l) == 10:                               #cas 3: if amb un else if
            condition1 = int(self.visit(l[1]))
            condition2 = int(self.visit(l[4]))
            if condition1 != 0:       
              value = self.visit(l[2])
            elif condition2 != 0:   
               value = self.visit(l[5])

        else:                                            #cas 4: if amb un else if i també else
            condition1 = int(self.visit(l[1]))
            condition2 = int(self.visit(l[4]))
            if condition1 != 0:     
               value = self.visit(l[2])
            elif condition2 != 0: 
               value = self.visit(l[5])
            else: 
               value = self.visit(l[7])

        return value        

    def visitLoop(self,ctx):
        l = list(ctx.getChildren())
        value = None
        if l[0].getText() == "while":               #cas 1: while 
            condition = self.visit(l[1])
            while condition != 0:  
                value = self.visit(l[2])
                if value != None: break
                condition = self.visit(l[1])

        elif l[0].getText() == "do":                #cas 2: do while
            self.visit(l[2])
            condition = self.visit(l[3])
            while condition != 0:  
                value = self.visit(l[1])
                if value != None: break
                condition = self.visit(l[3])

        return value



    def visitAssignment(self,ctx):
        l = list(ctx.getChildren())
        ID = l[0].getText()
        value = l[2]
        SymbolTable[-1][ID] = int(self.visit(value)) #Cal crear, al ultim scope disponible, una nova entrada amb nom ID i valor value
        return None

    def visitExpression(self,ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]))
