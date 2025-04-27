# Carbon Footprint Prediction and Evaluation System using-Machine-Learning

## Overview
This project aims to predict the carbon footprint of various activities and evaluate the prediction accuracy using the R² score. The project involves a data processing pipeline where actual carbon footprint data and predicted values are merged, and the R² score is calculated to evaluate the model’s performance.

## Features
- **Data Merging**: Merges two datasets: one with actual carbon footprint values and another with predicted carbon footprint values, based on a common ID column.
- **R² Score Calculation**: Calculates the R² score (coefficient of determination) to evaluate how well the prediction model is performing.
- **Final Score Calculation**: A custom formula is used to calculate the final prediction score, which is scaled between 0 and 100.

## Installation

### Prerequisites

Make sure to have Python installed on your system. You also need to install the following Python libraries:

```
pip install pandas scikit-learn

Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/Mazid2003/Carbon-Footprint-Estimator-using-Machine-Learning.git

Running the Project

Download or prepare two CSV files:

actual_test_values.csv: Contains the actual carbon footprint values.

your_submission.csv: Contains the predicted carbon footprint values.

Place the CSV files in the project directory.

Run the Python script to calculate the R² score and final accuracy score:

python carbon_footprint_evaluation.py

The script will output the R² score and the final score based on the prediction accuracy.

Code Walkthrough

Data Merging

The project merges the actual and predicted data based on the ID column in both datasets. This allows us to compare the actual carbon footprint with the predicted values.

R² Score Calculation

The R² score is calculated using sklearn.metrics.r2_score, which measures how well the predicted values match the actual values. The score ranges from 0 to 1, where 1 represents perfect predictions, and 0 indicates no correlation.

Final Score Calculation

The R² score is multiplied by 100 and capped at a minimum of 0 to generate a final score. This score serves as a simple way to evaluate the prediction accuracy of the model.

**Technologies Used**

Python: The programming language used for this project.

Pandas: Used for data manipulation and merging datasets.

Scikit-learn: Provides the r2_score function for evaluating model performance.

Jupyter Notebook: Used for testing and visualizing the workflow.

Example Output

R² Score: 0.85
Final Score: 85

**Potential Enhancements**

Integrate machine learning models (e.g., linear regression) to improve the accuracy of carbon footprint predictions.

Visualize the R² score and other evaluation metrics with charts.

Use real-time data sources to predict carbon footprints dynamically based on various activities.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

