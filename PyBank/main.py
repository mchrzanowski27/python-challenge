import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
output_file = os.path.join("PyBank", "Analysis", "financial-analysis.txt")

# lists
months = []
profit_loss = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    total_months = (len(months))

    total_profits = sum(profit_loss)

    average_change = (profit_loss[85] - profit_loss[0])/(total_months-1)

    profit_change = []
    for i in range (1, len(profit_loss)):
        profit_change.append(profit_loss[i]-profit_loss[i-1])
        greatest_increase = max(profit_change)
        greatest_decrease = min(profit_change)

    greatest_increase_index = profit_change.index(greatest_increase)
    greatest_decrease_index = profit_change.index(greatest_decrease)

    months_greatest_increase = months[greatest_increase_index +1]
    months_greatest_decrease = months[greatest_decrease_index +1]

Result_summary = ["Financial Analysis\n",
                "---------------------------\n"
                f"Total Months: {(total_months)}\n",
                f"Total: ${total_profits}\n",
                f"Average Change: ${average_change:.2f}\n",
                f"Greatest Increase in Profits: {months_greatest_increase} (${greatest_increase:.2f})\n",
                f"Greatest Decrease in Profits: {months_greatest_decrease} (${greatest_decrease:.2f})\n"
]


# Print results
print(*Result_summary, sep="")

with open(output_file, "w") as Analysis:
    Analysis.writelines(Result_summary)


    




