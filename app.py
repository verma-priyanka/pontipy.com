from flask import Flask, request, url_for, redirect, render_template, flash
import pandas as pd


app = Flask(__name__)


# df = pd.DataFrame({'1985': [10, 20, 30, 3, 4],
#                    '1986': [5, 6, 7, 8, 9],
#                    '1987': ['a', 'b', 'c', 'd', 'e'],
#                    '1988': ['a', 'b', 'c', 'd', 'e'],
#                    '1989': ['a', 'b', 'c', 'd', 'e'],
#                    '1990': ['a', 'b', 'c', 'd', 'e'],
#                    '1991': [5, 6, 7, 8, 9],
#                    '1992': [5, 6, 7, 8, 9],
#                    '1993': [5, 6, 7, 8, 9],
#                    '1994': [5, 6, 7, 8, 9],
#                    '1995': [5, 6, 7, 8, 9]})


@app.route("/", methods=['GET', 'POST'])
def home():

    # # enable the run button in home page
    # if request.method == 'POST':
    # #     # do stuff when the form is submitted
    # #     # return file.filename
    # #     # redirect to end the POST handling
    # #     # the redirect can be to the same route or somewhere else
    #     return redirect(url_for('tabletest'))


    return render_template("home.html")




@app.route("/tabletest", methods=['GET', 'POST'])
def tabletest():

    # procedure after clicking Run button in the home page
    if request.method == 'POST':

        # obtain the csv file
        upload_csv = request.files['csvfile']

        # upload_csv.save(os.path.join(app.config["CSV_UPLOADS"], upload_csv.filename))
        # if not upload_csv:
        #     flash('Please upload a correct csv table!')
        #     return redirect(url_for('home'))
        # filename = secure_filename(upload_csv.filname)

        # read the uploaded csv file   ---------- need to figure out how to store the file localy(may fixing errors caused by refreshing the page) for users since we are not using a database
        df = pd.read_csv(upload_csv)

        return render_template('tabletest.html', tables=[df.to_html(classes='table table-bordered table-sm', index=False)], titles="")

    # clicking on the table page without a csv uploaded
    else:
        return render_template('tabletest.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help", methods=['GET', 'POST'])
def help():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True)