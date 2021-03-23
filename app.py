from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

@app.route('/test')
def html_table():
    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/")
def home():
    return render_template("home.html")


# add a new page
@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/upload-csv")
# def upload_csv():
#     return render_template("upload_csv.html")

if __name__ == "__main__":
    app.run(debug=True)