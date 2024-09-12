# Supply Unchained - Supply Chain Data Processing

This project contains Python scripts for processing Excel files and CSV files containing apparel supply chain information, specifically handling product size ranges and color entries. It's designed to expand size ranges and color combinations into individual rows, making the data more granular and easier to work with.

## Scripts

### 1. ua-excel-cleaner.py

This script processes an Excel file, expands size ranges and color combinations, and outputs a CSV file.

#### Features

- Fills in blank values in the first 4 columns with values from the previous row
- Expands size ranges (e.g., 'M～L', '90～160cm') into individual sizes
- Expands color combinations (e.g., 'ナチュラル・カラー') into individual colors
- Handles multiple sizes or colors separated by '・' or '･'
- Creates new rows for each size and color combination

#### Usage

`python ua-excel-cleaner.py <input_excel_file> <output_csv_file>`

### 2. ua-csv-cleaner.py

Same features as `ua-excel-cleaner.py` but for CSV files.

#### Usage

`python ua-csv-cleaner.py <input_csv_file> <output_csv_file>`


### 3. convert.py

This script converts an Excel file to a CSV file, performing some basic cleaning operations.

#### Features

- Removes the first two rows of the Excel file
- Removes the first column
- Sets the first row as the header
- Cleans whitespace from headers

#### Usage

 `python convert.py <input_excel_file> <output_csv_file>`


## Requirements

- Python 3.x
- pandas
- openpyxl (for Excel file support)

## Input File Format

The input Excel file should have the following structure:
- The 4th column (index 3) contains size information
- The 5th column (index 4) contains color information

## Output

Both scripts generate new CSV files with cleaned and processed data.

## Example Output (ua-excel-cleaner.py)

Input row: 

```csv
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,S～XL,ホワイト・カラー,"¥4,950 "," 1,650 "
```

Output rows: 

```csv
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,S,ホワイト,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,S,カラー,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,M,ホワイト,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,M,カラー,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,L,ホワイト,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,L,カラー,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,XL,ホワイト,"¥4,950 "," 1,650 "
5214,01,10.0オンス スウェット プルオーバー パーカ（裏パイル）〈アダルト〉,XL,カラー,"¥4,950 "," 1,650 "
```

## Note

Make sure to back up your original files before running the scripts, as they will create new files with the processed data.
