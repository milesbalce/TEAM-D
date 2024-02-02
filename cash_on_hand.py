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
    final_output = "\n".join(all_deficits_output + [""] + top_deficits_output)
    
    return final_output

# Analyzing the cash trends
cash_analysis = analyze_cash_trends(daily_differences)

# Output the analysis
print(cash_analysis)