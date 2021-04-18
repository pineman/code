# This program demonstrates two python gotchas:
# late binding closures and mutable default arguments.
# http://docs.python-guide.org/en/latest/writing/gotchas/

def foo(a, methods=[]): # methods defaults to [] if not specified
    for i in range(3):
        # Append an anonymous function which returns x + i
        # to the `methods` array of functions
        methods.append(lambda x: x + i)

    sum_methods = 0
    # For each function `method` of in `methods`, sum `method(a)`
    for method in methods:
        sum_methods += method(a)
    return sum_methods

print(foo(0))  # Should be 3
print(foo(1))  # Should be 6
print(foo(2))  # Should be 9
print(foo(2, [lambda x: x]))  # Should be 11
print(foo(0))  # Should be 3
print(foo(1))  # Should be 6
print(foo(2))  # Should be 9
