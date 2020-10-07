"""Generate sales report showing total melons each salesperson sold."""

# Declare empty lists for salespeople and melons sold
salespeople = []
melons_sold = []

# Open the sales report file
f = open('sales-report.txt')

# Iterate over each line in file
for line in f:

    # Remove trailing whitespace
    line = line.rstrip()
    # Create a list of entries split at |
    entries = line.split('|')

    # Set sales person equal to first item in entries list
    salesperson = entries[0]
    # Set melons equal to integer of third item in entries list
    melons = int(entries[2])

    # If salesperson is found in salespeople list
    # Set position equal to the index of salesperson
    # Add melons to melons_sold list of salesperson
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    
    # Otherwise, add salesperson to salespeople list
    # And add melons to melons_sold list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# For each salesperson, print salesperson and melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
