# Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
# import os and time module to clear the screen and add delay
import sys, time
# typing effect for printing text function, super cool!!
def typingPrint(*args):
    text = ''.join(map(str, args))  # Concatenate arguments into a single string
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
# typing effect for input function, super cool!!
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    value = input()
    return value

