print('How much beer can you drink? ')
def categorize_number(number):
    if number == 0:
        category = "You eat grass for a living"
    elif 1 <= number <= 3:
        category = "You are a noob"
    elif 4 <= number <= 8:
        category = "You are a decent human being"
    elif 9 <= number <= 12:
        category = "Living Large!"
    else:
        category = "You need help"
    return category

number = int(input("Enter the number of beers per day: ))
category = categorize_number(number)

print("Enter the amount of beers per day")

