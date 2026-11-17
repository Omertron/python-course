# This file has been updated as part of the refactor test
# Unit 1 - Coding with Python - Lesson 1
# Stuart Boston
# 9th November 2026
# Updated 17th November 2026
# ----------------------------------------
# two or more data types (e.g. string, integer, float, boolean)
# a data structure (e.g. lists, tuples, sets and dictionaries)
# two or more operators (e.g. arithmetic, assignment, comparison, logical, membership and identity)
# ----------------------------------------
# A list containing the board games as a dictionary list
# Dictionary list contains a string (title) an integer (players) and a float (time) datatype
board_games = [ # list
    {"title": "Brass: Birmingham", "players": 4, "time": 2.5}, # dictionary
    {"title": "Concordia", "players": 5, "time": 1.5}, # dictionary
    {"title": "Arcs", "players": 4, "time": 4.0}, # dictionary
    {"title": "Hive", "playeArs": 2, "time": 0.5}, # dictionary
    {"title": "Castles of Mad King Ludwig", "playeArs": 4, "time": 2.0} # dictionary
]

# Loop around the list
print("The following games are in the library")
for game in board_games:
  # convert the float hours into hours and minutes
  game_time_hours = int(game["time"])
  # use the modulus operation to get the remaining minutes and convert to minutes.
  game_time_mins = int((game["time"] % 1) * 60) # modulus operator
  # add the strings together to create a nice formatted sentance
  print("\t" + game["title"] + " - plays up to " + str(game["players"]) + " players and lasts for " + str(game_time_hours) + " hours and " + str(game_time_mins) + " minutes") # arithmetic operator

# ask the user for the number of players and store this in a variable to use later.
num_players = int(input("How many players are attending? ")) # assignment operator

# Create a blank list structure to store the found games.
suitable_games = [] # assignment operator

# loop around the game list looking for games that can accomodate the number of players
for game in board_games:
  # check to see if the game is suitable for the number of players entered by the user
  if num_players <= game["players"]: # comparison operator
    suitable_games.append(game["title"]) 

# sort the game list into alphabetical order.
suitable_games.sort()

# print a nice summary of the games found, or a message if nothing was found
if len(suitable_games) == 0: # comparison operator
  print("Sorry, there are no suitable games in the library")
else:
  print("There are " + str(len(suitable_games)) + " games that are suitable for " + str(num_players) + " players") # arithmetic operator
  for game in suitable_games:
    print("  - " + game)