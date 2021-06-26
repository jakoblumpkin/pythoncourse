def gen123():
    yield 1
    yield 2
    yield 3

g=gen123()

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246()


# any and all
# if any True or is all true
print(any([False, False, True]))

print(all([False, False, True]))

#any(is_prime(x) for x in range(1328, 1361))
