from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Payment Calculator')
@app.route('/add', methods=['GET', 'post'])
def addition():
    if request.method =='post':
        form = request.form
        A = int(form['A'])
        D = int(form['D'])
        calc = A + D
        return render_template('index.html', display=calc, pageTitle='Loan Payment Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
