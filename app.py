from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Payment Calculator')

@app.route('/Divide', methods=['GET', 'POST'])
def Divide():
    if request.method =='POST':
        form = request.form
        A = float(form['NumOne'])
        n = float(form['NumTwo'])
        i = float(form['NumThree'])
        D = float(form['NumFour'])
        n = years * monthly payments
        i = annual rate / monthly payments
        d = ((( 1 + i ) ^^n ) - 1 ) / ( i ( 1+ i) ^^n)
        calc =  A/D
        calc = round(number[, 2])
        return render_template('index.html', display=calc, pageTitle='Loan Payment Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
