def outer():
    def inner1():
        def inner2():
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()