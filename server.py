from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template("checkerboard.html", cols = 8, rows = 8)

@app.route('/<int:rows>')
def rows_only(rows):
    return render_template("checkerboard.html", cols = 8, rows = rows)

if __name__ == "__main__":
    app.run(debug = True)