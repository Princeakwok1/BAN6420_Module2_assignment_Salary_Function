# Define the ZIP file and output directory
zip_file <- "Employee_Profile.zip"
output_dir <- "Employee_Profile"

# Unzip the folder
unzip(zip_file, exdir = output_dir)

# Get the extracted CSV file
csv_files <- list.files(output_dir, pattern = "\\.csv$", full.names = TRUE)

# Read and display the CSV file if found
if (length(csv_files) > 0) {
  employee_data <- read.csv(csv_files[1])
  print(employee_data)
} else {
  print("No CSV file found in the extracted folder.")
}
