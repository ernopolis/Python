# def hello(name):
#     print(f"Hello {name}")
# hello("kim")


# def f(x):
#     return x * x
# result = f(2)
# if result == 4:
#     print("ok!")


def average(x, y):
    return (x + y) / 2


print(average(3, 4))


def testAverage():
    arg1 = 3
    arg2 = 4
    expected = 3.5
    result = average(arg1, arg2)
    if expected == result:
        print("TEST PASSED")
    else:
        print("FAILED!")
        print(f"expected {expected}, but got {result}")


testAverage()
