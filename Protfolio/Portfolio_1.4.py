# Task 4

# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).

# Boycott's batting average.
# Geoffrey Boycott:
# Matches: 609
# Batted: 1014
# Times not out: 162
# Runs scored: 48426

matches = 609
batted = 1014
times_not_out = 162
runs_scored = 48426
batting_average = (runs_scored / (batted - times_not_out))

print(f"\nGeoffrey Boycott:\n\n    Matches: {matches}")
print(f"    Batted: {batted}")
print(f"    Times not out: {times_not_out}")
print(f"    Runs scored: {runs_scored}")
print(f"    Boycott's batting average: {round(batting_average,2)}")

# Output:

# Geoffrey Boycott:
#
#     Matches: 609
#     Batted: 1014
#     Times not out: 162
#     Runs scored: 48426
#     Boycott's batting average: 56.84

