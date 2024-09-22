#შექმენით calculator ფუნქცია რომელსაც ექნება ყველა მათემატიკური მოქმედება მაგალითად:+,-,*,/. ფუნქციას გადაეცით 3 არგუმენტი. პირველი იქნება პირველი რიცხვი, მეორე მეორე რიცხვი და მესამე მათემატიკური ოპერაციის ოპერატორი (+,-...).		
def calculator(a,b,operator):
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    operator = input("enter operation: ")
    if operator == "add":
        return a + b
    elif operator == "minus":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "division":
        return a / b 

print(calculator(55,20,"add"))





