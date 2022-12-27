from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
from flask import Flask, request, render_template

app = Flask(__name__)
functions = []
resultats = []

def getFunx(list):
    ID = list[0]
    result = str(ID)

    for i in list[1:]: 
        result = result + " " + str(i)
    return str(result)

@app.route('/', methods=['GET', 'POST'])
def base():
    
    if request.method == 'POST':

        input_text = request.form['input_text']
        input_stream = InputStream(input_text)
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()
        visitor = EvalVisitor()
        resultat = visitor.visit(tree)

        if isinstance(resultat,int):    #es tracta d'una evaluació amb resultat
            #limitem el maxim de resultats anteriors a 5, si n'hi han de nous es subistuiran amb politica FIFO
            string = "IN: " + input_text + "\t" + "OUT: " + str(resultat)
            resultats.append(string)
            if len(resultats) > 8: resultats.pop(0)

        elif isinstance(resultat,list): #es tracta d'una funció per guardar 
            #hem limitat el maxim de funcions a 5, si s'entren de noves es fa FIFO
            functions.append(getFunx(resultat))
            if len(functions) > 8: functions.pop(0)

        return render_template('base.html', results=resultats, functions=functions)




    return render_template('base.html')


if __name__ == '__main__':
    app.run()

