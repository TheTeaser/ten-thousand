from ten_thousand.game_logic import GameLogic
roll_dice = GameLogic.roll_dice
points_calculate = GameLogic.calculate_score
validate_keepers = GameLogic.validate_keepers


def play(roller=GameLogic.roll_dice, num_rounds=20):
    """
    The play() is responsible for starting the game.
    """
    global roll_dice
    roll_dice = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_response = input('> ')
    if user_response.lower() == 'y':
        start_game(num_rounds)
    elif user_response.lower() == "n":
        quitter()


def start_game(num_rounds, round_num=1, total=0, number_dices=6, round_score=0):
    """
    This function starts the game once the user enters (y/Y).
    """
    if (round_num > num_rounds):
        end_game(total)
        return
    if (number_dices == 6 and round_score == 0):
        print(f"Starting round {round_num}")
    print(f"Rolling {number_dices} dice...")
    first_roll = roll_dice(number_dices)
    result = ' '.join(str(x) for x in first_roll)
    print(f"*** {result} ***")
    if (points_calculate(first_roll) == 0):
        zilcher(num_rounds, round_num, total)
        return
    print('Enter dice to keep, or (q)uit:')
    dice_picked = input("> ")
    if dice_picked.lower() == "q":
        end_game(total)
        return
    if dice_picked == "":
        round_score = 0
        end_game(total)
    var = dice_picked.replace(" ", "")
    kept_dices = tuple(int(x) for x in var)
    if not validate_keepers(first_roll, kept_dices):
        print("Cheater!!! Or possibly made a typo...")
        kept_dices = cheater(num_rounds, first_roll,
                             round_num, round_score, total)
    remaining_dices = number_dices - len(kept_dices)
    round_score += points_calculate(kept_dices)
    if (remaining_dices == 0 and number_dices == 6):
        hot_dice(num_rounds, round_score, round_num, total, number_dices)
        return
    elif remaining_dices == 0:
        number_dices = 6
        hot_dice(num_rounds, round_score, round_num, total, number_dices)
        return
    print(
        f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
    print(f"(r)oll again, (b)ank your points or (q)uit:")
    end_of_round = input("> ")
    if end_of_round.lower() == 'b':
        bank_points(num_rounds, round_score, round_num, total)
    elif end_of_round.lower() == 'r':
        start_game(num_rounds, round_num, total, remaining_dices, round_score)
    else:
        end_game(total)


def quitter():
    """
    This function quits the game.
    """
    print('OK. Maybe another time')


def bank_points(num_rounds, points, round_num, total):
    """
    This function banks the points user earned whenever the user presses (b).
    """
    total += points
    print(f"You banked {points} points in round {round_num}")
    print(f"Total score is {total} points")
    round_num += 1
    start_game(num_rounds, round_num, total)


def cheater(num_rounds, first_roll, round_num, round_score, total):
    result = ' '.join(str(x) for x in first_roll)
    print(f"*** {result} ***")
    print('Enter dice to keep, or (q)uit:')
    dice_picked = input("> ")
    if dice_picked.lower() == "q":
        end_game(total)
        return
    if dice_picked == "":
        round_score = 0
        bank_points(num_rounds, round_score, round_num, total)
    var = dice_picked.replace(" ", "")
    kept_dices = tuple(int(x) for x in var)
    if not validate_keepers(first_roll, kept_dices):
        print("Cheater!!! Or possibly made a typo...")
        cheater(num_rounds, first_roll, round_num, round_score, total)
    elif (points_calculate(kept_dices) == 0):
        return "zilch"
    else:
        return kept_dices


def zilcher(num_rounds, round_num, total):
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")
    print(f"You banked 0 points in round {round_num}")
    print(f"Total score is {total} points")
    round_num += 1
    start_game(num_rounds, round_num, total)


def hot_dice(num_rounds, round_score, round_num, total, dices_number):
    print(
        f"You have {round_score} unbanked points and {dices_number} dice remaining")
    print(f"(r)oll again, (b)ank your points or (q)uit:")
    end_of_round = input("> ")
    if end_of_round.lower() == 'b':
        bank_points(num_rounds, round_score, round_num, total)
    elif end_of_round.lower() == 'r':
        start_game(num_rounds, round_num, total, dices_number, round_score)
    else:
        end_game(total)


def end_game(total):
    """
    This function prints a Good-bye message in addition to the total points earned.
    """
    print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    play()
