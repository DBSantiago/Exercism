"""These functions help with color coding resistors.
"""


def color_code(color):
    """Look up the numerical value associated with a particular color band.

    :param color: str - band color
    :return: int - numerical value associated with the color passed as argument
    """
    colors = ["black", "brown", "red", "orange", "yellow",
              "green", "blue", "violet", "grey", "white"]

    return colors.index(color)


def colors():
    """List the different band colors.

    :return: list -  list of different band colors
    """
    colors = ["black", "brown", "red", "orange", "yellow",
              "green", "blue", "violet", "grey", "white"]

    return colors
