from flask import Flask, render_template, request, url_for

import joblib

model = joblib.load("./models/standard_scaler")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        # to recieve the data 
        nitrogen = int(request.form["nitrogen"])
        phosphorus = int(request.form["phosphorus"])
        potassium = int(request.form["potassium"]) 
        temperature = (request.form["temperature"] )
        humidity = (request.form["humidity"]) 
        ph = (request.form["ph"]) 
        rainfall = (request.form["rainfall"]) 
        
    unseen_data = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]
    prediction = str(model(unseen_data)[0])
   
    return render_template("final.html", output = prediction)
    
if __name__ == "__main__":
    app.run(debug=True)
    

    
