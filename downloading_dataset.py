import pandas as pd
url = "https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv"

df = pd.read_csv(url)                 # read directly from the URL
df.to_csv("datasets/manhattan.csv", index=False)  # save locally
