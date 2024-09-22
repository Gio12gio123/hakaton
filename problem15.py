#აიღეთ რაიმე list'ი და დათვლეთ მასში მოცემული რიცხვების საშუალო არითმეტიკული.
list = [13, 17, 6, 4]
average = 0
for i in list:
    average = average + i
print(average / len(list))
