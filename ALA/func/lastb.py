import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns


def failed_attp(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "User" in dataframe:
        user_count = dataframe["User"].value_counts().reset_index().rename(columns={"index": "User", "User": "Count"})
        
        patches, texts, autotexts = plt.pie(user_count['Count'], labels=user_count['User'], autopct='%1.1f%%')
        plt.legend(patches, user_count['User'], loc="best")
        
        for i in range(len(autotexts)):
            autotexts[i].set_text(f'{autotexts[i].get_text()} ({user_count["Count"].iloc[i]})')
        
        plt.show()
        
        return user_count
    else:
        print("No 'User' column found in the CSV file.")
        return None


def all_ips(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "Session" in dataframe:
        dataframe = dataframe[~dataframe['Session'].str.contains(":")]
        ip_counts = dataframe["Session"].value_counts().reset_index().rename(columns={"index": "Session", "Session": "Count"})

        patches, texts, autotexts = plt.pie(ip_counts['Count'], labels=ip_counts['Session'], autopct='%1.1f%%')
        
        plt.legend(patches, ip_counts['Session'], loc="best")
        
        for i in range(len(autotexts)):
            autotexts[i].set_text(f'{autotexts[i].get_text()} ({ip_counts["Count"].iloc[i]})')
        
        plt.show()

        return ip_counts
    else:
        print("No 'Session' column found in the CSV file.")
        return None

    
def attempt_date(dataframe, date):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "DateTime" in dataframe:
        dataframe['DateTime'] = pd.to_datetime(dataframe['DateTime'], format='%a %b %d %H:%M', errors='coerce')
        dataframe['DateTime'] = dataframe['DateTime'].dt.strftime('%m-%d')
        ip_counts = dataframe.groupby(['User', 'DateTime']).size().reset_index(name='Counts')
        ip_counts['DateTime'] = pd.to_datetime(ip_counts['DateTime'], format='%m-%d')

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=ip_counts, x='DateTime', y='Counts', hue='User', ax=ax)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        for _, row in ip_counts.iterrows():
            ax.text(row['DateTime'], row['Counts'], s=row['DateTime'].strftime('%m-%d'), color='red')
        
        plt.tight_layout()
        plt.show()

        return ip_counts

    else:
        print("No 'DateTime' column found in the CSV file.")
        return None

