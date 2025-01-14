def repeat_me(func):

    def wrapper(text, count):
        # i = 1
        # while i <= count:
        for i in range(count):
            i += 1
            func(text, count)
    return wrapper


@repeat_me
def example(text, count):
    print(text)


example('print me', count=4)
