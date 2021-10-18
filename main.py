import data
import handler

if __name__ == '__main__':
    _event = {
        "function": "calculate_player_points",
        "payload": {
            "playerGuesses": data.player_guesses,
            "username": "username"
        }
    }

    handler.handler(_event, {})
