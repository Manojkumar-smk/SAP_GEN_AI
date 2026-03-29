def dynamic_function(*args, **kwargs):
    print("positional arguments", args)
    print("keyword arguments", kwargs)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

dynamic_function(1, 2, 3, name="Alice", age=30)
