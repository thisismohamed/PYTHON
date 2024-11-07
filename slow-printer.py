import time

def slowPrint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

slowPrint("Hello, Vistors!")
time.sleep(1)
slowPrint("I love slow print effects")
time.sleep(1)
slowPrint("Python is awesome")
time.sleep(1)
print("Learn python from https://learnpython.org")
