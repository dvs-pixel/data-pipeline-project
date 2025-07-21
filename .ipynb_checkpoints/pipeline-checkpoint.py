import pandas as pd

# Step 1: Load data (we'll use a sample dictionary for now)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'Age': [25, 30, None, 22, 29],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Kolkata', None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Clean the data (drop rows with missing values)
cleaned_df = df.dropna()

print("\nCleaned Data:")
print(cleaned_df)

# Step 3: Save the cleaned data to a CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)

print("\nCleaned data saved to 'cleaned_data.csv'")

