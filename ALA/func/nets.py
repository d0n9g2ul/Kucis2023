import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns


def all_PID(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "PIDProgramName" in dataframe:
        all_pid = dataframe["PIDProgramName"].apply(lambda x: x.split(':')[0] if ':' in x else x)
        return all_pid
    else:
        print("No 'PIDProgramName' column found in the CSV file.")
        return None


def local_ips(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "LocalAddress" in dataframe:
        localips = dataframe["LocalAddress"].value_counts()
        return localips
    else:
        print("No 'LocalAddress' column found in the CSV file.")
        return None


def foreign_ips(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return None

    if "ForeignAddress" in dataframe:
        forips = dataframe["ForeignAddress"].value_counts()
        return forips
    
    else:
        print("No 'ForeignAddress' column found in the CSV file.")
        return None


def state_count(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "State" in dataframe:
        state_count_df = dataframe['State'].value_counts().reset_index().rename(columns={"index": "State", "State": "Count"})
        patches, texts, autotexts = plt.pie(state_count_df['Count'], labels=state_count_df['State'], autopct='%1.1f%%')
        
        plt.legend(patches, state_count_df['State'], loc="best")
        
        for i in range(len(autotexts)):
            autotexts[i].set_text(f'{autotexts[i].get_text()} ({state_count_df["Count"].iloc[i]})')
        
        plt.show()
        return state_count_df

    else:
        print("No 'State' column found in the CSV file.")
        return None


def established_ports(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "State" in dataframe and "LocalAddress" in dataframe and "ForeignAddress" in dataframe:
        established_data = dataframe[dataframe['State'] == "ESTABLISHED"].copy()
        established_data.loc[:, 'LocalAddress'] = established_data['LocalAddress'].apply(lambda x: x.split(':')[1] if ':' in x else x)
        established_data.loc[:, 'ForeignAddress'] = established_data['ForeignAddress'].apply(lambda x: x.split(':')[1] if ':' in x else x)
        return established_data[['LocalAddress', 'ForeignAddress']]
    else:
        print("No 'State', 'LocalAddress', 'ForeignAddress' column found in the CSV file.")
        return None


def established_PID(dataframe):
    if dataframe is None:
        print("CSV file not loaded. Please use 'read_csv' method to load the CSV file.")
        return
    
    if "State" in dataframe and "PIDProgramName" in dataframe:
        established_data = dataframe[dataframe['State'] == "ESTABLISHED"].copy()
        established_data.loc[:, 'PIDProgramName'] = established_data['PIDProgramName'].apply(lambda x: x.split('/')[0] if '/' in x else x)
        return established_data['PIDProgramName']
    else:
        print("No 'State', 'PIDProgramName' column found in the CSV file.")
        return None

