# importing the entire pandas library, giving it a short, professional callsign: pd
import pandas as pd


df = pd.read_csv('messy_contacts.csv')

#finds the CSV file you named.
#df is the standard name for a DataFrame.
#A DataFrame IS a spreadsheet in your code. 
# It has rows, it has columns

#print(df)

df.columns = df.columns.str.strip()

#df.columns: This gives you a special list-like object of all 
# the column names: 
# [' first_name ', 'LAST NAME', ' email', 'phone number']

#.str: This is the "string accessor." 
# It's a magic gateway that tells pandas: 
# "I am about to perform a STRING OPERATION 
# on every single item in this list."

#.strip(): This is the string operation. You already know this one. 
# It chops off whitespace from the beginning and end.

#df.columns = ...: We take the newly cleaned list of column names
# and we ASSIGN IT BACK to the DataFrame, 
# overwriting the old ones.


print(df.columns)


df['first_name'] = df['first_name'].str.strip().str.capitalize()

#df['first_name']: This is how you SELECT a column.
# You use square brackets and the name of the column as a string.
# This gives you access to every cell in that one column.

#.str.strip().str.capitalize(): This is the COMBO MOVE.
# Because we are working on a pandas Series (a column),
# we can chain these str operations together.

#First, it performs .str.strip() on EVERY CELL in the column.
#Then, it takes the result of that and immediately 
# performs .str.capitalize() on EVERY CELL.

#df['first_name'] = ...: Again, we ASSIGN the new, clean column
#back to the DataFrame, overwriting the old data.

df['LAST NAME'] = df['LAST NAME'].str.strip().str.capitalize()
df['email'] = df['email'].str.strip().str.lower()


df['phone number'] = df['phone number'].str.replace(r'\D',' ',regex=True)

# It says "find anything that is NOT a digit (\D) and replace it with NOTHING."

#df['phone number'].str.replace(...): We are selecting the phone number column
# and running a "replace" operation on every cell.

#r'\D': This is the regex pattern. r'' just means "raw string," so Python 
# doesn't get confused by the backslash. \D is a special regex code that means
# "ANYTHING THAT IS NOT A DIGIT." This includes -, (, ), and spaces.

#' ': This is what we are replacing it with. NOTHING.

#regex=True: We have to explicitly tell pandas that the first argument is a regex pattern 
#and not just a normal string.

#THE RESULT: It goes through a string like (555) 234-5678 and
# annihilates every non-number, leaving only 5552345678

#print(df)

df.to_csv('clean_contacts.csv', index=False, sep=';')

#df.to_csv(): This is the save function. 
# It takes the perfect, clean DataFrame in memory and writes it to a new file.

# clean_contacts.csv': The name of the deliverable file.

# index=False: By default, pandas will add a new column at the beginning of your file 
# with the row numbers (0, 1, 2, 3...). The client does not want this.
# index=False tells pandas to not do that.