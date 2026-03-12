from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "women_ai_project"


# LOGIN PAGE
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect("/idea")

    return render_template("login.html")


# IDEA SELECTION
@app.route("/idea", methods=["GET","POST"])
def idea():

    if request.method == "POST":
        idea = request.form["idea"]
        session["idea"] = idea
        return redirect("/details")

    return render_template("idea.html")


# USER DETAILS
@app.route("/details", methods=["GET","POST"])
def details():

    if request.method == "POST":

        budget = request.form["budget"]
        location = request.form["location"]
        experience = request.form["experience"]

        idea = session["idea"]

        # Prediction Logic

        if idea == "Agriculture":
            result = "Start organic vegetable farming and sell through local markets and WhatsApp groups. Expected monthly income ₹15000 - ₹30000."

        elif idea == "Tailoring":
            result = "Start home based tailoring for women and kids clothes. Promote through Instagram and local customers. Expected income ₹10000 - ₹25000."

        elif idea == "Home Bakers":
            result = "Sell cakes, cookies and snacks through Instagram and local orders. Focus on birthday and custom cakes. Expected income ₹20000 - ₹40000."

        elif idea == "Handicrafts":
            result = "Create handmade crafts and sell through exhibitions and online marketplaces. Expected income ₹10000 - ₹20000."

        elif idea == "Beauty Products":
            result = "Prepare natural beauty products like soap and face packs. Sell through online platforms and local stores. Expected income ₹15000 - ₹30000."

        else:
            result = "Start small home business and promote through social media."

        return render_template("result.html", result=result)

    return render_template("details.html")


# RESULT PAGE
@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)