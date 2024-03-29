# Team members' information
team_members = """
##### Store your, name, email, student_id and class_number as STRINGS #####
name = 'Balce Miles Santos'
np_email = 's10255611@connect.np.edu.sg'
student_id = 'S10255611B'
class_number = 'TF03'

name = "Chua Meng Sven"
np_email = 's10256106@connect.np.edu.sg'
student_id = 'S10256106H'
class_number = 'TF03'

name = 'Amber Chong Rei En'
np_email = 'S10258314@connect.np.edu.sg'
student_id = 'S10258314C'
class_number = 'TF03'
"""

# Write to a text file
with open('team_members.txt', 'w') as file:
    file.write(team_members)

print("Team members' information have been written to team_members.txt")


#### OVERHEADS ####
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


#### CASH ON HAND ####
def read_csv(data):
    # Split the input string into lines
    lines = data.strip().split("\n")
    # Remove quotes and split the first line to get headers
    header = lines[0].replace('"', '').split(",")
    # Process each line, remove quotes, split by comma, and create a dictionary zipping with header
    rows = [line.replace('"', '').split(",") for line in lines[1:]]
    return [dict(zip(header, row)) for row in rows]

def compute_differences(data):
    # Initialize a list to store the differences in 'Cash On Hand' between days
    differences = []

    for amount in range(1, len(data)):
        # Calculate the difference between the current day and the previous day
        current_day = int(data[amount]["Cash On Hand"])
        previous_day = int(data[amount - 1]["Cash On Hand"])
        difference = current_day - previous_day
        # To the list, add the day and the difference.
        differences.append((int(data[amount]["Day"]), difference))
    return differences

# CSV data
csv_data = """
"Day","Cash On Hand"
11,339121
12,164206
13,93496
14,486615
15,336164
16,157457
17,194010
18,77283
19,122983
20,145737
21,437214
22,554977
23,359293
24,310569
25,410244
26,337566
27,168225
28,477403
29,581529
30,423452
31,228955
32,499162
33,267284
34,450184
35,326102
36,164954
37,134179
38,381328
39,652194
40,153784
41,285816
42,463012
43,322608
44,381554
45,237785
46,586413
47,607941
48,220172
49,103426
50,220900
51,607943
52,736790
53,129063
54,640503
55,73079
56,126317
57,86338
58,152205
59,226467
60,186026
61,55320
62,568679
63,293548
64,287827
65,49955
66,83064
67,632881
68,85196
69,35687
70,906263
71,2414336
72,2127701
73,2507649
74,2518192
75,2618469
76,2051860
77,1590978
78,2179160
79,2718204
80,2371865
81,2414224
82,3544066
83,2936357
84,3356383
85,4150821
86,4114822
87,3862679
88,4376652
89,4622945
90,5031869
"""  

# Read CSV and calculate differences
read_data = read_csv(csv_data)
daily_differences = compute_differences(read_data)

def analyze_cash_trends(changes):
    # Initialize a list to store all deficits
    all_deficits = []
    
    # Iterate through changes to find all deficits
    for day, change in changes:
        if change < 0:
            all_deficits.append((day, change))
    
    # Sort the deficits based on the deficit amount without using lambda
    sorted_deficits = sorted(all_deficits, key=lambda x: x[1])
    
    # Prepare the output for all deficits
    all_deficits_output = []
    for deficit in all_deficits:
        all_deficits_output.append(f"[CASH DEFICIT] Day: {deficit[0]}, Amount: SGD {abs(deficit[1])}")
    
    # Identify the top 3 highest deficits
    top_deficits = sorted_deficits[:3]  # Assuming deficits are sorted in ascending order
    
    # Prepare the output for top 3 deficits
    top_deficits_output = []
    ranks = ["HIGHEST", "2ND HIGHEST", "3RD HIGHEST"]
    for amount, deficit in enumerate(top_deficits):
        top_deficits_output.append(f"[{ranks[amount]} CASH DEFICIT] Day {deficit[0]}, Amount: SGD {abs(deficit[1])}")
    
    # Combine all outputs
    final_output = final_output = '\n'.join(all_deficits_output) + '\n' + '\n'.join(top_deficits_output)
    
    return final_output

