#შექმენით manual_max() ფუნქცია. ანუ უნდა შექმნათ ისეთი ფუნქცია რომელიც იპოვის მინიმალურ რიცხვს რაიმე list'ში, max() ფუნქციის გამოყენების გარეშე.		

def manual_max(list):
    max=0
    for i in list:
        if i > max:
            max = i
manual_max([1,2,3,4,64])