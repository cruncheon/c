import pandas as pd
import sys

def excel_to_csv(excel_file, csv_file):
    # Read the Excel file
    df = pd.read_excel(excel_file, header=None)
    
    # Delete the first two rows
    df = df.iloc[2:]
    
    # Delete the first column
    df = df.iloc[:, 1:]
    
    # Reset the index
    df = df.reset_index(drop=True)
    
    # Set the first row as header
    df.columns = df.iloc[0]
    df = df[1:]
    
    # Remove whitespace from headers
    df.columns = df.columns.str.strip().str.replace(' ', '')
    
    # Save to CSV
    df.to_csv(csv_file, index=False)
    print(f"Converted {excel_file} to {csv_file} (first two rows and first column removed, headers cleaned)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_excel_file> <output_csv_file>")
    else:
        excel_to_csv(sys.argv[1], sys.argv[2])