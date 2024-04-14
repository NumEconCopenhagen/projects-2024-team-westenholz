# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def graph_analysis(df, plot_title, indhold_column='INDHOLD'):
    df['ALDER'] = df['ALDER'].astype(str)
    yearly_totals = df.groupby('TID')[indhold_column].sum().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(yearly_totals['TID'], yearly_totals[indhold_column], '-o')
    plt.title(f'Total Count by Year ({plot_title})')
    plt.xlabel('Year (TID)')
    plt.ylabel(f'Total Count ({indhold_column})')
    plt.grid(True)
    plt.show()

    young_age_range = [str(age) for age in range(0, 17)]
    senior_age_range = [str(age) for age in range(80, 106)] + ['105 and above']

    young_totals = df[df['ALDER'].isin(young_age_range)].groupby('TID')[indhold_column].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.plot(young_totals['TID'], young_totals[indhold_column], '-o', color='blue')
    plt.title(f'Total Count by Year for Ages 0-16 ({plot_title})')
    plt.xlabel('Year (TID)')
    plt.ylabel(f'Total Count ({indhold_column})')
    plt.grid(True)
    plt.show()

    senior_totals = df[df['ALDER'].isin(senior_age_range)].groupby('TID')[indhold_column].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.plot(senior_totals['TID'], senior_totals[indhold_column], '-o', color='green')
