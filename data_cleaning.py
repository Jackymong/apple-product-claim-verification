import pandas as pd

# Read your original CSV file
df = pd.read_csv("ARE_CustomerReviews.csv")

# Keep only rows where Product Title contains Apple
apple_df = df[
    df["Product Title"].str.contains("Apple", case=False, na=False)
]

# Save the filtered data
apple_df.to_csv("apple_reviews.csv", index=False)

print("Original rows:", len(df))
print("Apple product rows:", len(apple_df))

print(apple_df.head())
