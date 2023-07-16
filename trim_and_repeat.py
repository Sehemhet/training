def cut_rep (text, offset=0, repetitions=1):
    if offset < len(text):
        return f"{text[offset:] * repetitions}"
    else:
        return f'text was short or offset big'

text = 'python'
print(cut_rep(text, 3, 3))

text1 = 'samsung'
print(cut_rep(text1,5,5))

t2 = 'победа'
print(cut_rep(t2,2,2), sep='+')

# t3 = str(input(f'Введите текст:_ '))
# a, b = map(int,input(f"введите offset:_ и repetitions_ через пробел ").split())
# print(cut_rep(t3,a,b))


# this is predicat
def is_mister(string):
    return string == "Mister"

#кратное или не кратное число. обыкновенная функция
def is_even(number):
    return number % 2 == 0

print(is_even(10))  # => True
print(is_even(3))   # => False


def is_first_letter_an_a(string):
    first_letter = string[0]
    return first_letter == 'a'

print(is_first_letter_an_a('orange'))  # => False
print(is_first_letter_an_a('apple'))   # => True

print(is_mister('Mister'))

#проверка высокосного года
def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

#проверка слово на полидром

def is_palindrome(word):
    w = word.lower()
    return w == w[::-1]

def is_not_palindrome(word):
    w = word.lower()
    return w != w[::-1]

def is_not_palindrome(word):
    return not is_palindrome(word)

#проверка пароля
def is_correct_password(password):
    length = len(password)
    return length > 8

print(is_correct_password('Qwerйцйцty'))

#проверка полученого адреса
def normalize_url(url):
    start_url = 'https://'
    if url[:8] == start_url:
        return url
    else:
        if url[:7] == 'http://':
            return start_url + url[7:]
        else:
            return start_url + url

print(normalize_url('http://google.com'))

#
# На электронной карте Вестероса, которую реализовал Сэм, союзники Старков отображены зелёным кружком, враги — красным, а нейтральные семьи — серым.
#
# Напишите для Сэма функцию who_is_this_house_to_starks(), которая принимает на вход фамилию семьи и возвращает одно из трёх значений: 'friend', 'enemy', 'neutral'.

def who_is_this_house_to_starks(l_name):
    friend = ['Karstark','Tully']
    enemy = ['Lannister','Frey']
    if l_name in friend:
        return 'friend'
    elif l_name in enemy:
        return 'enemy'
    else:
        return 'neutral'

def who_is_this_house_to_starks(house_name):
    if house_name == 'Karstark' or house_name == 'Tully':
        return 'friend'
    elif house_name == 'Lannister' or house_name == 'Frey':
        return 'enemy'
    return 'neutral'
#Тернарный оператор

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question


#59

# Тернарный оператор — способ превратить простую условную инструкцию в выражение, например, number if number >= 0 else -number.


def flip_flop(string):
    return 'flop' if string == 'flip' else 'flip'


def get_number_explanation(count):
    match count:
        case 666:
            return 'devil'
        case 13:
            return 'bad'
        case 11:
            return 'twin_tour'
        case _:
            return None

print(get_number_explanation(13))

#count
def print_numbers(last_number):
    # i сокращение от index (порядковый номер)
    # используется по общему соглашению во множестве языков
    # как счетчик цикла
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')

print_numbers(3)
# => 1
# => 2
# => 3
# => finished!

def print_numbers(numbers):
    i = numbers
    while i > 0:
        print(i)
        i-=1
    print('finished!')

print(print_numbers(9))

#function
def multiply_numbers_from_range(st, fin):
    i = st
    result = 1
    while i <= fin:
        result = result * i
        i += 1
    return result
print(multiply_numbers_from_range(2,8)*10000)

def work_time(result, time):
    i = 1
    while i <= time:
        result *= 2
        i += 1
    return result
print(work_time(20000,5)+20000)

#
def join_numbers_from_range(start, end):
    i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result

print(join_numbers_from_range(1,5))

def print_reversed_word_by_symbol(name):
    i = len(name) - 1
    while i >= 0:
        print(name[i])
        i = i - 1

print(print_reversed_word_by_symbol('Volk'))

#
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].lower() == char.lower():
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count

text = 'in here will be text and latters what i need to find'
print(count_chars(text, "t"))

def filter_string(text, char):
    index = 0
    result = ''
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result = f'{result}{current_char}'
        index += 1
    return result

t1 = 'in here will be text and latters what i need to find'
print(filter_string(t1, 't'))

#цикл фор

def reverse_string(text):
    # Начальное значение
    result = ''
    # char - переменная, в которую записывается текущий символ
    for char in text:
        # Соединяем в обратном порядке
        result = char + result
    # Цикл заканчивается, когда пройдена вся строка
    return result


print(reverse_string('go!'))  # => '!og'


def get_hidden_card(card_number, stars_count=4):
    visible_digits_line = str(card_number)[-4:]
    return f"{'*' * stars_count}{visible_digits_line}"


card_num1 = 2034399002121100
card_num2 = 78137412901
card_num3 = 89413084102
card_num4 = 7325974021481974
print(get_hidden_card(card_num1, 2))
print(get_hidden_card(card_num2, 3))
print(get_hidden_card(card_num3, 4))
print(get_hidden_card(card_num4, 5))