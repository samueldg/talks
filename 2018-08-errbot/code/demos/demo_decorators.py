"""Demo of the ability to set a function attribute from within a decorator.

We simply tag some functions as "cool" or not, and canuse that information
later to act on these functions accordingly.
"""

def cool(func):
    func._cool = True
    return func


@cool
def studying():
    pass


def doing_drugs():
    pass


if __name__ == '__main__':

    for func in [studying, doing_drugs]:

        coolness = getattr(func, '_cool', False)

        if coolness:
            print(f'{func.__name__} is cool :)')
        else:
            print(f'{func.__name__} is not cool :(')