# Analyzing the cash trends
cash_analysis = analyze_cash_trends(daily_differences)

# Output the analysis
print(cash_analysis)


#### PROFIT AND LOSS ####
def read_csv(data):
    # Split the data into lines
    lines = data.strip().split("\n")
    # Remove quotes and split the first line to get the headers
    header = lines[0].replace('"', '').split(",")
    # Process each subsequent line, remove quotes, split by comma, and create a dictionary
    rows = [line.replace('"', '').split(",") for line in lines[1:]]
    # Zip each row with the header to create a dictionary for each line
    return [dict(zip(header, row)) for row in rows]

def compute_profit_changes(data):
    # Initialize a list to store the changes in net profit
    changes = []
    for amount in range(1, len(data)):
        # Calculate the change in net profit from the previous day
        current_profit = int(data[amount]["Net Profit (Accumulated) (SGD)"])
        previous_profit = int(data[amount - 1]["Net Profit (Accumulated) (SGD)"])
        change = current_profit - previous_profit

        # Append the day and the change to the list
        changes.append((int(data[amount]["Day"]), change))
    return changes

csv_data = """
"Day","Net Profit (Accumulated) (SGD)"
11,-2180265
12,-2134375
13,-2734954
14,-1352894
15,-1432516
16,-1901516
17,-1901418
18,-1892151
19,-1885905
20,-2579466
21,-1704757
22,-1208485
23,-1208192
24,-673520
25,-685854
26,-1364260
27,-886156
28,61139
29,26384
30,63790
31,-672518
32,479695
33,691723
34,723716
35,1028409
36,1016979
37,276851
38,314707
39,471823
40,329262
41,375732
42,-294805
43,-347172
44,-18774
45,868531
46,-44560
47,-54211
48,529040
49,1212904
50,1275776
51,1088120
52,1267908
53,1757184
54,1912520
55,1877464
56,1876901
57,2386625
58,2390323
59,1849627
60,824201
61,1210781
62,826205
63,853941
64,1428803
65,1401957
66,1396802
67,1010264
68,1091462
69,794680
70,1511562
71,2561935
72,2605597
73,3021729
74,3107885
75,3130537
76,2826022
77,2842711
78,3011179
79,2629713
80,2637973
81,2636468
82,3974012
83,3790436
84,3571619
85,4217933
86,4195893
87,3145917
88,3505073
89,3739639
90,4127261
"""  

def analyze_profit_trends(changes):
    # Initialize a list to store all deficits
    all_deficits = []
    
    # Iterate through changes to find all deficits
    for day, change in changes:
        if change < 0:
            all_deficits.append((day, change))
    
    # Sort the deficits based on the deficit amount without using lambda
    sorted_deficits = sorted(all_deficits, key=lambda x: x[1])
    
    # Prepare the output for all deficits
    all_deficits_output = []
    for deficit in all_deficits:
        all_deficits_output.append(f"[NET PROFIT DEFICIT] Day: {deficit[0]}, Amount: SGD {abs(deficit[1])}")
    
    # Identify the top 3 highest deficits
    top_deficits = sorted_deficits[:3]  # Assuming deficits are sorted in ascending order
    
    # Prepare the output for top 3 deficits
    top_deficits_output = []
    ranks = ["HIGHEST", "2ND HIGHEST", "3RD HIGHEST"]
    for amount, deficit in enumerate(top_deficits):
        top_deficits_output.append(f"[{ranks[amount]} NET PROFIT DEFICIT] Day {deficit[0]}, Amount: SGD {abs(deficit[1])}")
    
    # Combine all outputs
    final_output = '\n'.join(all_deficits_output) + '\n' + '\n'.join(top_deficits_output)
    
    return final_output

# Reading and analyzing the data
read_data = read_csv(csv_data)
daily_profit_changes = compute_profit_changes(read_data)
profit_analysis = analyze_profit_trends(daily_profit_changes)

# Output the analysis
print(profit_analysis)
# Forming the result string
result_str = f"[HIGHEST OVERHEAD] {highest_overhead_category}: {max_overhead_value}%\n{cash_analysis}\n{profit_analysis}"
# Writing the result to a text file named 'summary_report.txt'
with open('summary_report.txt', 'w') as file:
    file.write(result_str)

