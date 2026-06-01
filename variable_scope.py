global_var = "I am Global"


def outer():
    outer_var = "I am Nonlocal"

    def inner():
        nonlocal outer_var

        local_var = "I am Local"

        print(global_var)
        print(outer_var)
        print(local_var)

    inner()


outer()
