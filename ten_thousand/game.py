from game_logic import GameLogic
roll_dice = GameLogic.roll_dice
points_calculate = GameLogic.calculate_score


def play(roller=GameLogic.roll_dice):
    """
    The play() is responsible for starting the game.
    """
    global roll_dice
    roll_dice = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_response = input('> ')
    if user_response.lower() == 'y':
        start_game()
    elif user_response.lower() == "n":
        quitter()


def start_game(round_num=1, total=0, number_dices=6, round_score=0):
    validate_keepers = GameLogic.validate_keepers
    """
    This function starts the game once the user enters (y/Y).
    """
    if (number_dices == 6):
        print(f"Starting round {round_num}")
    print(f"Rolling {number_dices} dice...")
    first_roll = roll_dice(number_dices)
    result = ' '.join(str(x) for x in first_roll)
    print(f"*** {result} ***")
    print('Enter dice to keep, or (q)uit:')
    dice_picked = input("> ")
    if dice_picked.lower() == "q":
        end_game(total)
        return
    if dice_picked == "":
        round_score = 0
        bank_points(round_score, round_num, total)
    kept_dices = tuple(int(x) for x in dice_picked)
    remaining_dices = number_dices - len(kept_dices)
    if not validate_keepers(first_roll, kept_dices):
        print("Cheater!!! Or possibly made a typo...")
        print(f"*** {result} ***")
        return
    round_score += points_calculate(kept_dices)
    if remaining_dices == 0:
        bank_points(round_score, round_num, total)
    print(
        f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
    print(f"(r)oll again, (b)ank your points or (q)uit:")
    end_of_round = input("> ")
    if end_of_round.lower() == 'b':
        bank_points(round_score, round_num, total)
    elif end_of_round.lower() == 'r':
        if (remaining_dices == 0 and number_dices == 6):
            remaining_dices = 6
            start_game(round_num, total, remaining_dices, round_score)
        elif remaining_dices > 0:
            start_game(round_num, total, remaining_dices, round_score)
    else:
        end_game(total)


def quitter():
    """
    This function quits the game.
    """
    print('OK. Maybe another time')


def bank_points(points, round_num, total):
    """
    This function banks the points user earned whenever the user presses (b).
    """
    total += points
    print(f"You banked {points} points in round {round_num}")
    print(f"Total score is {total} points")
    round_num += 1
    start_game(round_num, total)


def end_game(total):
    """
    This function prints a Good-bye message in addition to the total points earned.
    """
    print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    play()
