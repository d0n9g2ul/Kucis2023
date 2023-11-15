import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cpu_usage(df, threshold=None):
    if threshold==None:
      threshold = 0.5

    return df[df['%CPU'] >= threshold]


def mem_usage(df, threshold=None):
    if threshold==None:
      threshold = 0.5

    return df[df['%MEM'] >= threshold]


def high_memory(df, n):
    return df.nlargest(n, 'VIRT')


def is_running(df):
    return df[df['S'] == 'R']


def pie_chart(df, resource_col=None , command_col='COMMAND', title=None):
    if resource_col == None:
        print("resource_col is None")
    try:
        sorted_df = df.sort_values(by=resource_col, ascending=False)

        plt.figure(figsize=(5, 5))
        plt.pie(sorted_df[resource_col], labels=sorted_df[command_col], autopct='%1.1f%%', startangle=90)
        plt.axis('equal') 

        if title:
            plt.title(title)

        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def bar_chart(df, resource_col=None, command_col='COMMAND', title=None):
    try:
        if resource_col is None:
            print("resource_col is None")

        sorted_df = df.sort_values(by=resource_col, ascending=False)

        plt.figure(figsize=(10, 6))
        plt.bar(sorted_df[command_col], sorted_df[resource_col], color='skyblue')
        plt.xlabel('Processes')
        plt.ylabel(resource_col)
        plt.title(title if title else f'Bar Chart - {resource_col}')

        plt.xticks(rotation=45, ha='right')

        plt.show()
    except Exception as e:
        print(f"Error: {e}")

