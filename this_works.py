import a_module


def another_quack() -> None:
    print('another_quack')


class Test:

    def __init__(self) -> None:
        setattr(a_module, 'quack', another_quack)
        a_module.quack()


if __name__ == '__main__':
    Test()
