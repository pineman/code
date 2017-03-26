""" File to hold all the functions and code that,
while not directly change the game, are needed for it to work properly """

def wraps(original_func):
    """Update the decorated function with some important attributes from the
    one that was decorated so as not to lose good information"""
    def update_attrs(new_func):
        # Update the __annotations__
        for key, value in original_func.__annotations__.items():
            new_func.__annotations__[key] = value
        # Update the __dict__
        for key, value in original_func.__dict__.items():
            new_func.__dict__[key] = value
        # Copy the __name__
        new_func.__name__ = original_func.__name__
        # Copy the docstring (__doc__)
        new_func.__doc__ = original_func.__doc__
        return new_func
    return update_attrs # return the decorator
    
def ensure_types(f):
    """Uses f.__annotations__ to check the expected types for the function's
    arguments. Raises a TypeError if there is no match.
    If an argument has no annotation, object is returned and so, regardless of
    the argument passed, isinstance(arg, object) evaluates to True"""
    @wraps(f) # say that test_types is wrapping f
    def test_types(*args, **kwargs):
        # Loop through the positional args, get their name and check the type
        for i in range(len(args)):
            # function.__code__.co_varnames is a tuple with the names of the
            ##arguments in the order they are in the function def statement
            var_name = f.__code__.co_varnames[i]
            if not(isinstance(args[i], f.__annotations__.get(var_name, object))):
                raise TypeError("Bad type for function argument named '{}'".format(var_name))
        # Loop through the named args, get their value and check the type
        for key in kwargs.keys():
            if not(isinstance(kwargs[key], f.__annotations__.get(key, object))):
                raise TypeError("Bad type for function argument named '{}'".format(key))
        return f(*args, **kwargs)
    return test_types
    
def debug_dec(f):
    """Does some annoying printing for debugging purposes"""
    @wraps(f)
    def profiler(*args, **kwargs):
        print("{} function called:".format(f.__name__))
        print("\tArgs: {}".format(args))
        print("\tKwargs: {}".format(kwargs))
        return f(*args, **kwargs)
    return profiler
    
if __name__ = "__main__":
	pass