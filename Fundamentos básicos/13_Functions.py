from re import M


def say_hello():
    print("hello")

def fahr2Celsius(fahr):
    celsius = (5*(fahr-32))/9
    return celsius

print(fahr2Celsius(3422423))