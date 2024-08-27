# CSV Cleaner for Size and Color Processing

This Python script processes a CSV file containing product information, specifically handling size ranges and multiple color entries. It's designed to expand size ranges and color combinations into individual rows, making the data more granular and easier to work with.

## Features

- Fills in blank values in the first 4 columns with values from the previous row
- Expands size ranges (e.g., 'M～L', '90～160cm') into individual sizes
- Expands color combinations (e.g., 'ナチュラル・カラー') into individual colors
- Handles multiple sizes or colors separated by '・' or '･'
- Creates new rows for each size and color combination

## Requirements

- Python 3.x
- CSV file with product information (sizes in the 4th column, colors in the 5th column)

## Usage

1. Ensure your input CSV file is in the same directory as the script.
2. Update the `input_file` and `output_file` variables in the script if necessary.
3. Run the script: `python3 ua-csv-cleaner.py`
4. The processed data will be saved in the specified output file.

## Input File Format

The input CSV file should have the following structure:
- The 4th column (index 3) contains size information
- The 5th column (index 4) contains color information

## Output

The script generates a new CSV file with:
- Blank values in the first 4 columns filled from the previous row
- Size ranges expanded into individual sizes
- Color combinations split into separate rows
- A new row for each size and color combination

## Example

Input row: 
```
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

Make sure to back up your original CSV file before running the script, as it will create a new file with the processed data.