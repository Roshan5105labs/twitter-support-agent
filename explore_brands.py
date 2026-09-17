import pandas as pd

# Load only the columns we need, to keep it fast on a 3M-row file
df = pd.read_csv(
    "data/raw/twcs.csv",
    usecols=["author_id", "inbound"],
)

# Brand accounts are the ones sending NON-inbound tweets (brand -> customer)
brands = df[df["inbound"] == False][ "author_id"].value_counts()

print("Top 20 brands by outbound tweet volume:\n")
print(brands.head(20))
