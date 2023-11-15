import pandas as pd


def total_date_count(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    if "Date" in dataframe:
        date_count = dataframe["Date"].nunique()
        
        dataframe['Date'] = pd.to_datetime(dataframe['Date'])

        first_date = dataframe['Date'].min()
        last_date = dataframe['Date'].max()
        
        return {"total_date": date_count, "first_date": first_date, "last_date": last_date}
    else:
        print("No 'Date' column found in the CSV file.")
        return None


def file_count(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "FilePath" in dataframe:
        file_counts = dataframe["FilePath"].value_counts().sum()
        return file_counts
    else:
        print("No 'FilePath' column found in the CSV file.")
        return None


def filter_by_date(dataframe, date):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "Date" in dataframe and "FilePath" in dataframe and "Time" in dataframe:
        filtered_data = dataframe[dataframe["Date"] == date][["Time", "FilePath"]]
        return filtered_data.to_string(index=False)
    
    else:
        print("No 'Date', 'FilePath', 'Time' column found in the CSV file.")
        return None
