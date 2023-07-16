number = [1,2,-3,4,-5,6, 0]
def new_number(number: int) -> None:
    print(f"is num: {number}")
def is_positive(number: int) -> None:

    if number > 0:
        print(f"{number}    positive ")
    elif number < 0:
        print(f"{number}    negative")
    else:
        print('Zero')
def print_bye(number: int) -> None:
    print('Bye!', end='\n\n')
def numbers_handler (
        numbers: list,
        before: None = new_number,
        action: None = is_positive,
        after: None = print_bye
) -> None:
    for number in numbers:
        before(number)
        action(number)
        after(number)

numbers_handler(number)


