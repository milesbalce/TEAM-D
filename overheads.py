# Extracting overheads data
def read_csv(data):
    # Splitting data string into individual lines
    lines = data.strip().split("\n")

    # Removing quotes ("") and splitting the first line to get headers
    header = lines[0].replace('"', '').split(",")

    # Processing each line, removing quotes, splitting by comma, and creating dictionaries
    rows = [line.replace('"', '').split(",") for line in lines[1:]]

    # Returning a list of dictionaries for each row
    return [dict(zip(header, row)) for row in rows]

# CSV data
csv_data = """
"Category","Overheads"
"Salary Expense",23.54
"Interest Expense ",1.49
"Marketing Expense",2.48
"Rental Expense",3.68
"Overflow Expense - Retail",0.1
"Overflow Expense - Warehouse",0.15
"Penalty Expense",6.69
"Depreciation Expense",4.73
"Maintenance Expense",1.8
"Shipping Expense",41.67
"Human Resource Expense",13.65
"""  

# Finding the highest overhead in the data
def find_highest_overhead(data):
    # Initializing variables to store the highest overhead category and its value
    highest_overhead_category = None
    max_overhead_value = 0

    # Going over each data input one by one
    for entry in data:
        # Extracting and converting category into uppercase
        category = entry['Category'].upper()

        # Converting the overhead value to a float
        overhead = float(entry['Overheads'])

        # Checking if the current overhead is greater than the maximum found so far
        if overhead > max_overhead_value:
            highest_overhead_category = category
            max_overhead_value = overhead

    # Returning the category with the highest overhead and its value
    return highest_overhead_category, max_overhead_value

# Reading the CSV data
read_data = read_csv(csv_data)

# Finding the category with the highest overhead
highest_overhead_category, max_overhead_value = find_highest_overhead(read_data)

# Printing the highest overhead category and its value
print(f"[HIGHEST OVERHEAD] {highest_overhead_category}: {max_overhead_value}%")
