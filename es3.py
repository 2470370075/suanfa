
def a():
    c = 1
    def b():
        d = 2 + c
        print(d)
    b()
a()


def a():
    c = 1
    def b(c):
        c = 2 + c
        print(c)
    b(c)
a()