import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns


def connect_user(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "User" in dataframe:
        connect_user = dataframe["User"].value_counts().reset_index().rename(columns={"index": "User", "User": "Count"})
        patches, texts, autotexts = plt.pie(connect_user['Count'], labels=connect_user['User'], autopct='%1.1f%%')
        
        plt.legend(patches, connect_user['User'], loc="best")
        
        for i in range(len(autotexts)):
            autotexts[i].set_text(f'{autotexts[i].get_text()} ({connect_user["Count"].iloc[i]})')
        
        plt.show()
        
        return connect_user
    
    else:
        print("No 'User' column found in the CSV file.")
        return None

    
def connect_time(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "DateTime" in dataframe and "User" in dataframe:
        dataframe['DateTime'] = pd.to_datetime(dataframe['DateTime'], format='%a %b %d %H:%M', errors='coerce')
        dataframe['DateTime'] = dataframe['DateTime'].dt.strftime('%m-%d')
        user_counts = dataframe.groupby(['User', 'DateTime']).size().reset_index(name='Counts')
        user_counts['DateTime'] = pd.to_datetime(user_counts['DateTime'], format='%m-%d')

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=user_counts, x='DateTime', y='Counts', hue='User', ax=ax)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        for _, row in user_counts.iterrows():
            ax.text(row['DateTime'], row['Counts'], s=row['DateTime'].strftime('%m-%d'), color='red')
        
        plt.tight_layout()
        plt.show()

        return user_counts

    else:
        print("No 'DateTime' or 'User' column found in the CSV file.")
        return None