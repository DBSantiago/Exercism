""" This module showcases Bob's conversational abilities.
"""


def response(hey_bob):
    answer = None

    clean_bob = hey_bob.strip().strip("0123456789")

    if clean_bob.isspace() == True or clean_bob.strip() == "":
        return "Fine. Be that way!"

    if clean_bob.endswith("?"):
        if clean_bob.isupper():
            answer = "Calm down, I know what I'm doing!"
        else:
            answer = "Sure."
    elif clean_bob.isupper() == True:
        answer = "Whoa, chill out!"
    else:
        answer = "Whatever."

    return answer
