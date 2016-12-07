import math


# ToDo: add a function or two to aggregate information about lists of strings.
# ToDo: change the assumption to so that the iterables are assumed to contain
# strings and mean and median then just parse strings to floats and catch
# errors. Also makes testing more fun :)

def mean(input_):
    """compute the mean of the values in an iterable.
    """
    return sum(input_)/len(input_)


def median(input_):
    """ compute the median of values in an iterable.
        If the length of the list is even pick the leftmost iterable.
    """
    # This is actually broken because there is no sort step.
    return input_[int(math.floor(len(input_) / 2))]

