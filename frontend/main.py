from taipy.gui import Gui 
import taipy.gui.builder as tgb
from math import cos, exp
import pandas as pd
import taipy as tp
data = {
    'Rank': [1, 2, 3, 4, 5],
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'],
    'Gold': [46, 27, 26, 19, 19],
    'Silver': [37, 25, 19, 13, 16],
    'Bronze': [38, 40, 25, 15, 17],
    'Total': [121, 92, 70, 47, 52]
}

page = """
# Table

<|{data}|table|>
"""

if __name__ == "__main__":
    Gui(page).run(title="Dynamic chart")