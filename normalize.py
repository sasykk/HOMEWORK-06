import re
UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
ENGLISH_SYMBOLS = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")
TRANS = {}
for key, value in zip(UKRAINIAN_SYMBOLS, ENGLISH_SYMBOLS):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()

def normalize(name: str) -> str:
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', '_', new_name)
    return f"{new_name}.{'.'.join(extension)}" if extension else new_name

if __name__ == '__main__':
    example_name = 'Jh0ю5я_ghВlд0kБ.ykk'
    print(normalize(example_name))
