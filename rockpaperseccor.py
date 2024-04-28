class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Your vote for {candidate} has been recorded.")
        else:
            print("Invalid candidate!")

    def display_results(self):
        print("Voting Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")


def main():
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    voting_system = VotingSystem(candidates)
    
    print("Welcome to the Voting System!")
    print("Candidates:", ", ".join(candidates))
    
    while True:
        choice = input("Enter the name of the candidate you want to vote for (or 'done' to finish): ").strip().title()
        
        if choice == "Done":
            break
        
        voting_system.vote(choice)
    
    voting_system.display_results()

if __name__ == "__main__":
    main()

