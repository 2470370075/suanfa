def a():
    l = []
    print(1)
    c = 0
    def helper():

        print(2)
        l.append(1)
        print(l)
        helper()
    print(3)
    helper()

a()