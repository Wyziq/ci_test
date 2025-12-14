from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def say_hello():
    return render_template("home.html", message="Hello, Flask!")

@app.route('/calc', methods=['GET'])
def calc():
    op = request.args.get('op')  # "add" или "sub"

    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - НЕ числа'

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    else:
        return "Неизвестная операция, используй op=add или op=sub"

    return str(result)

if __name__ == "__main__":
    app.run()