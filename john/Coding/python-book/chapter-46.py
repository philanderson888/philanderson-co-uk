date = "Wednesday 24/08/22"
print(date)

# a function for the score of a football game

def display_result(winner, score, **other_info) :
  print("The winner was " + winner)
  print("The score was " + score)
  for key, value in other_info.items():
    print(key + ": " + value)

display_result(winner="Real Madrid", score="1-0", overtime="yes", fouls="none")

# Note: Optional arguments must come after regular arguments. Optional parameters must come after regular parameters.

# Wednesday 24/08/22
# The winner was Real Madrid
# The score was 1-0
# overtime: yes
# fouls: none