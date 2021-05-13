from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


df = pd.DataFrame({'1985': [10, 20, 30, 3, 4],
                   '1986': [5, 6, 7, 8, 9],
                   '1987': ['a', 'b', 'c', 'd', 'e'],
                   '1988': ['a', 'b', 'c', 'd', 'e'],
                   '1989': ['a', 'b', 'c', 'd', 'e'],
                   '1990': ['a', 'b', 'c', 'd', 'e'],
                   '1991': [5, 6, 7, 8, 9],
                   '1992': [5, 6, 7, 8, 9],
                   '1993': [5, 6, 7, 8, 9],
                   '1994': [5, 6, 7, 8, 9],
                   '1995': [5, 6, 7, 8, 9]})


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/tabletest')
def html_table():
    return render_template('tabletest.html',  tables=[df.to_html(classes='table table-bordered table-sm')], titles="")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help():
    return render_template("help_updated.html")

# @app.route("/upload-csv")
# def upload_csv():
#     return render_template("upload_csv.html")

if __name__ == "__main__":
    app.run(debug=True)