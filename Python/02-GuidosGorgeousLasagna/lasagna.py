EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - layers of lasagna.
    :return: int - minutes it'll take to make the lasagna layers.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake) in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - minutes the lasagna has been baking in the oven.
    :return: int - total number in minutes of preparation time and baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time