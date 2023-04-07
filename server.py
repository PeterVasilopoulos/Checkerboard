from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template("checkerboard.html", cols = 8, rows = 8)

@app.route('/<int:rows>')
def rows_only(rows):
    return render_template("checkerboard.html", cols = 8, rows = rows)

@app.route('/<int:rows>/<int:cols>')
def rows_cols(rows, cols):
    return render_template("checkerboard.html", cols = cols, rows = rows)

@app.route('/<int:rows>/<int:cols>/<color1>')
def rows_cols_colors1(rows, cols, color1):
    return render_template("checkerboard.html", cols = cols, rows = rows, color1 = color1)

@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def rows_cols_colors2(rows, cols, color1, color2):
    return render_template("checkerboard.html", cols = cols, rows = rows, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug = True)