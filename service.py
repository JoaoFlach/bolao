import data


def get_matches():
    return data.matches


def update_guess_card(match_points, i, player_guess_card):
    player_guess_card[i]['points'] = match_points
    return player_guess_card


def calculate_player_points(payload):
    player_guess_card = payload['playerGuesses']
    matches = get_matches()

    for i in range(len(matches)):
        player_guess = player_guess_card[i]
        match_score = data.scores[i]

        match_points = get_match_points(match_score, player_guess)

        player_guess_card[i]['points'] = match_points

        i += 1

    print(player_guess_card)

    return player_guess_card


def get_match_points(match_score, player_guess):
    points = 0

    if is_exact_guess(player_guess, match_score):
        points = 10

    elif guessed_right_winner(player_guess, match_score):
        points = 5

    return points


def guessed_right_winner(guess, score):
    guessed_result = get_result(guess)
    match_result = get_result(score)
    return guessed_result == match_result


def get_result(score):
    if score['home'] > score['away']:
        return 'home'
    elif score['home'] < score['away']:
        return 'away'
    return 'draw'


def is_exact_guess(guess, actual):
    return guess == actual
