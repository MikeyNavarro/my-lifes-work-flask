from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/<int:num1>')

def rowLength(num1):
    return render_template('rowLength.html', num1 = num1)



@app.route('/<int:x>/<int:y>')

def xy(x,y):
    return render_template('xy.html', x = int(x), y = int(y))


if __name__ == '__main__':
  app.run(debug=True)