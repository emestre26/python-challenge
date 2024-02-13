import csv

with open('/Users/eddie/Desktop/python-challenge/python-challenge/PyPoll/Resource/election_data.csv', mode='r') as file:
    reader = csv.reader(file)
    new_reader = csv.DictReader(file)
    next(reader)

    
    
    Candidates = set()
    Votes_per_Candidate = {}
    Total_Votes = 0
        
    for row in reader:
    
        
        Candidates.add(row[2])
        Total_Votes += 1
        Candidate = row[2]
        
        if Candidate in Votes_per_Candidate:
            Votes_per_Candidate[Candidate] += 1
        else:
            Votes_per_Candidate[Candidate] = 1
            
            Total_Votes += 1
        
    Winner= max(Votes_per_Candidate, key=Votes_per_Candidate.get)

    print("Total Votes: " +str(Total_Votes))
    print("Candidates Receiving Votes: " +str(Candidates))
    
    print("Candidates Vote Percentage: ")
    for Candidate, votes in Votes_per_Candidate.items():
        percentage = (votes/Total_Votes)*100
        print(f"{Candidate}: {percentage:.2f}%")

    
        print(f"{Candidate}: ({votes}" ')')
    print("Winner: ", Winner)
    
    
        
