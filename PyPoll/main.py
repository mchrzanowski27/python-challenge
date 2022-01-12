import os
import csv

election_csv = os.path.join("PyPoll","Resources","election_data.csv")
output_file = os.path.join("PyPoll" , "Analysis" ,"election-anaylysis.txt")

Khan = 0
Correy = 0
Li = 0
OTooley = 0

# count votes for each candidate
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")


    for row in csvreader:
        if row[2] == "Khan":
            Khan += 1

        elif row[2] == "Correy":
            Correy += 1

        elif row[2] == "Li":
            Li += 1

        elif row[2] == "O'Tooley":
            OTooley += 1


# calculate total votes
total_votes = Khan + Correy + Li + OTooley

# calculate percentage votes for each candidate 
print(f"Total Votes: {total_votes}")
print(f'Khan: {Khan/total_votes} ({Khan})')
print(f'Correy: {Correy/total_votes} ({Correy})')
print(f'Li: {Li/total_votes} ({Li})')
print(f'OTooley: {OTooley/total_votes} ({OTooley})')


Election_summary = ["Election Results" "\n",
                    "---------------------------\n",
                    f"Total Votes: {total_votes}\n",
                    "---------------------------\n",
                    f"Khan: {Khan/total_votes:.3%} ({Khan})\n",
                    f"Correy: {Correy/total_votes:.3%} ({Correy})\n",
                    f"Li: {Li/total_votes:.3%} ({Li})\n",
                    f"O'Tooley: {OTooley/total_votes:.3%} ({OTooley})\n",
                    "---------------------------\n"
]

# find the winner
winner = max(Khan, Correy, Li, OTooley)
if winner == Khan:
    Election_summary.append("Winner: Khan\n",)
elif winner == Correy:
    Election_summary.append("Winner: Correy\n",)
elif winner == Li:
    Election_summary.append("Winner: Li\n",)
elif winner == OTooley:
    Election_summary.append("Winner: O'Tooley\n",)

Election_summary.append("---------------------------\n")

# print/write text file
print(*Election_summary, sep="")

with open(output_file, "w") as Results:
    Results.writelines(Election_summary)
