import pandas as pd
import csv
from datetime import datetime

class CSV:
  CSV_FILE ="finance_data.csv" # CSV file name
  COLUMNS = ["date", "description", "amount", "category"]

  @classmethod
  def initialize_csv(cls):
    try:
      pd.read_csv(cls.CSV_FILE)
    except FileNotFoundError:
      df = pd.DataFrame(columns=cls.COLUMNS)
      df.to_csv(cls.CSV_FILE, index=False)

  @classmethod           
  def add_entry(cls, date, description, amount, category): # Add a new entry
    new_entry = {
      "date": date,
      "description": description,
      "amount": amount,
      "category": category
    }
    with open(cls.CSV_FILE, mode='a', newline='') as file: # Append mode
      writer = csv.DictWriter(file, fieldnames=cls.COLUMNS) # Create a writer
      writer.writerow(new_entry)
      print("Entry added successfully.")

CSV.initialize_csv()
CSV.add_entry("01-02-2026", "Grocery Shopping", 150 , "Food")