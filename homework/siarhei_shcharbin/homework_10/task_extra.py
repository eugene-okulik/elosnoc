def counter(count):

    def repeat_me(func):

        def wrapper(text):
            i = 1
            while i <= count:
                i += 1
                func(text)
        return wrapper
    return repeat_me


@counter(count=5)
def example(text):
    print(text)


example('print me')

# некоторое время погуглил и уловил посыл, что нужна еще одна внешняя функция для счетчика.
# но код правил чисто интуитивно с подсказками/подсветками самого пайчарма.
# для меня эта тема, как движение автомобиля - понимаю принцип движения, но без понятия, как работает изнутри))
