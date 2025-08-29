import time


Practice_Sentence = "I am learning how to type fast and accurately. Here's me trying"
words = len(Practice_Sentence.split())
attempt_separator = "-+-" * 20

start_time = time.time()
print(attempt_separator) 
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
    print(f"your typing accuracy was", accuracy*100, "%")
    print(f"You can type {words_per_minute} words per minute")
    print(attempt_separator)
    print("Would you like to try again?")
    if input():
        start_time = time.time()
        print(attempt_separator)
    else:
        print("Thank you for playing! Goodbye!")