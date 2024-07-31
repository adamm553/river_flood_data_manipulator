import pandas as pd

def transform_excel(input_file_path, output_file_path):

    df = pd.read_excel(input_file_path)
    
    transformed_data = []
    
    for _, row in df.iterrows():
        year = row['Rok powodzi']
        locations = row['Cieki, na których wystąpiła powódź'].split(', ')
        for location in locations:
            location = location.strip()  
            if location:  
                transformed_data.append([year, location])
    
    transformed_df = pd.DataFrame(transformed_data, columns=['Rok powodzi', 'Cieki, na których wystąpiła powódź'])
    
    transformed_df.to_excel(output_file_path, index=False)
    
    print("Transformed DataFrame has been saved to", output_file_path)
    
input_file_path = "powodzie_przerobione.xlsx"
output_file_path = "transformed_powodzie.xlsx"
transform_excel(input_file_path, output_file_path)
