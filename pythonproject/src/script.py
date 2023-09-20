"""
This script is a test case of the module lib.

It imports functions from the lib module to perform descriptive statistics
and generate a plot based on data from a CSV file.
"""

from lib import descriptive_statistics, generating_plot

data, results = descriptive_statistics("pythonproject/src/data/median-income-by-country-2023.csv")

generating_plot(
    data,
    x_variable="gdpPerCapitaPPP",
    y_variable="meanIncome",
    size="pop2023",
    title="GDP per Capita vs Avg income (size proportional Population)",
)
