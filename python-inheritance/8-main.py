#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

BaseGeometry = __import__('8-rectangle').BaseGeometry
test_class = Rectangle
some_class = BaseGeometry
print(f"Is {test_class} subclass of {some_class}: {issubclass(test_class, some_class)}")
