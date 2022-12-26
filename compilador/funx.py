from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
from flask import Flask, request, render_template

app = Flask(__name__)

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
        result = visitor.visit(tree)
        return render_template('base.html', result=result)
        
    return render_template('base.html')

if __name__ == '__main__':
    app.run()