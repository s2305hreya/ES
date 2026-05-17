//Create an application that prints your Name, seat number, department 5 times on separate lines using python

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        seat = request.form['seat']
        department = request.form['department']

        output = ""

        for i in range(5):
            output += f"Name: {name}<br>"
            output += f"Seat Number: {seat}<br>"
            output += f"Department: {department}<br><br>"

        return output

    return '''
    <h2>Student Details Form</h2>

    <form method="POST">

        Name:
        <input type="text" name="name"><br><br>

        Seat Number:
        <input type="text" name="seat"><br><br>

        Department:
        <input type="text" name="department"><br><br>

        <input type="submit" value="Submit">

    </form>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)






//Create an application to perform addition, multiplication, division and subtraction of two numbers. 
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():

    if request.method == 'POST':

        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        result = ""

        if operation == 'Addition':
            result = num1 + num2

        elif operation == 'Subtraction':
            result = num1 - num2

        elif operation == 'Multiplication':
            result = num1 * num2

        elif operation == 'Division':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Division by zero not possible"

        return f"<h2>Result: {result}</h2>"

    return '''
    <h2>Simple Calculator</h2>

    <form method="POST">

        Number 1:
        <input type="number" step="any" name="num1"><br><br>

        Number 2:
        <input type="number" step="any" name="num2"><br><br>

        <select name="operation">
            <option>Addition</option>
            <option>Subtraction</option>
            <option>Multiplication</option>
            <option>Division</option>
        </select>

        <br><br>

        <input type="submit" value="Calculate">

    </form>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)





//table
from flask import Flask

app = Flask(__name__)

@app.route('/')
def table():

    output = ""

    for i in range(1, 11):
        output += f"10 x {i} = {10*i}<br>"

    return output

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)





//fibonacci
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fibonacci():

    a = 0
    b = 1

    output = ""

    for i in range(10):
        output += str(a) + "<br>"

        c = a + b
        a = b
        b = c

    return output

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)




//Create an application to find the largest of three numbers.
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def largest():

    if request.method == 'POST':

        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])

        if num1 >= num2 and num1 >= num3:
            largest = num1

        elif num2 >= num1 and num2 >= num3:
            largest = num2

        else:
            largest = num3

        return f"<h2>Largest Number is: {largest}</h2>"

    return '''
    <h2>Find Largest Number</h2>

    <form method="POST">

        Number 1:
        <input type="number" name="num1"><br><br>

        Number 2:
        <input type="number" name="num2"><br><br>

        Number 3:
        <input type="number" name="num3"><br><br>

        <input type="submit" value="Find Largest">

    </form>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)