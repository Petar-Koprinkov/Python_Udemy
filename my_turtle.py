from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Names', ['Petar', 'Georgi'])
table.add_column('Age', [24, 23])
table.add_column('Gender', ['Male', 'Male'])
table.align = 'l'
print(table)