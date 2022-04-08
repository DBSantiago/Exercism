"""This is the little_sister module.
 
Add or remove prefixes and suffixes to strings.
"""


def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    new_vocab_words = vocab_words[:]
    for index, word in enumerate(vocab_words):
        if index == 0:
            new_vocab_words[0] = word
        else:
            new_vocab_words[index] = prefix + word
    return (" :: ").join(new_vocab_words)


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    no_suffix_word = word[:-4]
    if no_suffix_word[-1] == "i":
        return no_suffix_word.replace("i", "y")
    return no_suffix_word


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence_list = sentence.split()
    adj = sentence_list[index]
    if adj[-1] == ".":
        verb = adj[:-1] + "en"
    else:
        verb = adj + "en"
    return verb
