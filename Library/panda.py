import pandas as pd

# Membuat DataFrame Dari Dictionary

data = {
    'Nama'          :['Muhamad','Nabil','Firdaus'],
    'Usia'          :[20,21,22],
    'Perkerjaan'    :['Data Scientist','Data Analyst','Machine Learning']
}

df = pd.DataFrame(data)

print(df)