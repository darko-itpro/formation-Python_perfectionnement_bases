
def count_calls(func):
    count = 0
    def inner():
        nonlocal count
        count += 1
        func()

    def get_count():
        return count

    inner.nbcalls = get_count

    return inner


@count_calls
def some_func():
    print("func called")

print(some_func.nbcalls())
some_func()
some_func()
print(some_func.nbcalls())