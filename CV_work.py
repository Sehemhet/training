# import re
#
# text = 'GOOGLE google гугл 1234546'
#
# result1 = re.findall(r'[0-9]\d+', text)
# result2 = re.findall(r'[a-z,A-Z]\w+', text)
# result3 = re.findall(r'[A-Z]\w+', text)
#
#
# print(result1)
# print(result2)
# print(result3)



number_list = [3, 7, 4, 2, 9]

def create_new_num_list(num_list):
    result1 = []
    result2 = []
    for i in num_list:
        if i % 2 == 0:
            result1.append(i)
        elif i % 2 != 0:
            result2.append(i)
    return f'парные числа: {result1}\nне парные числа:{result2}'

print(f"исходные данные: {number_list}")
print(create_new_num_list(number_list))



