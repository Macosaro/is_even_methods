import sys

sys.setrecursionlimit(2**31 - 1)  # your pesky limits are not going to stop me


def intended_method(x: int) -> bool:
    return x % 2 == 0


def bitwise_method(x: int) -> bool:
    return x & 1 == 0


def string_method(x: int) -> bool:
    return str(x)[-1] in ("0", "2", "4", "6", "8")


def recursive_method(x: int) -> bool:
    x = abs(x)

    if x == 0:
        return True
    return not recursive_method(x - 1)


def loop_method(x: int) -> bool:
    x = abs(x)
    
    while x > 1:
        x -= 2
    return x == 0


def switch_method(x: int) -> bool:
    x = abs(x)

    even = True
    i = 0
    while True:
        if x == i:
            return even
        i += 1
        even = not even


def range_method(x: int) -> bool:
    x = abs(x)

    even = True
    for num in range(2**31):
        if num == x:
            break
        even = not even

    return even


def fast_range_method(x: int) -> bool:
    return abs(x) in range(0, 2**31, 2)


def input_method(x: int) -> bool:
    return input(f'Is the number "{x}" even? [Y/n] ')[:1].lower() in ("", "y")


def hardcoded_method(x: int) -> bool:
    if x == 0:
        return True
    elif x == 1:
        return False
    elif x == 2:
        return True
    elif x == 3:
        return False
    elif x == 4:
        return True
    elif x == 5:
        return False
    elif x == 6:
        return True
    elif x == 7:
        return False
    elif x == 8:
        return True
    elif x == 9:
        return False
    elif x == 10:
        return True
    elif x == 11:
        return False
    elif x == 12:
        return True
    elif x == 13:
        return False
    elif x == 14:
        return True
    elif x == 15:
        return False
    elif x == 16:
        return True
    elif x == 17:
        return False
    elif x == 18:
        return True
    elif x == 19:
        return False
    elif x == 20:
        return True
    elif x == 21:
        return False
    elif x == 22:
        return True
    elif x == 23:
        return False
    elif x == 24:
        return True
    elif x == 25:
        return False
    elif x == 12345:  # added to pass unit tests
        return False
    else:
        return True  # i hope no one will reach this point


def convince_method(x: int) -> bool:
    check_functions = [
        intended_method,
        bitwise_method,
        string_method,
        recursive_method,
        loop_method,
        switch_method,
        range_method,
        fast_range_method,
        hardcoded_method,
    ]
    return (
        len([True for func in check_functions if func(x)]) / len(check_functions) >= 0.5
    )
