import pandas as pd


def by_date(dataframe, start_date, end_date=None):
    if dataframe is None:
        print("Dataframe is not provided.")
        return None

    if "Date" not in dataframe.columns or "Time" not in dataframe.columns:
        print("No 'Date' or 'Time' column found in the dataframe.")
        return None

    datetime_column = pd.to_datetime(dataframe['Date'] + ' ' + dataframe['Time'], format='%b %d %H:%M:%S')

    start_date = pd.to_datetime(start_date, format='%b %d').date()
    if end_date is not None:
        end_date = pd.to_datetime(end_date, format='%b %d').date()

    if end_date is not None:
        end_date += pd.Timedelta(days=1)
        dataframe = dataframe[(datetime_column.dt.date >= start_date) & (datetime_column.dt.date < end_date)]
    else:
        dataframe = dataframe[datetime_column.dt.date == start_date]

    return dataframe


def by_time(dataframe, start_time, end_time=None):
    if dataframe is None:
        print("Dataframe is not provided.")
        return None

    if "Time" not in dataframe.columns:
        print("No 'Time' column found in the dataframe.")
        return None

    dataframe['Time'] = pd.to_datetime(dataframe['Time'], format='%H:%M:%S').dt.time

    start_time = pd.to_datetime(start_time, format='%H:%M').time()
    if end_time is not None:
        end_time = pd.to_datetime(end_time, format='%H:%M').time()

    if end_time is not None:
        dataframe = dataframe[(dataframe['Time'] >= start_time) & (dataframe['Time'] <= end_time)]
    else:
        dataframe = dataframe[dataframe['Time'] >= start_time]

    return dataframe


def by_message(dataframe, keyword):
    if dataframe is None:
        print("Dataframe is not provided.")
        return None

    if "Message" not in dataframe.columns:
        print("No 'Message' column found in the dataframe.")
        return None

    filtered_dataframe = dataframe[dataframe['Message'].str.contains(keyword, case=False)]

    return filtered_dataframe


def by_process(dataframe, keyword):
    if dataframe is None:
        print("Dataframe is not provided.")
        return None

    if "Process" not in dataframe.columns:
        print("No 'Process' column found in the dataframe.")
        return None

    filtered_dataframe = dataframe[dataframe['Process'].str.contains(keyword, case=False)]

    return filtered_dataframe