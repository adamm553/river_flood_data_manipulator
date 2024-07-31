import pandas as pd

def filter_year_and_values(file_path, output_path):
    # Load the specific sheet (Sheet 2)
    sheet_name = 'zalacznik1'
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Identify the 'Year' column
    year_column = df.columns[df.columns.str.contains("Year", case=False, na=False)].tolist()
    
    # Identify the value columns (those not containing 'Year')
    value_columns = df.columns[~df.columns.str.contains("Year", case=False, na=False)].tolist()
    
    # Filter the DataFrame to keep only these columns
    columns_to_keep = year_column + value_columns
    filtered_df = df[columns_to_keep].dropna(how='all')  # Drop rows where all columns are NaN
    
    # Save the filtered data into a new Excel file
    filtered_df.to_excel(output_path, index=False)
    print(f"Filtered data saved to {output_path}")

# Paths to the input and output Excel files
input_file = 'powodzie.xlsx'  # Replace with your input file path
output_file = 'powodzie_przerobione.xlsx'  # Output file path

# Run the filter function
filter_year_and_values(input_file, output_file)


