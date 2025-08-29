import time
import sys

Practice_Sentence = "I am learning how to type fast and accurately."
words = len(Practice_Sentence.split())
attempt_separator = "-+-" * 20

def print_welcome_message():
    print("Welcome to the Typing Speed Test!")
    print("You will be given a sentence to type as fast and accurately as you can.")
    print("Your typing speed and accuracy will be calculated at the end.")

def Retry():
    print("Would you like to try again? (Yes or no?)" )
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
        print("Type the following sentence as fast and accurately as you can: ", Practice_Sentence)
        user_input = input("your attempt: ")
        user_words = len(user_input.split())
        end_time = time.time()
        elapsed_time = end_time - start_time
        accuracy = len(set(user_input.split()) & set(Practice_Sentence.split()))
        accuracy = (accuracy / words)
        words_per_minute = user_words / (elapsed_time / 60)

        print(f" You took {elapsed_time: 1f} seconds to type")
        print("your typing accuracy was", accuracy*100, "%")
        print(f"You can type {words_per_minute} words per minute")
        print(attempt_separator)
        Retry()



if __name__ == '__main__':
    main()