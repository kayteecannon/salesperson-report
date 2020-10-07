"""Generate sales report showing total melons each salesperson sold."""

# Declare empty lists for salespeople and melons sold
# TODO: Create a salespeople dictionary, include total order amount and melons sold


# Open the sales report file
# TODO: Create function to read files

filename = 'sales-report.txt'


# Iterate over each line in file
# TODO: Create function to make dictionary

def make_dictionary(filename):

    sales_dictionary = {}

    filename = open(filename)
    
    for line in filename:

        # Remove trailing whitespace
        line = line.rstrip()
        # Create a list of entries split at |
        entries = line.split('|')

        # Set sales person equal to first item in entries list
        salesperson = entries[0]
        # Set melons equal to integer of third item in entries list
        melons = int(entries[2])
        order_total = float(entries[1])

        # If salesperson is found in salespeople list
        # Set position equal to the index of salesperson
        # Add melons to melons_sold list of salesperson
        if salesperson in sales_dictionary.keys():
            sales_dictionary[salesperson]['melons sold'] = melons 
            sales_dictionary[salesperson]['order total'] = order_total
                    
        # Otherwise, add salesperson to salespeople list
        # And add melons to melons_sold list
        else:
            sales_dictionary[salesperson] = {'melons sold': melons, 'order total': order_total}
            
    return sales_dictionary
            



# For each salesperson, print salesperson and melons sold
# TODO: Create function to print sales report

def print_sales_report(filename):

    sales_dictionary = make_dictionary(filename)

    for salesperson in sales_dictionary.keys():
        sales_values = sales_dictionary[salesperson]
        melons_sold = sales_values['melons sold']
        order_total = sales_values['order total']
        print(f'{salesperson} sold {melons_sold} melons for an order total of {order_total}')

print_sales_report(filename)