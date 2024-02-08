import os
import csv
buget_data = os.path.join(r"C:/Users/eddie/Desktop/python-challenge/python-challenge/PyBank/Resource/budget_data.csv")
with open('budget_data', newline="") as csvfile:
    csvreader = next(csvfile)
    print(f"Header: {csv_header}")
