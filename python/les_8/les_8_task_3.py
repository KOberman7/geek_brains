class StrError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        print('Do not input string')

b = []
while True:
    try:
        num = int(input('Input a number: '))
        if type(num) == int:
            b.append(num)
            print(b)
        elif type(num) == str:
            raise StrError
        elif num == stop:
            break
            print(b)
    except ValueError:
        print(StrError)
