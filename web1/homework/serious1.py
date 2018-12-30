from flask import Flask

serious1 = Flask(__name__)

@serious1.route("/")
def home():
    return "HOME"

@serious1.route("/bmi/<int:weight>/<int:height>")
def calc(weight, height):
    bmi = weight/((height/100)**2)
    if bmi < 16:
        return "BMI = " + str(bmi) + " Severely underweight!"
    elif (bmi < 18.5) and (bmi >= 16):
        return "BMI = " + str(bmi) + " Underweight!"
    elif (bmi < 25) and (bmi >= 18.5):
        return "BMI = " + str(bmi) + " Normal!"
    elif (bmi < 30) and (bmi >= 25):
        return "BMI = " + str(bmi) + " Overweight!"
    else:
        return "BMI = " + str(bmi) + "  Obese!"

if __name__ == "__main__": 
    serious1.run(debug=True)
