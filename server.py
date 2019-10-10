from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['box']
    print (request.form)

    return render_template("result.html", name_on_template= name_from_form, location_on_template= location_from_form, language_on_template= language_from_form, textbox_on_template=comments_from_form)



if __name__ == "__main__":
    app.run(debug=True)