import csv
import re
import pandas as pd
import sys

def expand_size_range(size_range):
    if '～' in size_range:
        start, end = size_range.split('～')
        if start.isdigit() and end.endswith('cm') and end[:-2].isdigit():
            start_num = int(start)
            end_num = int(end[:-2])
            return [f"{i}cm" for i in range(start_num, end_num+1, 10)]
        else:
            sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', 'XXXXL', '5XL', '6XL']
            try:
                start_index = sizes.index(start)
                end_index = sizes.index(end)
                return sizes[start_index:end_index+1]
            except ValueError:
                # If size not found, return the original range
                return [size_range]
    elif '・' in size_range or '･' in size_range:
        return size_range.replace('･', '・').split('・')
    else:
        return [size_range]

def expand_colors(color_string):
    return color_string.replace('･', '・').split('・')

def process_excel(input_file, output_file):
    # Read Excel file
    df = pd.read_excel(input_file, header=None)
    
    # Delete the first two rows
    df = df.iloc[2:]

    # Delete the first column
    df = df.iloc[:, 1:]
    
    # Reset index
    df = df.reset_index(drop=True)

    # Set the first row as header
    df.columns = df.iloc[0]
    df = df[1:]
    
    # Remove whitespace from headers
    df.columns = df.columns.str.strip().str.replace(' ', '')
    
    # Convert DataFrame to list of lists
    data = df.values.tolist()
    
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write header
        writer.writerow(df.columns.tolist())
        
        previous_row = [''] * len(df.columns)
        
        for row in data:
            for i in range(4):  # Process only the first 4 columns
                if pd.isna(row[i]) or row[i] == '':
                    row[i] = previous_row[i]
            
            sizes = expand_size_range(str(row[3]))
            colors = expand_colors(str(row[4]))
            
            for size in sizes:
                for color in colors:
                    new_row = row.copy()
                    new_row[3] = size
                    new_row[4] = color
                    writer.writerow(new_row)
            
            previous_row = row

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ua-excel-cleaner.py <input_excel_file> <output_csv_file>")
    else:
        process_excel(sys.argv[1], sys.argv[2])