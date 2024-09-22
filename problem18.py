#შექმენით manual_min() ფუნქცია. ანუ უნდა შექმნათ ისეთი ფუნქცია რომელიც იპოვის მინიმალურ რიცხვს რაიმე list'ში, min() ფუნქციის გამოყენების გარეშე.


def manual_min(list):
    min = list[0]
    for i in list:
        if min > i:
            min = i
    print(min)
manual_min([1,2,3,4,64])