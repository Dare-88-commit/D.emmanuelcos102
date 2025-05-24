x = 10


def outer_func():
    x = 20

    def inner_func():
        global x
        x = 30
    inner_func()
    print("x in outer_func:", x)


print("x in global:", x)
