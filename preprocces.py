import os
import pandas as pd
from googletrans import Translator

# Set the path to the data folder
data_folder = "/workspaces/visualization-energy/data"

# Initialize the translator
translator = Translator()

# Get the list of CSV files in the data folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Iterate over each CSV file
for file in csv_files:
    # Read the CSV file
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path, sep=",", engine="python")

    # Translate the column names to English
    translated_columns = [translator.translate(col).text for col in df.columns]
    df.columns = translated_columns

    # Save the translated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)
