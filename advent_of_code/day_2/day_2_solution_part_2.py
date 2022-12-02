with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_2/input.txt', 'r') as f:
    contents = f.read()

tournament = contents.split('\n')

def result_of_game(game):
    '''
        points: 
        A - Rock - 1
        B - Paper - 2
        C - Scissors - 3

        X = lose 
        Y = draw 
        Z = win
    '''

    rules = {'A':['C', 'B'], 'B':['A', 'C'], 'C':['B', 'A']}
    points = {'C':3, 'A':1, 'B':2}

    game_score = 0 
    game_input = game.split(' ')

    if game_input[1] == 'Z':
        responce = rules[game_input[0]][1]
        game_score = game_score  + 6 + points[responce]

    elif game_input[1] == 'Y':
        responce = game_input[0]
        game_score = game_score + 3 + points[responce]

    else: 
        responce = rules[game_input[0]][0]
        game_score = game_score  + points[responce]

    return game_score

result_games = []
for game in tournament:
    result_games.append(result_of_game(game))

print(sum(result_games))

