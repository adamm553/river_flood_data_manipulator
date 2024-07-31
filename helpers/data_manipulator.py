import pandas as pd

def clean_and_save_excel(file_path):
    # Load the data from the Excel file
    df = pd.read_excel(file_path)
    
    # Filter the DataFrame to keep only rows where 'Rok powodzi' can be converted to a numeric value
    df = df[pd.to_numeric(df['Rok powodzi'], errors='coerce').notnull()]
    
    # Save the modified DataFrame back to the same Excel file
    df.to_excel(file_path, index=False)
    
    print("DataFrame has been saved to", file_path)

# Example usage:
file_path = "powodzie_przerobione.xlsx"
clean_and_save_excel(file_path)
