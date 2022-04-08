"""This is the darts module.

Calculates score on dartboard hits.
"""


def score(x, y):
    distance_from_center = (abs(x) ** 2 + abs(y) ** 2) ** (1/2)
    score = 0

    if 10 >= distance_from_center > 5:
        score = 1
    elif 5 >= distance_from_center > 1:
        score = 5
    elif distance_from_center <= 1:
        score = 10

    return score
