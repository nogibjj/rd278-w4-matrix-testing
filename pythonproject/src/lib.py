"""
This module takes a CSV and returns statistics about it.
"""
import os
import matplotlib.pyplot as plt
import polars as pl

def is_int_or_float(value):
    """
    Check if a value is an integer or a float.

    Parameters:
        value: The value to check.

    Returns:
        bool: True if the value is an integer or float, False otherwise.
    """
    return isinstance(value, (int, float))

def test_float_int(vector):
    """
    Check if a Polars Series contains mostly integers or floats.

    Parameters:
        vector: A Polars Series to check.

    Returns:
        bool: True if the majority of values are integers or floats, False otherwise.
    """
    # Allowance of 90%
    threshold = 0.9

    allowance = sum(vector.apply(is_int_or_float)) / len(vector) >= threshold

    return allowance

def is_csv_file(file_path):
    """
    Check if a file has a '.csv' extension.

    Parameters:
        file_path: The path to the file.

    Returns:
        bool: True if the file has a '.csv' extension, False otherwise.
    """
    # Extract the file extension from the file path
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension == ".csv"

def is_png_file(file_path):
    """
    Check if a file has a '.png' extension.

    Parameters:
        file_path: The path to the file.

    Returns:
        bool: True if the file has a '.png' extension, False otherwise.
    """
    # Extract the file extension from the file path
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension == ".png"

def descriptive_statistics(directory_path):
    """
    Calculate descriptive statistics for a DataFrame.

    Parameters:
        directory_path (str): The path to the input CSV file.

    Returns:
        Tuple[pl.DataFrame, pl.DataFrame]: A tuple containing 
        the input Polars DataFrame and the statistics DataFrame.
    """
    if is_csv_file(directory_path):
        data = pl.read_csv(directory_path)
        results = data.describe()
        results.write_csv('results.csv')

        return data, results
    raise NotADirectoryError("This is not a valid .csv file")

def generating_plot(data, x_variable, y_variable, title, size=None):
    """
    Generate a scatter plot.

    Parameters:
        data (pl.DataFrame): The input Polars DataFrame.
        x_variable (str): The variable on the X-axis.
        y_variable (str): The variable on the Y-axis.
        title (str): The title of the plot.
        size (str, optional): A variable for marker size. Default is None.
    """
    lc_size = (size is None) or (test_float_int(data[size]))
    if (
        test_float_int(data[x_variable])
        and test_float_int(data[y_variable])
        and lc_size
    ):
        if size is None:
            area = 1
        else:
            area = data[size] * 10 / data[size].mean()

        # Labeling
        plt.scatter(data[x_variable], data[y_variable], s=area, alpha=0.5)
        plt.xlabel(x_variable)
        plt.ylabel(y_variable)
        plt.title(title)
        
        # Save the plot to a PNG file
        filename = title + ".png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        
        plt.show()
    else:
        raise ValueError(
            f"One or more of {x_variable}, {y_variable}, or {size} is not a float or int"
        )