"""Generate sales report showing total melons each salesperson sold."""

filename = 'sales-report.txt'

def make_dictionary(filename):
    '''Creates sales report dictionary from text file'''

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
        # Set order total equal to float of second item in entries list
        order_total = float(entries[1])

        # If salesperson is found in sales dictionary
        # Add melon count and order total to existing totals
        if salesperson in sales_dictionary.keys():
            sales_dictionary[salesperson]['melons sold'] = melons 
            sales_dictionary[salesperson]['order total'] = order_total
                    
        # Otherwise, add new salesperson to sales dictionary
        else:
            sales_dictionary[salesperson] = {'melons sold': melons, 'order total': order_total}
            
    return sales_dictionary
            

def print_sales_report(filename):
    '''Print sales report from text file'''

    sales_dictionary = make_dictionary(filename)

    for salesperson in sales_dictionary.keys():
        # Capture salesperson information
        sales_values = sales_dictionary[salesperson]
        melons_sold = sales_values['melons sold']
        order_total = sales_values['order total']

        print(f'{salesperson} sold {melons_sold} melons for an order total of {order_total}')


print_sales_report(filename)