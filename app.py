from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('pickle files/model.pkl', 'rb'))

# Load the scaler
#scaler = pickle.load(open('scaler.pkl', 'rb'))

# Load the encoders
le_town = pickle.load(open('pickle files/le_town.pkl', 'rb'))
le_flat_type = pickle.load(open('pickle files/le_flat_type.pkl', 'rb'))
le_storey_range = pickle.load(open('pickle files/le_storey_range.pkl', 'rb'))
le_flat_model = pickle.load(open('pickle files/le_flat_model.pkl', 'rb'))

# Define a route for the home page
@app.route('/')
def home():
    #return render_template('index.html', result='')
    return render_template('home.html', result='')

# Define a route for making predictions
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Log the entire form data for debugging
            form_data = request.form.to_dict()
            print(f"Form data received: {form_data}")

            # Get form data
            month = float(request.form['month'])
            town = float(le_town.transform([request.form['town']])[0])
            flat_type = float(le_flat_type.transform([request.form['flat_type']])[0])
            storey_range = float(le_storey_range.transform([request.form['storey_range']])[0])
            floor_area_sqm = float(request.form['floor_area_sqm'])
            flat_model = float(le_flat_model.transform([request.form['flat_model']])[0])
            lease_commence_year = float(request.form['lease_commence_year'])
            year = float(request.form['year'])

            # Prepare features
            features = np.array([[month, town, flat_type, storey_range, floor_area_sqm, flat_model, lease_commence_year, year]])
            #features = scaler.transform(features)

            # Make prediction
            output = model.predict(features)[0]
            output=round(np.exp(output))

            # Return the prediction as a response
            #return render_template('index.html', result=output)
            return render_template('home.html', result=output)

        except KeyError as e:
            return f"Form key error: {e}. Please check the form field names."
        except Exception as e:
            return f"An error occurred: {e}"

    #return render_template('index.html', result='')
    return render_template('home.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
