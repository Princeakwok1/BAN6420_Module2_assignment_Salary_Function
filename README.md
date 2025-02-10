# BAN6420_Module2_assignment_Salary_Function
Overview

This project involves analyzing salary data using Python and R. The main objectives are:
1. Importing salary data from a CSV file (Total.csv).
2. Creating a function to retrieve employee details.
3. Processing the data using a dictionary.
4. Implementing error handling to manage potential issues.
5. Exporting employee details into a CSV file and compressing it into a ZIP folder (Employee_Profile).
6. Using R to unzip and display the employee details.


# Dataset. 
The dataset is provided in a CSV format with the following columns:
1. EmployeeName:     Name of the employee
2. JobTitle:         Employee's job title
3. BasePay:          Basic salary
4. OvertimePay:      Overtime earnings
5. OtherPay:         Additional earnings
6. Benefits:         Employee benefits
7. TotalPay:         Sum of base, overtime, and other pay
8. TotalPayBenefits: Total earnings including benefits
9. Year:             Year of salary data


# Prerequisites
1. Python Dependencies
2. Ensure you have the required Python libraries installed:
3. pip install pandas


# R Dependencies
1. Make sure you have R installed with necessary libraries:
2. install.packages("utils")

# Project Files
#  1. module_2_assignment_salary_function.py (Python Script)
1. This script performs the following tasks:
2. Reads the Total.csv file.
3. Implements a function to retrieve employee details.
4. Stores data in a dictionary.
5. Handles errors such as missing values and incorrect names.
6. Exports employee details into a CSV file.
7. Zips the CSV file into Employee_Profile.zip.

# Usage

1. Run the Python script:
python module_2_assignment_salary_function.py
2. Upon execution, the script will generate an Employee_Profile.zip containing the employee details.


# 2. unzip_and_display.R (R Script)
1. This script extracts and reads the employee CSV file from the ZIP archive.
Usage
1. Run the R script in R:
source("unzip_and_display.R")
2. The script will unzip Employee_Profile.zip, read the extracted CSV, and display its contents.


# Expected Output
Python Script Output:
1. Successfully retrieves employee details if the name exists.
2. Saves employee data as a CSV file.
3. Compresses the CSV file into a ZIP archive.


# R Script Output:
1. Extracts the ZIP file.
2. Reads the CSV file and displays employee details.


Author
1. Name:           Prince Nsidibe
2. Course:         BAN 6420 - Python and R
3. Institution:    Nexford University

