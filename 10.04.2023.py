import re

tell = (
    '''
    +3720631234567
    +381231234567
    +372321234567
    +375921234567
    +81231234567
    +3331231234567
    +1111231234567
    +380501231231
    '''
)

def num(tell: str) -> None:
    res1 = re.findall(r"[+]?\d{8,15}", tell)
    return res1

def ukr_num(res1) -> None:
    ukr = []
    for phone in res1:
        if res1[:3] == '+38':
            ukr.append(phone)
    return ukr

def phones_handler(
    phones: list,
    before: None = num,
    action: None = ukr_num
) -> None:
    for phone in phones:
        before(phone)
        action(phone)
