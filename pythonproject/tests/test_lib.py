import unittest
import os
import sys
import pytest

# Import your lib module correctly

#As the module src is not in the test directory I'll append it

dir=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src'))
sys.path.append(dir)
import lib


class TestScriptCode(unittest.TestCase):
    """unit test class which will test source code"""

    def test_raised_errors(self):
            sample_data,results=lib.descriptive_statistics("pythonproject/src/data/median-income-by-country-2023.csv")
            with pytest.raises(ValueError):
                 lib.generating_plot(
                    data=sample_data,
                    x_variable="country",
                    y_variable="meanIncome",
                    size="pop2023",
                    title="GDP per Capita vs Avg income (size proportional Population)",
                )
                 



if __name__ == "__main__":
    unittest.main()




