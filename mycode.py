import pandas as pd 
import os
data = {
    "name":["Sujit", "Isha", "Nisha"],
    "age" : [15,120,25], 
    }

df = pd.DataFrame(data)

data_dir = "data"

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path,index=False)

print(f"CSV saved to filepath {file_path}")