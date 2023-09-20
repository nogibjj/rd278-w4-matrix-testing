import unittest
import os
import polars
import sys

# Import your lib module correctly

#As the module src is not in the test directory I'll append it

dir=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src'))
sys.path.append(dir)
import lib


class TestScriptCode(unittest.TestCase):
    """unit test class which will test source code"""

    sample_data,results=lib.descriptive_statistics("pythonproject/src/data/median-income-by-country-2023.csv")

    def test_csv_validity(self,data=sample_data):

        valid_csv_path = "pythonproject/src/data/results.csv"  # Replace with the path to a valid CSV file
        invalid_csv_path = "pythonproject/src/data/results.docx"  # Replace with the path to an invalid CSV file

        self.assertTrue(lib.is_csv_file(valid_csv_path), "Valid CSV file check failed.")
        self.assertFalse(lib.is_csv_file(invalid_csv_path), "Invalid CSV file check failed.")

    def test_png_validy(self,data=sample_data):
        plot_title="GDP per Capita vs Avg income (size proportional Population)"
        lib.generating_plot(data,x_variable="gdpPerCapitaPPP",
                    y_variable="meanIncome",
                    size="pop2023",
                    title=plot_title)
        
        valid_csv_path = "pythonproject/src/data/"+ plot_title + ".png"  # Replace with the path to a valid CSV file
        invalid_csv_path = "pythonproject/src/data/"+ plot_title  # Replace with the path to an invalid CSV file

        self.assertTrue(lib.is_png_file(valid_csv_path), "Valid PNG file check failed.")
        self.assertFalse(lib.is_png_file(invalid_csv_path), "Invalid PNG file check failed.")



if __name__ == "__main__":
    unittest.main()




