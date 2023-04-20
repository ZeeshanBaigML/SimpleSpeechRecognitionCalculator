
import transformers
import torch

# Load the pipeline for speech recognition
recognizer = transformers.pipeline("automatic-speech-recognition")

# Define math operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Map recognized commands to math functions
math_functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Main program loop
while True:
    # Get user input
    print("Say a math operation and two numbers, e.g. 'add 3 and 5'")
    input_text = input("> ")

    # Use speech recognition to transcribe input text
    recognized_text = recognizer(input_text)[0]["text"]

    # Parse recognized text to extract operation and numbers
    parts = recognized_text.split()
    if len(parts) != 4:
        print("Sorry, I didn't understand that. Please try again.")
        continue

    operation = parts[0]
    x = float(parts[1])
    y = float(parts[3])

    # Perform math operation and print result
    result = math_functions[operation](x, y)
    print("Result:", result)
