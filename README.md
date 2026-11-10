
# Iris Flower Classification Using Machine Learning

## 1. Project Overview

This project implements a Machine Learning-based Iris Flower Classification system that predicts the species of an Iris flower using four physical measurements.

The system uses a Random Forest Classifier and provides a graphical user interface built with Python Tkinter. Prediction records are stored in an SQLite database.

## 2. Problem Statement

Manual identification of Iris flower species can be time-consuming. This project aims to automate the classification process using supervised machine learning.

## 3. Objectives

- Understand and analyze the Iris dataset.
- Perform data preprocessing and exploratory data analysis.
- Compare multiple machine learning algorithms.
- Train and evaluate a classification model.
- Improve model performance using hyperparameter tuning.
- Develop a graphical user interface.
- Store prediction history using SQLite.

## 4. Dataset Description

The Iris dataset is obtained from Scikit-learn.

- Original records: 150
- Features: 4
- Target classes: 3
- Missing values: 0
- Duplicate records: 1
- Cleaned records: 149

### Input Features

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

### Target Classes

- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 5. Data Preprocessing

The following preprocessing operations were performed:

- Loaded the Iris dataset.
- Checked missing values.
- Identified duplicate records.
- Removed one duplicate record.
- Saved the cleaned dataset as `data/iris_cleaned.csv`.

The final dataset contains 149 records and 5 columns.

## 6. Exploratory Data Analysis

Exploratory Data Analysis was performed using Matplotlib.

Visualizations include:

- Species distribution.
- Feature distribution histograms.
- Sepal feature scatter plot.
- Petal feature scatter plot.
- Feature correlation heatmap.

## 7. Feature and Target Selection

Input (X): Four flower measurements.

Target (Y): Iris species.

The dataset was divided into:

- Training data: 80%
- Testing data: 20%

A fixed random state of 42 and stratified splitting were used.

## 8. Machine Learning Algorithms

Three classification algorithms were compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

## 9. Model Comparison

| Algorithm | Accuracy |
|---|---:|
| Logistic Regression | 93.33% |
| Decision Tree | 93.33% |
| Random Forest | 93.33% |

All three algorithms achieved the same test accuracy.

## 10. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

The baseline Random Forest achieved:

- Accuracy: 93.33%
- Precision: 93.33%
- Recall: 93.33%
- F1 Score: 93.33%

It correctly classified 28 out of 30 test samples.

## 11. Model Improvement

Hyperparameter tuning was performed on Random Forest using GridSearchCV and 5-fold cross-validation.

Parameters tested:

- Number of estimators: 50, 100, 150
- Maximum depth: None, 3, 5
- Minimum samples split: 2, 4

Best parameters:

- n_estimators: 50
- max_depth: None
- min_samples_split: 2

Results:

| Model | Accuracy | F1 Score |
|---|---:|---:|
| Baseline Random Forest | 93.33% | 93.33% |
| Tuned Random Forest | 90.00% | 89.97% |

The tuned model performed worse on the held-out test set. Therefore, the baseline Random Forest was selected as the final model.

## 12. Final Model

The final Random Forest model uses 100 estimators.

It was retrained on all 149 cleaned records after evaluation.

Saved model: `models/iris_model.pkl`

## 13. Front-End Development

A graphical user interface was developed using Python Tkinter.

Features:

- Accepts four flower measurements.
- Predicts the Iris species.
- Displays the classification result.
- Saves prediction records to SQLite.

## 14. Database Implementation

SQLite is used for storing flower measurements and prediction history.

Database tables:

- species
- flowers
- predictions

Database operations include:

- INSERT
- SELECT
- WHERE
- ORDER BY
- JOIN
- GROUP BY
- AVG

Database normalization and primary/foreign key relationships were also examined.

## 15. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SQLite
- Tkinter

## 16. Project Structure

```text
iris classification/
│
├── data/
│   └── iris_cleaned.csv
│
├── models/
│   └── iris_model.pkl
│
├── database/
│
├── reports/
│   ├── eda/
│   ├── model_comparison.csv
│   └── model_improvement.csv
│
├── app.py
├── predict.py
├── train_model.py
├── test_final_model.py
├── compare_models.py
├── improve_model.py
├── dataset_analysis.py
├── preprocess.py
├── eda.py
├── requirements.txt
└── README.md
```

## 17. How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the model

```bash
python train_model.py
```

### Step 3: Launch the application

```bash
python app.py
```

### Step 4: Enter flower measurements

Enter sepal length, sepal width, petal length and petal width to obtain the predicted species.

## 18. Conclusion

The project successfully demonstrates a supervised machine learning classification workflow, from dataset preprocessing and exploratory analysis to algorithm comparison, model evaluation, hyperparameter tuning and graphical application development.

The final Random Forest model achieved 93.33% accuracy on the held-out test dataset.

SQLite provides persistent storage for prediction history, making the application a combination of machine learning and database technologies.
