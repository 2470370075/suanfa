def outer():
    name="python"
    def inner():
        print(name)
    inner()
outer()