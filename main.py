match_list = [
    {"home": "blueteam", "away": "redteam"},
    {"home": "yellowteam", "away": "greenteam"},
    {"home": "blackteam", "away": "purpleteam"},
]

guess_list = [
    {"home": 0, "away": 0},
    {"home": 2, "away": 0},
    {"home": 1, "away": 2},
]

match_result_list = [
    {"home": 0, "away": 3},
    {"home": 0
        , "away": 1},
    {"home": 4, "away": 3},
]


class Match(object):
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team


def is_exact_guess(guess, actual):
    return guess == actual


def guessed_winner_or_tie(guess, match_result):
    match_winner = "draw"
    guess_winner = "draw"

    if guess['home'] > guess['away']:
        guess_winner = 'home'
    elif guess['home'] < guess['away']:
        guess_winner = 'away'

    if match_result['home'] > match_result['away']:
        match_winner = 'home'
    elif match_result['home'] < match_result['away']:
        match_winner = 'away'

    return guess_winner == match_winner


def run(event, context):
    points = 0

    for i in range(len(match_list)):
        guess = guess_list[i]
        match_result = match_result_list[i]

        if is_exact_guess(guess, match_result):
            points += 10

        elif guessed_winner_or_tie(guess, match_result):
            points += 5

        i += 1

    print(f"Points = {points}")


if __name__ == '__main__':
    run({}, {})
