def brief_case(brand, color, combination):
    briefcase = {
        'Brand':brand,
        'Color':color,
        'Combination':combination,
        }
    return briefcase

user_brand = input('What brand briefcase do you have? ')
user_color = input('What color is it? ')
user_combination = input('What is the combination to lock it? ')


def display_briefcase(briefcase):
    for key, value in briefcase,items():
        print(key + ": " + value)
    print("\n")
    return display_briefcase
print (display_briefcase)

x = brief_case(user_brand, user_color, user_combination)
print (x)

    

