import csv
import re
import sys

def expand_size_range(size_range):
    sizes = ['Women', 'Men', 'WM', 'WL', 'JS', 'JM', 'JL', '150', '160', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL', '6XL', '7XL']
    size_mapping = {'LL': 'XL', '3L': 'XXL', '4L': '3XL', '5L': '4XL', 'XXXL': '3XL', 'XXXXL': '4XL', 'XXXXXL': '5XL'}  # Add more mappings if needed
    
    def normalize_size(size):
        return size_mapping.get(size, size)
    
    if '-' in size_range:
        start, end = map(normalize_size, size_range.split('-'))
        if start.isdigit() and end.isdigit():
            start_num = int(start)
            end_num = int(end)
            return [str(i) for i in range(start_num, end_num+1, 10)]
        else:
            try:
                start_index = sizes.index(start)
                end_index = sizes.index(end)
                return sizes[start_index:end_index+1]
            except ValueError:
                # If size not found, return the original range
                return [size_range]
    elif '・' in size_range or '･' in size_range:
        return [normalize_size(size) for size in size_range.replace('･', '・').split('・')]
    else:
        return [normalize_size(size_range)]

def expand_colors(color_string):
    return color_string.replace('･', '・').split('・')

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        previous_row = [''] * len(header)

        for row in reader:
            for i in range(4):  # Process the first 4 columns, if blank string, copy value from previous row
                if row[i] == '':
                    row[i] = previous_row[i]

            sizes = expand_size_range(row[2])
            colors = expand_colors(row[3])

            if not colors:
                colors = ['']  # Use an empty string if no color is specified

            for size in sizes:
                for color in colors:
                    new_row = row.copy()
                    new_row[2] = size
                    new_row[3] = color if color else row[3]  # Keep original color if expanded color is empty
                    writer.writerow(new_row)

            previous_row = row

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python truss-csv-cleaner.py <input_csv_file> <output_csv_file>")
    else:
        process_csv(sys.argv[1], sys.argv[2])