import time
import sys

Practice_Sentence = "I am learning how to type fast and accurately."
words = len(Practice_Sentence.split())
attempt_separator = "-+-" * 20

def print_welcome_message():
    print("Welcome to the Typing Speed Test!")
    print("You will be given a sentence to type as fast and accurately as you can.")
    print("Your typing speed and accuracy will be calculated at the end.\n")

def Retry():
    print("\n Would you like to try again? (Yes or no?)" )
    if input() in ["Yes", "yes", "Y", "y"]:
        print(attempt_separator)
        start_time = time.time()   
    else:
        print("Thank you for playing! Goodbye!")
        sys.exit()

print(attempt_separator)
start_time = time.time()

def main():
    print_welcome_message()
    while 1:
        print("Type the sentence below as fast and accurately as you can: \n", Practice_Sentence)
        user_input = input("\n your attempt: ")
        user_words = len(user_input.split())
        end_time = time.time()
        elapsed_time = end_time - start_time
        accuracy = len(set(user_input.split()) & set(Practice_Sentence.split())) # checks if the length of set of unique words of user input is same as that of the original sentence.
        accuracy = (accuracy / words)
        words_per_minute = user_words / (elapsed_time / 60)

        print()
        print(f"You took {elapsed_time: .1f} seconds to type")
        print("your typing accuracy was", round(accuracy*100, 2), "%")
        print(f"You can type {words_per_minute: .0f} words per minute")
        print(attempt_separator)
        Retry()

if __name__ == '__main__':
    main()


#SMALL DOCUMENTATION
"""
This is a simple Typing Speed Test program written in Python. 
The program prompts the user to type a predefined sentence as quickly and accurately as possible. 
It calculates the time taken, typing accuracy, and words per minute (WPM) based on the user's input.

> len() is a string method that returns the number of characters in a string or the number of items in a list.

> set() separates inputs into a set of unique words. Creates a set of unordered collection of unique elements. Output is a set containing elements from the input

> .1f means let the result be a floating point number and to 1 decimal place

> round() rounds a to the nearest whole number. Specifying 2 means round to 2 dp

> split() separates a string into a list of substrings based on a delimiter. Default is a white space. 
    e.g words = ["Hello", "world", "Hello"]
        unique_words = set(words)  
        Output = {'Hello', 'world'} we see that hello appears just once in the output.
"""