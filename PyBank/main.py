import os
csv_path = os.path.join("PyBank","Ressources","budget_data.csv")

total_months = 0
net_total = 0
max_profit = 0
max_profit_month = ""
min_profit = 0
min_profit_month = ""

with open(csv_path, "r") as file:

    file.readline()
    for line in file:
        total_months += 1
        line_info = line.strip().split(",")
        net_total += int(line_info[1])
        
        if max_profit < int(line_info[1]):
            max_profit = int(line_info[1])
            max_profit_month = str(line_info[0])

        if min_profit > int(line_info[1]):
            min_profit = int(line_info[1])
            min_profit_month = str(line_info[0])

average_change = round(float(net_total/total_months), 2)

print(
    f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {max_profit_month} (${max_profit})
Greatest Decrease in Profits: {min_profit_month} (${min_profit})
    """
)