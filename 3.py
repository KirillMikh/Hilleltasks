class BracketChecker:

    def __init__(self):
        self.string1 = input("Введите скобочную последовательность ")

    def checker(self):
        str1 = self.string1
        if '()' in str1 or '[]' in str1 or '{}' in str1 or '<>'in str1:
            str1 = str1.replace('()', '')
            str1 = str1.replace('[]', '')
            str1 = str1.replace('{}', '')
            str1 = str1.replace('<>','')
            self.string1 = str1
            if len(str1) !=0:
                return self.checker()
            else:
                return "Правильная скобочная последовательность"
        else:
            return "Неравильная скобочная последовательность"


checker1 = BracketChecker()
print(checker1.checker())

# <><><>()()  Правильная
# [[}()]]  Неправильная
# ({[<>]}) Правильная
