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
    for i in range(1, len(data)):
        # Calculate the change in net profit from the previous day
        current_profit = int(data[i]["Net Profit (Accumulated) (SGD)"])
        previous_profit = int(data[i - 1]["Net Profit (Accumulated) (SGD)"])
        change = current_profit - previous_profit
        # Append the day and the change to the list
        changes.append((int(data[i]["Day"]), change))
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
    # Check if the net profit is always increasing or decreasing
    increasing = all(change >= 0 for _, change in changes)
    decreasing = all(change <= 0 for _, change in changes)

    # If always increasing, find and return the highest increase
    if increasing:
        highest_increase = max(changes, key=lambda x: x[1])
        return f"Highest Increase: Day {highest_increase[0]}, Amount {highest_increase[1]}"
    # If always decreasing, find and return the highest decrease
    elif decreasing:
        highest_decrease = min(changes, key=lambda x: x[1])
        return f"Highest Decrease: Day {highest_decrease[0]}, Amount {abs(highest_decrease[1])}"
    # Otherwise, calculate and return all deficits and the top 3 deficits
    else:
        deficits = [d for d in changes if d[1] < 0]
        sorted_deficits = sorted(deficits, key=lambda x: x[1])
        all_deficits_str = '\n'.join(f"[NET PROFIT DEFICIT] Day: {d[0]}, Amount: SGD {abs(d[1])}" for d in deficits)
        top_deficits_str = "\n".join([
            f"[HIGHEST NET PROFIT DEFICIT] Day {sorted_deficits[0][0]}, Amount: SGD {abs(sorted_deficits[0][1])}",
            f"[2ND HIGHEST NET PROFIT DEFICIT] Day {sorted_deficits[1][0]}, Amount: SGD {abs(sorted_deficits[1][1])}",
            f"[3RD HIGHEST NET PROFIT DEFICIT] Day {sorted_deficits[2][0]}, Amount: SGD {abs(sorted_deficits[2][1])}"
        ])
        return f"{all_deficits_str}\n{top_deficits_str}"

# Reading and analyzing the data
read_data = read_csv(csv_data)
daily_profit_changes = compute_profit_changes(read_data)
profit_analysis = analyze_profit_trends(daily_profit_changes)

# Output the analysis
print(profit_analysis)

