'''
points: 
A/X - Rock - 1
B/Y - Paper - 2
C/Z - Scissors - 3

'''
with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_2/input.txt', 'r') as f:
    contents = f.read()

tournament = contents.split('\n')

def result_of_game(game):

    rules = {'A':['Z', 'X'], 'B':['X', 'Y'], 'C':['Y','Z']}
    points = {'Z':3, 'X':1, 'Y':2}

    game_score = 0 
    game_input = game.split(' ')

    if rules[game_input[0]][0] == game_input[1]:
        game_score = game_score  + points[game_input[1]]
    elif rules[game_input[0]][1] == game_input[1]:
        game_score = game_score + 3 + points[game_input[1]]
    else:
        game_score = game_score + 6 + points[game_input[1]]
    return game_score

result_games = []
for game in tournament:
    result_games.append(result_of_game(game))

print(sum(result_games))
