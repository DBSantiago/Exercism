""" These functions are used to build a high-scores component in a game.
"""


def latest(scores):
    """

    :param scores: list - all the scores in the game.
    :return: int - the latest score.
    """
    return scores[-1]


def personal_best(scores):
    """

    :param scores: list - all the scores in the game.
    :return: int - the highest score.
    """
    scores.sort()

    return scores[-1]


def personal_top_three(scores):
    """

    :param scores: list - all the scores in the game.
    :return: list - the 3 highest scores.
    """
    scores_copy = list(scores)

    scores_copy.sort()

    highest_three = scores_copy[-3:]

    highest_three.reverse()

    return highest_three
