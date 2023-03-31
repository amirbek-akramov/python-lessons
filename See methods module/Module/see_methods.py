def see_methods(classOrObject):
    # Class or object. Illustrate the all methods of classes or objects
    return [method for method in dir(classOrObject) if not method.startswith("__")]

def see_default_methods(classOrObject):
    # Class or object. Illustrate the all default methods of classes or objects
    return [method for method in dir(classOrObject) if method.startswith("__")]
