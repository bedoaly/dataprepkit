import pandas as pd
def load_file(file_path):
    extension = file_path.split('.')[-1].lower()

    if extension == 'csv':
        df = pd.read_csv(file_path)
    elif extension == 'json':
        df = pd.read_json(file_path)
    elif extension in ['xls', 'xlsx']:
        df = pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: .{extension}")

    return df
def analyze_dataframe(df):
    rows, cols = df.shape
    print(f"The dataset contains {rows} rows and {cols} columns.")
def count_missing_values(df, column_name):

    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' does not exist in the DataFrame.")
        return None

    missing_count = 0
    for value in df[column_name]:
        if pd.isna(value):
            missing_count += 1

    return missing_count
df = load_file("C:/Users/LENOVO LAP/Desktop/New Microsoft Excel Worksheet.xlsx")
analyze_dataframe(df)
print(count_missing_values(df,"salery"))