import os
import pandas as pd

csv_file = "cities.csv"

cities_data = pd.read_csv(csv_file)

cities_df = pd.DataFrame(cities_data)

cities_df.to_html('../cities_data.html', index=False)

