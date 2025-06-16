import random
start = input("Start? (Y/N): ")
play_again = "Y"
if start.upper() == "Y":
    amount = int(input("Enter your amount of money(in dollars $): "))
    while start.upper() == "Y" or play_again.upper() == "Y":
        start = "n"
        i = 3
        symbols = []
        numbers = [0, 3, 5, 7]
        count=1
        if amount>0:
            while i>0:
                symbols.append(random.choice(numbers))
                i-=1
            for i in range(2):
                if symbols[i]==symbols[i+1]:
                    count+=1
            for i in symbols:
                print(i, end=" ")
            print()
            if count == 3:
                print("Congratulations, you won the jackpot!!")
                amount*=3
                print(f"Your new amount is: {amount}")
            elif symbols[0] == symbols[1] or symbols[1] == symbols[2] or symbols[0] == symbols[2]:
                print("Too bad guess you didnt win :(")
                print("Your amount is the same")
            else:
                print("Hehe thanks for the free cash")
                amount//=2
                print(f"Your new amount is: {amount}")
            play_again = input("Play again? (Y/N): ")
        else:
            print("Add some more money you brokie")
            stop = input("Stop? (Y/N): ")
            if stop.upper() == "Y":
                exit()
            elif stop.upper() == "N":
                amount = int(input("Enter your amount of money(in dollars $): "))
elif start.upper() == "N":
    print("Come back when you have the balls to gamble")
    exit()