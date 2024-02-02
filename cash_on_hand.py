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

def analyze_cash_trends(differences):
    # Check if the cash on hand is always increasing or decreasing
    increasing = all(diff >= 0 for _, diff in differences)
    decreasing = all(diff <= 0 for _, diff in differences)

    # If always increasing, find the highest increase
    if increasing:
        highest_increase = max(differences, key=lambda x: x[1])
        return f"Highest Increase: Day {highest_increase[0]}, Amount {highest_increase[1]}"
    # If always decreasing, find the highest decrease
    elif decreasing:
        highest_decrease = min(differences, key=lambda x: x[1])
        return f"Highest Decrease: Day {highest_decrease[0]}, Amount {abs(highest_decrease[1])}"
    # If fluctuating, list all deficit days and the top 3 highest deficits
    else:
        deficits = [d for d in differences if d[1] < 0]
        sorted_deficits = sorted(deficits, key=lambda x: x[1])
        all_deficits_str = '\n'.join(f"[CASH DEFICIT] Day: {d[0]}, Amount: SGD {abs(d[1])}" for d in deficits)
        top_deficits_str = "\n".join([
            f"[HIGHEST CASH DEFICIT] Day {sorted_deficits[0][0]}, Amount: SGD {abs(sorted_deficits[0][1])}",
            f"[2ND HIGHEST CASH DEFICIT] Day {sorted_deficits[1][0]}, Amount: SGD {abs(sorted_deficits[1][1])}",
            f"[3RD HIGHEST CASH DEFICIT] Day {sorted_deficits[2][0]}, Amount: SGD {abs(sorted_deficits[2][1])}"
        ])
        return f"{all_deficits_str}\n{top_deficits_str}"

# Analyzing the cash trends
cash_analysis = analyze_cash_trends(daily_differences)

# Output the analysis
print(cash_analysis)