
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Instantiate the Flask app
app = Flask(__name__)

# Route for the landing page
@app.route('/')
def main():
    return render_template('index.html')

# Route for processing prediction requests
@app.route('/submit', methods=['GET', 'POST'])
def process_prediction():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        # Capture and map the form data
        input_features = CustomData(
            Time=float(request.form.get('Time')),
            Ipv=float(request.form.get('Ipv')),
            Vpv=float(request.form.get('Vpv')),
            Vdc=float(request.form.get('Vdc')),
            ia=float(request.form.get('ia')),
            ib=float(request.form.get('ib')),
            ic=float(request.form.get('ic')),
            va=float(request.form.get('va')),
            vb=float(request.form.get('vb')),
            vc=float(request.form.get('vc')),
            Iabc=float(request.form.get('Iabc')),
            If=float(request.form.get('If')),
            Vabc=float(request.form.get('Vabc')),
            Vf=float(request.form.get('Vf'))
        )
        
        # Transform the data into a DataFrame
        df_input = input_features.to_dataframe()
        print("Input data as DataFrame:")
        print(df_input)
        print("Initiating prediction...")

        # Execute the prediction pipeline
        prediction_pipeline = PredictPipeline()
        print("Pipeline in action...")
        prediction_output = prediction_pipeline.predict(df_input)
        print("Prediction completed.")

        # Return the result to the template
        return render_template('home.html', results=prediction_output[0])

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0")
