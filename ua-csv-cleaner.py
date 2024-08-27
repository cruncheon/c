import csv
import re

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

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        previous_row = [''] * len(header)

        for row in reader:
            for i in range(4):  # Process only the first 4 columns
                if row[i] == '':
                    row[i] = previous_row[i]

            sizes = expand_size_range(row[3])
            colors = expand_colors(row[4])

            for size in sizes:
                for color in colors:
                    new_row = row.copy()
                    new_row[3] = size
                    new_row[4] = color
                    writer.writerow(new_row)

            previous_row = row

# Usage
input_file = 'input.csv'
output_file = 'output.csv'
process_csv(input_file, output_file)