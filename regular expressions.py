import re
#training regular expressions
t1 = 'war wait you in game - world of warcraft'
w = 'Abc, abc, abC, abcd, abcde, 5, 55, 12345'
l = 'lol, lool, loool, looool'
#training regular expressions
res = re.findall('war', t1)
print(res)
res = re.findall('''\\bwar\\b''', t1)
print(f'string 9: use "\\b___\\b" give independent word {res}')     #\\b___\\b
res = re.findall(r'\bwar\b', t1)
print(f'string 13: use "r"\\b___\\b"" give independent word {res}')  #r'\b___\b'
res = re.findall(r'[Aa]b[cC]', w)
print(f'string 16: use "[Aa]b[cC]" {res}')                          #r'[Aa]b[Cc]'
res = re.findall(r'\b[Aa]b[cC]\b', w)                               #r'\b[Aa]b[Cc]\b'
print(f'string 18: "\\b[Aa]b[Cc]\\b"___{res}')
res = re.findall(r'[5][5]', w)                                      #r'[5][5]'
print(f'string 20: "[5][5]" find one num {55}')
res = re.findall(r'[5]', w)                                         #r'[5]'
print(f'string 22: [5] find everuone symbol {res}')
res = re.findall(r'\b[5]\b', w)                                     #r'\b[5]\b'
print(f'string 24: "\\b[5]\\b" find independent num {res}')
res = re.findall(r'\b[3-5][3-5]\b', w)                              #\d everyone num
print(f'string: 23 "\\b[3-5][3-5]\\b" will be independent num between 3-5 __ {res}')
res = re.findall(r'[^1-5]', w)                                      #\D no one num
print(f'string 25: {res} will all whiout choice num')               #\w every words \W no one words
res = re.findall(r'.', w)                                           # "." all symbols
print(f'string 27: all symbols "." will {res}')
res = re.findall(r'\w', w)
print(f'string 27: "\w" {res}')                                     ##\w every words \W no one words
res = re.findall(r'o{2,3}', l)                                      # all letter 'o' detween 2-3
print(f'string 32: {res} "r{2,3}"')
res = re.findall(r'o{2,3}?', l)                                      # all letter 'o' detween 2-3
print(f'string 34: {res} "r{2,3}?"')                                 #минорный режим

# краткие формы квантификатора
# {,3},{3,}{3}  {,3}? {3,}?
res = re.findall(r'lo{,2}l', l)
print(f'string 39: {res} до двух символов О')
res = re.findall(r'lo{2,}l', l)
print(f'string 41: {res} от двух символов О')

num = '812345678'
res = re.findall(r'8\d{8}', num)
print(res)
res = re.findall(r'looo?l', l)                                      # r'looo?l'
print(f' sring 47{res}')

text = "author=Пушкин A.C.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)
d = text.split (";")
print(d)

text = "«р>Картинка <img src='bg.jpg'> в тексте</р>"
mat = re.findall (r"<img.*>", text)
print(f'string :57 {mat}')
mat = re.findall(r'<img.*?>', text)           # *?> все до >
print(f'string :59 {mat}')
mat = re.findall(r'<img.[^>]*>', text)        # [^>]*> все до >
print(f'string :61 {mat}')
mat = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]+>', text)
print(f'string :63 {mat}')
# \s символьный класс пробелов
# \w символьный класс соответсвуюзий слову
# + квантификатор, символов от 1 до скольки есть
# * может быть от нуля и более
#  [^>] все до > [^;] все до ;
#   *?> ? - минорный квантификатор, то есть все значения до первого >
#   [^>]*> все до >
text = "lat = 5, lon=7"
mat = re.findall(r"\w+\s*=\s*\d+", text)
print(mat)
mat = re.findall(r'lat\s*=\s*\d+|lon\s*=\s*\d+', text)
print(f'string 75 {mat}')

mat = re.findall(r'(lat|lon)\s*=\s*\d+', text)
print(f'string 78 {mat}')
mat = re.findall(r'(lat|lon)\s*=\s*(\d+)', text)
print(f'string 80 {mat}')

text = "‹р>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text)
print(match)

text = "ход, доход, ходдог, ходор]"
match = re. findall(r"прибыль |обретение |доход", text)
print(match)
text = "ход, доход, ходдог, ходор]"
match = re. findall(r"фыв |ячс |\bдоход\b", text)
print(match)
text = "ход, доход, ходдог, ходор]"
match = re. findall(r"(фыв |ячс |\bдоход\b)", text)
print(match)
text = "ход, доход, ходдог, ходор]"
match = re. findall(r"\b(фыв|ячс|доход)\b", text)
print(match)

text = "Lol, lol, LOL"
match = re.findall(r"(?im)lol", text)
print(f'string 101 whitout "i" will {match}')

text = "Lol, lol, LOL"
match = re.findall(r"(?m)lol", text)
print(f'string 105 with "i" will {match}')


text = " +7 (123)456-78-90"
m = re.match (r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

text = "+38(063)474-36-94"
m = re.match (r"[+]?38\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

text = "38(063)474-36-94"
m = re.match (r"[+]?38\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

text = "-38(063)474-36-94"
m = re.findall(r"[+]?38\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

q1 = '+38(063)123-45-67 +38(097)123-45-67 +38(093)123-23-23 38(063)111-22-33 +38(050)123-23-23'
life = re.findall(r'[+]?38\([0][6|9][3]\)\d{3}-\d{2}-\d{2}', q1)
mtc = re.findall(r'[+]?38\([0][5|6][0|6]\)\d{3}-\d{2}-\d{2}', q1)

print(f"{life}{mtc}", sep='\n')


text = 'JNKNJNF лойутййт 349124 jnfe'

result1 = re.findall(r'[A-Z,a-z]\w+', text)
result2 = re.findall(r'[0-9]\d+', text)
result3 = re.findall(r'[A-Z]\w+', text)

print(result1)
print(result2)
print(result3)