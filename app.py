from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = ""
    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])

        # BMI formula: weight (kg) / [height (m)]²
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
