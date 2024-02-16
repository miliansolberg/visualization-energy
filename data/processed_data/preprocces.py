import os
import pandas as pd
# from googletrans import Translator

# Set the path to the data folder
data_folder = "/workspaces/visualization-energy/data"

# Initialize the translator
#translator = Translator()

# Get the list of CSV files in the data folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Iterate over each CSV file
for ind, file in enumerate(csv_files):
    # Read the CSV file
    file_path = os.path.join(data_folder, file)
    iterator = pd.read_csv(
        file_path,
        sep=",",
        engine="python",
        encoding="utf-8",
        on_bad_lines="skip",
        chunksize=100_000,
    )
    i = 0
    while True:
        try:
            chunk = next(iterator)
            chunk.to_parquet(
                os.path.join(data_folder, "processed_data", f"datacenter_{ind}_{i}_.parquet"),
                index=False,
                #encoding="utf-8",
            )
        except Exception as e:
            print(f"Error reading file {file} {i}: {e} ")
            i += 1
            break
        i += 1

            
    # for i, chunk in enumerate():
    #     print
    #     try:
    #         # Translate the column names to English
    #         # ranslated_columns = [translator.translate(col).text for col in df.columns]
    #         # df.columns = translated_columns
    #         # save the file basename in the processed_data folder
           
    #     except Exception as e:
    #         print(f"Error processing file {file} and chunk {i}: {e}")
