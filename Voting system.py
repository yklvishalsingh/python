def voting_system():
 candidates = {}
 num_candidates = int(input("Enter the number of candidates: "))
 # Initialize candidates with zero votes
 for i in range(num_candidates):
  candidate_name = input(f"Enter the name of candidate {i+1}: ")
 candidates[candidate_name] = 0
 num_voters = int(input("Enter the number of voters: "))
 # Record votes
 for i in range(num_voters):
  print(f"Voter {i+1}, please select your candidate:")
 for candidate in candidates:
  print(f"{candidate}")
 vote = input("Enter candidate name: ")
# Check if the candidate exists
 if vote in candidates:
  candidates[vote] += 1
  print("Vote recorded successfully!")
 else:
  print("Invalid candidate! Vote not recorded.")
 print("\nElection Results:")
 for candidate, votes in candidates.items():
  print(f"{candidate}: {votes} votes")
voting_system()
