# Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time, os, sys

def typingPrint(*args):
    """Print text with a typing effect."""
    import sys, time
    text = ''.join(map(str, args))  # Concatenate arguments into a single string
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    value = input()
    return value