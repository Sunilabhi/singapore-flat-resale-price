# House Price Prediction Web Application

This project is a Flask-based web application that predicts house prices using a trained machine learning model. The application allows users to input various features of a house and returns the predicted resale price.

## Features

- Predict house prices based on multiple input features:
  - Month
  - Town
  - Flat Type
  - Storey Range
  - Floor Area (sqm)
  - Flat Model
  - Lease Commence Year
  - Year
- Simple and user-friendly web interface.
- Model prediction results displayed on the same page.

## Requirements

- Python 3.6+
- Flask
- Pandas
- Numpy
- Pickle

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/house-price-prediction.git
    cd house-price-prediction
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the following files in the project directory:
   - `model.pkl`: The trained machine learning model.
   - `le_town.pkl`: Label encoder for the town feature.
   - `le_flat_type.pkl`: Label encoder for the flat type feature.
   - `le_storey_range.pkl`: Label encoder for the storey range feature.
   - `le_flat_model.pkl`: Label encoder for the flat model feature.

## Usage

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

3. Fill in the form with the required details and click the "Predict" button to get the predicted house price.

## File Structure

