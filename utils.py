def choose(display, choices):
    a = str()
    while a not in choices:
        a = input(f"{display} {choices} :\n\t").lower()
    return a
