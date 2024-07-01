import seaborn as sns
from pandasql import sqldf
penguins = sns.load_dataset('penguins')
penguins.head()

# sqldf function from the pandasql library to  <br>
# execute a SQL query on a pandas DataFrame called "penguins".

data = sqldf('''SELECT species, island FROM penguins LIMIT 5''')
for i in data:
    print(i)


# The type() function is then used to determine the data type of the output of the sqldf function. <br>
# • The output is a pandas DataFrame, so the type() function will return .

type(sqldf('''SELECT species, island FROM penguins LIMIT 5'''))

# Display unique rows in pandas and sqlite

penguins['species'].unique()

sqldf('''SELECT Distinct species, island  FROM penguins ''')

# sorting the data

sqldf('''SELECT body_mass_g  FROM penguins  ORDER BY body_mass_g DESC LIMIT 5''')

penguins['body_mass_g'].sort_values(ascending=False, 
ignore_index=True).head()


# filtering data
sqldf('''SELECT DISTINCT species FROM penguins WHERE sex = 'Male'  AND flipper_length_mm > 210''')

penguins[(penguins['sex'] == 'Male') & (penguins['flipper_length_mm'] >210)]['species'].unique()

# Grouping and aggregating data 
sqldf('''SELECT species, MAX(bill_length_mm) FROM penguins GROUP BY species''')

penguins[['species','bill_length_mm']].groupby('species',as_index=False).max()


# mathematical operations with pandasql

sqldf('''SELECT bill_length_mm / bill_depth_mm AS length_to_depth FROM penguins ORDER BY length_to_depth  DESC LIMIT 5''')


penguins['ength_to_depth']=penguins['bill_length_mm'] / penguins['bill_depth_mm']
penguins['ength_to_depth'].sort_values(ascending=False , ignore_index=True).head()

