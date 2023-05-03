import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    def calculate_score(tup):
        total_points = 0
        counter = Counter(tup)
        # Three pairs
        if len(counter) == 3 and all(val == 2 for val in counter.values()):
            total_points += 1500
            return total_points
        if counter[5] == 1 or counter[5] == 2:
            total_points += 50 * counter[5]
        if counter[1] == 1 or counter[1] == 2:
            total_points += 100*counter[1]
        # Three of a kind:
        if counter[1] == 3:
            total_points += 1000
        if counter[2] == 3:
            total_points += 200
        if counter[3] == 3:
            total_points += 300
        if counter[4] == 3:
            total_points += 400
        if counter[5] == 3:
            total_points += 500
        if counter[6] == 3:
            total_points += 600
        # Four of a kind:
        if counter[1] == 4:
            total_points += 2000
        if counter[2] == 4:
            total_points += 400
        if counter[3] == 4:
            total_points += 600
        if counter[4] == 4:
            total_points += 800
        if counter[5] == 4:
            total_points += 1000
        if counter[6] == 4:
            total_points += 1200
        # Five of a kind:
        if counter[1] == 5:
            total_points += 4000
        if counter[2] == 5:
            total_points += 800
        if counter[3] == 5:
            total_points += 1200
        if counter[4] == 5:
            total_points += 1600
        if counter[5] == 5:
            total_points += 2000
        if counter[6] == 5:
            total_points += 2400
        # Six of a kind:
        if counter[1] == 6:
            total_points += 8000
        if counter[2] == 6:
            total_points += 1600
        if counter[3] == 6:
            total_points += 2400
        if counter[4] == 6:
            total_points += 3200
        if counter[5] == 6:
            total_points += 4000
        if counter[6] == 6:
            total_points += 4800
        # Zilch
        if counter[2] or counter[3] or counter[4] or counter[6] < 3:
            total_points += 0
        # Straight
        if counter[1] and counter[2] and counter[3] and counter[4] and counter[5] and counter[6] == 1:
            total_points += 1350
        return total_points

    def roll_dice(int):
        num_list = []
        for i in range(int):
            randomNumber = random.randint(1, 6)
            num_list.append(randomNumber)
        return tuple(num_list)
        # Fives:

    def validate_keepers(first_roll, kept_dices):
        dices = Counter(GameLogic.get_scorers(first_roll))
        keepers = Counter(kept_dices)
        count = keepers-dices
        if not count:
            return True
        else:
            return False

    def get_scorers(first_roll):
        if not first_roll:
            return ()
        else:
            full_score = GameLogic.calculate_score(first_roll)
            result = []
            for i in first_roll:
                lis = []
                for j in first_roll:
                    if j != i:
                        lis.append(j)
                tup = tuple(lis)
                if (full_score != GameLogic.calculate_score(tup)):
                    result.append(i)
            return tuple(result)
