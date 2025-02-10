import pandas as pd
import os
import zipfile

# Load the data and handle non-numeric values
file_path = "Total.csv"

df = pd.read_csv(file_path, low_memory=False)

# Convert problematic columns to numeric, replacing non-numeric values with NaN
cols_to_convert = ["BasePay", "OvertimePay", "OtherPay", "Benefits"]
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert, replacing errors with NaN

# Ensure EmployeeName is unique before setting it as the index
df = df.drop_duplicates(subset=["EmployeeName"])
df = df.set_index("EmployeeName")
salary_dict = df.to_dict(orient="index")

# Function to retrieve employee details
def get_employee_details(name):
    try:
        emp_data = df.loc[[name]]
        if emp_data.empty:
            return "Employee not found."
        return emp_data
    except KeyError:
        return "Employee not found."
    except Exception as e:
        return f"Error occurred: {e}"

# Export employee details and zip them
def export_employee_details(name):
    try:
        emp_data = get_employee_details(name)
        if isinstance(emp_data, str):  # If employee not found
            print(emp_data)
            return
        
        folder_name = "Employee_Profile"
        os.makedirs(folder_name, exist_ok=True)
        
        file_name = f"{folder_name}/{name}_details.csv"
        emp_data.to_csv(file_name, index=True)  # Ensure file is written
        
        zip_name = "Employee_Profile.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(file_name, os.path.basename(file_name))
        
        print(f"Employee details exported and zipped as {zip_name}")
    except Exception as e:
        print(f"Error occurred while exporting: {e}")

# Ask for an employee name to export
employee_name = input("Enter an employee name to export: ").strip()
export_employee_details(employee_name)

print("Python script execution completed!")
