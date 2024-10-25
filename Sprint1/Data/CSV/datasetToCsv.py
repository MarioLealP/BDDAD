import pandas as pd
import os

def excel_to_csv(excel_file, output_folder):
    # Read the Excel file
    xls = pd.ExcelFile(excel_file, engine='openpyxl')
    
    # Loop through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read each sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Create a CSV file for each sheet
        csv_file = os.path.join(output_folder, f'{sheet_name}.csv')
        
        # Save the DataFrame to CSV
        df.to_csv(csv_file, index=False)
        print(f'Saved {sheet_name} to {csv_file}')

# Example usage:
excel_file = 'Dataset02_v2.xlsx'  # Path to the Excel file
output_folder = 'CSV'  # Path to the output folder for CSV files

excel_to_csv(excel_file, output_folder)
