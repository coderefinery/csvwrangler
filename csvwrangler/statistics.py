import math


def mean(input_):
    """compute the mean of the values in an iterable.
    """
    return sum(input_)/len(input_)


def median(input_):
    """ compute the median of values in an iterable.
        If the length of the list is even pick the leftmost iterable.
    """
    return input_[int(math.floor(len(input_) / 2))]
