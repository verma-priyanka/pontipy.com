from flask import Flask, render_template
from pontiPy import *

app = Flask(__name__)

df = pd.read_csv('sampledata/coastal_1995_2000.csv', index_col=0)
df_change = pontiPy_Change(df)



@app.route("/")
def home():
    return render_template("home.html")


@app.route('/tabletest')
def html_table():
    return render_template('tabletest.html',  tables=[df_change.matrix().to_html(classes='table table-bordered table-sm')],
                                                        result = dict(df_change.exchange(2, Total=False)),
                                                        fa_all= df_change.loss(),
                                                        miss_all = df_change.gain(),
                                                        hit_all=df_change.persistence(),
                                                        ex_all=df_change.exchange(),
                                                        shift_all=df_change.shift(),
                                                        titles="")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help():
    return render_template("help.html")

# @app.route("/upload-csv")
# def upload_csv():
#     return render_template("upload_csv.html")

if __name__ == "__main__":
    app.run(debug=True)