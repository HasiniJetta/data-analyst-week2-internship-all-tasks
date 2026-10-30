import pandas as pd

df = pd.read_excel("SQL_Sales_Dataset_200_Rows.xlsx")

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)



# Question 2: Handle missing values and duplicates

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())



# Question 3: Group data by category and find total revenue

print("\nTotal revenue by category:")

category_revenue = df.groupby("category")["total_price"].sum()

print(category_revenue)



# Question 4: Sort data by multiple columns

print("\nData sorted by region and total price:")

sorted_data = df.sort_values(
    by=["region", "total_price"],
    ascending=[True, False]
)

print(sorted_data.head(10))



# Question 5: Create a correlation matrix

print("\nCorrelation matrix:")

correlation_matrix = df[["quantity", "unit_price", "total_price"]].corr()

print(correlation_matrix)