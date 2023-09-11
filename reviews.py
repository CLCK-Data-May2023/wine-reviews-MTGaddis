import pandas as pd

data = pd.read_csv("data/winemag-data-130k-v2.csv.zip", compression="zip")

summary_data = data.groupby("country").agg({"points": ["count", "mean"]}).reset_index()

summary_data.columns = ["country", "count", "points"]

summary_data["points"] = summary_data["points"].round(1)

summary_data.to_csv("data/reviews-per-country.csv", index=False)

print("Summary data has been written to 'reviews-per-country.csv'")