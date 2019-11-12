import string


def contains_idiom(sentence):
    """
    test a sentence for idiomatic expression
    :param sentence: text to analyze
    :return: boolean indication
    """
    sentence = sentence.strip().lower()
    if any(expression in sentence for expression in IDIOMATIC): return True

    for expression in IDIOMATIC_FOLLOWED_BY_PUNCTUATION:
        if expression not in sentence: continue
        if sentence.endswith(expression): return True
        # assuming untokenized input, e.g., "or something,"
        next_char_index = sentence.index(expression) + len(expression)
        if sentence[next_char_index] in string.punctuation: return True
    # end for
    return False
# end def


IDIOMATIC_FOLLOWED_BY_PUNCTUATION = ['or something, or anything']
IDIOMATIC = ['something something', 'than anything else', 'more than anything',
             ' or something like that', 'if anything']

if __name__ == '__main__':

    assert (contains_idiom('you should eat your meal or something'))
    assert (contains_idiom('i really like this book, more than anything!'))
    assert (contains_idiom('if anything, we should go out and check this ourselves!'))
    assert (contains_idiom('we should go out and check this ourselves if anything'))

    assert (not contains_idiom('you should buy this book, or something like this book'))
    assert (not contains_idiom('if anything matters that much to you, go ahead'))
    assert (not contains_idiom('is there anything i can do for you?'))

# end if
