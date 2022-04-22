low = 1
high = 1000
print(f"please think of a number in between {low} and {high}")
input("press Enter to start")
guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}. Should i guess higher or lower?"
                     "please enter h for high, l for low or c if answer is correct").casefold()
    if high_low == "h":
        # guess higher
        low = guess + 1

    elif high_low == "l":
        # guess lower
        high = guess - 1
    elif high_low == "c":
        print(f"Got it correct in {guesses} guess/es")
        break
    else:
        print("Please enter h,l or c")
    guesses += 1
else:
    print(f"You thought of the number {low}, i got it correct in {guesses} guesses")