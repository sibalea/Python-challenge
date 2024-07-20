import os 
election_data = os.path.join("PyPoll","Ressources","election_data.csv")

total_votes = 0
candidates = {}
with open(election_data, 'r') as file:
    file.readline()

    for ballot in file:
        total_votes += 1
        ballot_info = ballot.strip().split(",")

        if ballot_info[2] not in candidates:
            candidates[ballot_info[2]] = 1
        else:
            candidates[ballot_info[2]] += 1

result = ""

for candidate in candidates:
    perc = round(float(candidates[candidate]/total_votes * 100), 3)
    result += f"{candidate}: {perc}% ({candidates[candidate]})\n"

print(
    f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{result.strip()}
-------------------------
Winner: {max(candidates, key = lambda x: candidates[x])}
-------------------------
""")