print("Welcome to the Fizz Buzz Game")
player = input("Enter your name:")
instructions = '''
1. Type 'Fizz' for multiples of 3,
2.'Buzz' for multiples of 5, 
3.'FizzBuzz' for multiples of both.
4. Otherwise, just type the number itself.
5. One wrong guess and the game is over!.
6. Survive all 100 rounds to win!.
'''
print(f"Welcome {player}!, There are the instructions. {instructions}")
import random
total = 0
prev_number = 0
while True:

    number = random.randint(1, 20)
    total = prev_number + number    
    prev_number = number            
    

    if total % 3 == 0 and total % 5 == 0:
        correct = "fizzbuzz"
    elif total % 3 == 0:
        correct = "fizz"
    elif total % 5 == 0:
        correct = "buzz"
    else:
        correct = str(total)
    

    print(number)  
    guess = input("Your answer: ").lower()
        
    if guess != correct:
        print(f"Wrong! The correct answer was {correct}. Game Over!")
        break
else:
    print("Congratulations! You survived all 100 rounds of FizzBuzz!")

