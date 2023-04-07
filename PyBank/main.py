import os
import csv

#path to csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#reads csv file
with open(budget_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skips header rows
    next(csv_reader)
    total_months = 0
    net_profit_loss = 0
    prev_profit_loss = None
    profit_changed = []
    greatest_increase = 0
    greatest_decrease = 0
    for row in csv_reader:
        total_months += 1
        net_profit_loss += int(row[1])
        current_profit_loss = int(row[1])
        profit_loss = int(row[1])
        if prev_profit_loss is not None:
            change = current_profit_loss - prev_profit_loss
            profit_changed.append(change)
        prev_profit_loss = current_profit_loss
        if len(profit_changed) > 0:
            greatest_increase = max(profit_changed)
            greatest_increase_date = row[0]
        if len(profit_changed) > 0:
            greatest_decrease = min(profit_changed)
            greatest_decrease_date = row[0]
    average = sum(profit_changed) / len(profit_changed)
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit_loss:.0f}")
    print(f"Average Change: ${average:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.0f})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.0f})")