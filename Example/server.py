from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)


@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/process/", methods=["POST"])
def process_form():
    print(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)