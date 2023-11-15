import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns


def total_ip_count(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    if "IP" in dataframe:
        ip_count = dataframe["IP"].nunique()
        return {"total": ip_count}
    else:
        print("No 'IP' column found in the CSV file.")
        return None


def ip_count(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "IP" in dataframe:
        ip_counts = dataframe["IP"].value_counts().reset_index().rename(columns={"index": "IP", "IP": "Count"})   
    
        ip_counts = ip_counts.sort_values(by="Count", ascending=False).head(10)
        
        plt.figure(figsize=(10,6))
        bars = plt.bar(ip_counts['IP'], ip_counts['Count'])
        plt.xlabel('IP')
        plt.ylabel('Count')
        plt.title('Top 10 IP counts')
        plt.xticks(fontsize=7)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, yval, ha='center', va='bottom')

        plt.show()

        return ip_counts
    else:
        print("No 'IP' column found in the CSV file.")
        return None
    

def status_count(dataframe, status_code=None):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if status_code is not None:
        if str(status_code) in dataframe["Status"].unique():
            count_df = dataframe[dataframe["Status"] == str(status_code)].reset_index(drop=True)
            count_df["status_code"] = str(status_code)
            count_df = count_df.groupby("status_code")["Status"].count().reset_index().rename(columns={"status_code": "Stute", "Status": "Count"})
            return count_df
        else:
            print("No 'Status' column found in the CSV file.")
            return None

    else:
        status_counts = dataframe["Status"].value_counts().reset_index().rename(columns={"index": "Status", "Status": "Count"})
        # Bar chart
        plt.bar(status_counts["Status"], status_counts["Count"])
        plt.xlabel('Status')
        plt.ylabel('Count')
        plt.title('Status Counts')
        plt.show()

        return status_counts


def filter_by_status(dataframe, target_status):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "Status" in dataframe:
        filtered_data = dataframe[dataframe['Status'] == target_status].reset_index(drop=True)
        return filtered_data
    else:
        print("No 'Status' column found in the CSV file.")
        return None
