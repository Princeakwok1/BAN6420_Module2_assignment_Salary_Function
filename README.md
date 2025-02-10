# BAN6420_Module2_assignment_Salary_Function
Overview

This project involves analyzing salary data using Python and R. The main objectives are:
Importing salary data from a CSV file (Total.csv).
Creating a function to retrieve employee details.
Processing the data using a dictionary.
Implementing error handling to manage potential issues.
Exporting employee details into a CSV file and compressing it into a ZIP folder (Employee_Profile).
Using R to unzip and display the employee details.


# Dataset
The dataset is provided in a CSV format with the following columns:
EmployeeName:     Name of the employee
JobTitle:         Employee's job title
BasePay:          Basic salary
OvertimePay:      Overtime earnings
OtherPay:         Additional earnings
Benefits:         Employee benefits
TotalPay:         Sum of base, overtime, and other pay
TotalPayBenefits: Total earnings including benefits
Year:             Year of salary data


# Prerequisites
Python Dependencies
Ensure you have the required Python libraries installed:
pip install pandas


# R Dependencies
Make sure you have R installed with necessary libraries:
install.packages("utils")

Project Files
# 1.  
# module_2_assignment_salary_function.py (Python Script)
This script performs the following tasks:
Reads the Total.csv file.
Implements a function to retrieve employee details.
Stores data in a dictionary.
Handles errors such as missing values and incorrect names.
Exports employee details into a CSV file.
Zips the CSV file into Employee_Profile.zip.

# Usage

Run the Python script:
python module_2_assignment_salary_function.py
Upon execution, the script will generate an Employee_Profile.zip containing the employee details.


# 2. 
# unzip_and_display.R (R Script)
This script extracts and reads the employee CSV file from the ZIP archive.
Usage
Run the R script in R:
source("unzip_and_display.R")
The script will unzip Employee_Profile.zip, read the extracted CSV, and display its contents.


# Expected Output
Python Script Output:
Successfully retrieves employee details if the name exists.
Saves employee data as a CSV file.
Compresses the CSV file into a ZIP archive.


# R Script Output:
Extracts the ZIP file.
Reads the CSV file and displays employee details.


Author
Name:         Prince Nsidibe
Course:       BAN 6420 - Python and R
Institution:  Nexford University

