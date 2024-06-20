# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def graph_analysis(df, plot_title, content_column='CONTENT', vertical_line_year=None):
    df['AGE'] = df['AGE'].astype(str)
    yearly_totals = df.groupby('TIME')[content_column].sum().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(yearly_totals['TIME'], yearly_totals[content_column], '-o')
    plt.title(f'Total Count by Year {plot_title}')
    plt.xlabel('Year (TIME)')
    plt.ylabel(f'Total Count ({content_column})')
    plt.grid(True)
    if vertical_line_year is not None:
        plt.axvline(x=vertical_line_year, color='red', linestyle='--', label=f'{vertical_line_year} (Separation-Year)')
        plt.legend()
    plt.show()

    young_age_range = [str(age) for age in range(0, 17)]
    senior_age_range = [str(age) for age in range(80, 106)] + ['105 and above']

    young_totals = df[df['AGE'].isin(young_age_range)].groupby('TIME')[content_column].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.plot(young_totals['TIME'], young_totals[content_column], '-o', color='blue')
    plt.title(f'Total Count by Year for Ages 0-16 {plot_title}')
    plt.xlabel('Year (TIME)')
    plt.ylabel(f'Total Count ({content_column})')
    plt.grid(True)
    if vertical_line_year is not None:
        plt.axvline(x=vertical_line_year, color='red', linestyle='--', label=f'{vertical_line_year} (Separation-Year)')
        plt.legend()
    plt.show()

    senior_totals = df[df['AGE'].isin(senior_age_range)].groupby('TIME')[content_column].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.plot(senior_totals['TIME'], senior_totals[content_column], '-o', color='green')
    plt.title(f'Total Count by Year for Ages 80-106 {plot_title}')
    plt.xlabel('Year (TIME)')
    plt.ylabel(f'Total Count ({content_column})')
    plt.grid(True)
    if vertical_line_year is not None:
        plt.axvline(x=vertical_line_year, color='red', linestyle='--', label=f'{vertical_line_year} (Separation-Year)')
        plt.legend()
    plt.show()
