import pandas as pd
from datetime import date

today = date.today()

# Paste your notepad file path here
File_Path = 'C:/Users/Acer/python/data-savings2.txt'

# Pandas header
cols = ['MyRecord']
df = pd.read_fwf(File_Path, names=cols)

# Extract only the expenses
df['Expenses'] = df['MyRecord'].str.split().str[-1]

# Remove row of date
symbol = '/'
mask = df['Expenses'].str.contains(symbol)
df = df[~mask]

# Convert string to float
df['Expenses'] = df['Expenses'].astype(float)

# Sum and display
total_sum = df['Expenses'].sum()
print(df)
print("\nYour total expsnes is:  ", total_sum, "\n")

# save the output
try:
	file = open("MySavings.txt", "x")
except:
	file = open("MySavings.txt", "a")
	file.write(str(today) + ": Your total expenses = " + str(total_sum) + "\n")
	file.close()

print("Done")