# End to End Data Science Project

This project is a small end-to-end machine learning web app that predicts a student’s maths score from basic background and exam-preparation details. It includes the full flow from data preparation and model training to a Flask-based prediction interface.

## Overview

The application uses a trained regression model along with a preprocessing pipeline saved in the `artifacts/` directory. A user can open the web interface, enter a student profile, and receive a predicted maths score instantly.

The project is organized into the following layers:

- Data ingestion from the raw student dataset
- Data transformation with imputation, encoding, and scaling
- Model training and evaluation across multiple regressors
- Flask web application for prediction
- Jinja templates for the user interface

## Features

- Simple web form for student input
- End-to-end preprocessing and prediction pipeline
- Multiple regression models evaluated during training
- Saved model and preprocessing artifacts for fast inference
- Minimal, clean HTML interface with no external frontend framework required

## Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- Jinja2 templates

## Project Structure

```text
app.py
README.md
requirements.txt
setup.py
artifacts/
	data.csv
	test.csv
	train.csv
	model.pkl
	preprocessor.pkl
src/
	exception.py
	logger.py
	utils.py
	components/
		data_ingestion.py
		data_transformation.py
		model_trainer.py
	pipeline/
		predict_pipeline.py
		train_pipeline.py
	templates/
		home.html
		index.html
```

## How It Works

### 1. Data Ingestion

The raw dataset is loaded and split into train and test sets. Those files are stored in the `artifacts/` folder.

### 2. Data Transformation

The preprocessing pipeline handles:

- Missing values
- Categorical encoding
- Feature scaling

The fitted transformer is saved as `artifacts/preprocessor.pkl`.

### 3. Model Training

Several regression models are evaluated, and the best one is saved as `artifacts/model.pkl`.

### 4. Prediction

The Flask app loads the trained model and preprocessor, transforms the form input, and returns a predicted maths score.

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Prediction Page Inputs

The prediction form expects the following values:

- Gender
- Race or ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

## Notes

- The templates are stored in `src/templates/`, so the Flask app is configured to use that folder.
- The inference pipeline expects both `artifacts/model.pkl` and `artifacts/preprocessor.pkl` to exist.
- If you retrain the project, make sure the preprocessing artifact keeps the same filename so prediction continues to work.

## Troubleshooting

- If Flask is missing, reinstall dependencies with `pip install -r requirements.txt`.
- If templates are not loading, confirm the app is pointing to `src/templates`.
- If prediction fails with a missing artifact error, verify that `artifacts/model.pkl` and `artifacts/preprocessor.pkl` are present.

## Example Output

After submitting the form, the app shows the predicted maths score directly on the page.

## License

No license has been specified for this project.