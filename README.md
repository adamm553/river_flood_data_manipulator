# Flood Data Processing

This repository contains scripts for processing and transforming flood data from Excel spreadsheets. The workflow includes filtering columns, cleaning data, and transforming it into a more structured format. 

## Overview

The code consists of three main functions:

1. **filter_year_and_values**: This function filters the Excel data to retain only columns related to years and values, and removes rows where all values are missing.

2. **clean_and_save_excel**: This function cleans the data by ensuring that the 'Rok powodzi' column contains only numeric values.

3. **transform_excel**: This function transforms the cleaned data by splitting locations and restructuring it for easier analysis.

## Requirements

- Python 3.x
- `pandas` library
- `openpyxl` library (for reading and writing Excel files)

To install the required libraries, you can use pip:
pip install pandas openpyxl

## Usage

1. **Filtering and Cleaning Data**

   To filter columns and clean the data, use the `filter_year_and_values` function. This function reads an Excel file, selects columns related to years and values, and removes any rows where all values are missing. The filtered data is then saved to a new Excel file.

2. **Cleaning Data**

   To clean the Excel file and ensure that only numeric values are present in the 'Rok powodzi' column, use the `clean_and_save_excel` function. This function reads the specified Excel file, filters out rows where 'Rok powodzi' is not numeric, and saves the cleaned data back to the file.

3. **Transforming Data**

   To transform the cleaned data, use the `transform_excel` function. This function reads the cleaned Excel file, splits the locations in the 'Cieki, na których wystąpiła powódź' column, and restructures the data. Each location is paired with its corresponding year, and the transformed data is saved to a new Excel file.

## Files

- `powodzie.xlsx`: The initial Excel file containing flood data.
- `powodzie_przerobione.xlsx`: The intermediate file after filtering and cleaning.
- `transformed_powodzie.xlsx`: The final file after transformation.

## Notes

- Ensure that the initial file `powodzie.xlsx` contains the correct sheet and columns as expected by the scripts.
- Modify the sheet names and column names as needed based on the actual data.
