# Medical Insurance Price Estimator

A machine learning project that estimates medical insurance charges using Support Vector Regression (SVR) and a Streamlit web application.

## Project Overview

This project uses demographic and lifestyle-related information to predict medical insurance charges based on a US insurance dataset.

The application provides a simple interface where users can enter their information and receive an estimated insurance charge.

**Disclaimer:** This project is for educational and demonstration purposes only. Predictions are not official insurance quotes and should not be treated as reliable estimates for insurance in India.

## Features

* Predicts estimated medical insurance charges.
* Uses Support Vector Regression (SVR).
* Applies feature scaling using StandardScaler.
* Encodes categorical features using OneHotEncoder.
* Uses a scikit-learn Pipeline for preprocessing and prediction.
* Tunes hyperparameters using GridSearchCV.
* Evaluates performance using R², MAE, and MSE.
* Provides an interactive interface built with Streamlit.
* Saves the trained model pipeline using Joblib.

## Dataset

The project uses the Medical Cost Personal Dataset, commonly distributed as `insurance.csv`.

### Input Features

| Feature  | Description                                      |
| -------- | ------------------------------------------------ |
| age      | Age of the individual                            |
| sex      | Sex of the individual as recorded in the dataset |
| bmi      | Body Mass Index                                  |
| children | Number of dependent children                     |
| smoker   | Smoking status                                   |
| region   | US residential region                            |

### Target Variable

* `charges`: Medical insurance charges in the source dataset, measured in US dollars.

**Dataset source:** Add the URL of the dataset you downloaded before publishing this repository.

## Machine Learning Workflow

1. Load and inspect the dataset.
2. Separate input features and the target variable.
3. Split the data into training and testing sets.
4. Scale numerical features using StandardScaler.
5. Encode categorical features using OneHotEncoder.
6. Combine preprocessing and SVR in a Pipeline.
7. Tune hyperparameters using GridSearchCV with cross-validation.
8. Evaluate the best estimator on the held-out test set.
9. Save the fitted pipeline using Joblib.
10. Load the pipeline in Streamlit and generate predictions from user inputs.

The entire fitted pipeline is saved, so the application automatically performs the same preprocessing used during training.

## Model Performance

The following results were obtained during the current training run.

| Metric                    |        Result |
| ------------------------- | ------------: |
| Cross-validation R²       |          0.56 |
| Test R²                   |        0.5723 |
| Mean Absolute Error (MAE) |     $3,795.42 |
| Mean Squared Error (MSE)  | 68,478,771.58 |

### Interpretation

* **R²:** The model explains approximately 57.2% of the variation in insurance charges in the test set.
* **MAE:** The average absolute prediction error is approximately $3,795.
* **MSE:** This measures the average squared prediction error, penalizing larger errors more heavily.

The model demonstrates moderate predictive performance. Individual predictions may differ substantially from actual charges.

## Technologies Used

* Python
* Pandas
* NumPy
* scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## Project Structure

```text
Insurance Price Estimator/
├── insurance.csv
├── Train.ipynb
├── model.pkl
├── stream_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

Update the filenames above if your actual project structure differs.

## Installation and Usage

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a virtual environment (recommended)

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

Ensure `model.pkl` is in the same directory as `stream_app.py`.

Run:

```bash
streamlit run stream_app.py
```

Open the local address displayed in the terminal to use the application.

## Limitations

* The dataset is relatively small and represents US insurance charges.
* The model's predictive performance is moderate.
* The available features do not capture every factor that influences insurance pricing.
* Predictions are estimates, not guaranteed prices or official insurance quotes.
* Performance may vary with different training data and train-test splits.

## Future Improvements

* Add exploratory data analysis visualizations.
* Inspect residuals to understand prediction errors.
* Establish a baseline model for comparison.
* Improve the user interface.
* Explore ways to improve generalization and predictive performance.

## Author

Developed as a machine learning and deployment practice project.
