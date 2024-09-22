#"შექმენით number guess თამაში. 
#description: შექმენით ცვლადი და მიანიჭეთ რაიმე int მნიშვნელობა. შექმენით მეორე ცვლადი რომელშიც მომხმარებელს შემოატანინებთ რაიმე რიცხვს. სანამ არ გამოიცნობს რა რიცხვი იყო პირველ ცვლადში, 
#დაუწერეთ: ""Try again"" თუ გამოიცნობს მაშინ: ""Congrats. You guessed the number"". (გამოიყენეთ while loop'ი)"	
# 


number = 10
user_guess = int(input("Guess the number from 1-100: "))
while number != user_guess:
    user_guess = int(input("try again: ")) 
print("congrats, you guessed the right number")

    