from flask import Flask, render_template, request, url_for, redirect, flash
from pontiPy import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route("/tabletest", methods=['GET', 'POST'])
def html_table():
    ch_gain, ch_loss, _quan, ch_quan_gain, ch_quan_loss = [], [], [], [], []

    if request.method == 'POST':
        upload_csv = request.files['csvfile']
        df = pd.read_csv(upload_csv, index_col=0)
        df_change = pontiPy_Change(df)

        for i in df.columns.tolist():
            loss = "%s lost %s pixels" % (i, df_change.loss((df.columns.tolist()).index(i)))
            gains = "%s gained %s pixels" % (i, df_change.gain((df.columns.tolist()).index(i)))
            ch_loss.append(loss)
            ch_gain.append(gains)

            # _quantity.append(df_change.quantity((df.columns.tolist()).index(i)))
            _quan = df_change.quantity((df.columns.tolist()).index(i), label=True)
            if "Miss" in _quan:
                q_gain_label = "%s net gained %s pixels" % (i, round(_quan['Miss']))
                ch_quan_gain.append(q_gain_label)
                ch_quan_loss.append("%s net lost %s pixels" % (i, 0))
            elif "False Alarm" in _quan:
                q_loss_label = "%s net lost %s pixels" % (i, round(_quan['False Alarm']))
                ch_quan_loss.append(q_loss_label)
                ch_quan_gain.append("%s net gained %s pixels \n" % (i, 0))
            else:
                ch_quan_gain.append(0)
                ch_quan_loss.append(0)
    return render_template('tabletest.html',
                           tables=[df_change.matrix().to_html(classes='table table-bordered table-sm')],
                           result=dict(df_change.exchange(2, Total=False)),
                           fa_all=ch_loss,
                           miss_all=ch_gain,
                           quan_gain = ch_quan_gain,
                           quan_loss = ch_quan_loss,
                           hit_all=df_change.persistence(),
                           ex_all=df_change.exchange(),
                           shift_all=df_change.shift(),
                           columns="",
                           titles="")
        # return render_template('tabletest.html',
        #                        tables=[df.to_html(classes='table table-bordered table-sm', index=False)], titles="")


@app.route("/help", methods=['GET', 'POST'])
def help():
    return render_template("help_updated.html")


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


# @app.route("/upload-csv")
# def upload_csv():
#     return render_template("upload_csv.html")

if __name__ == "__main__":
    app.run(debug=True)
