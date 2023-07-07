import random
from typing import List


def roll_dice_sided_n(side: int, times: int):
    results = []
    for _ in range(times):
        dice = random.randint(1, side)
        results.append(dice)

    return results


n = int(input("サイコロの面の数は?"))
m = int(input("何回振りますか?"))


print(roll_dice_sided_n(side=n, times=m))
