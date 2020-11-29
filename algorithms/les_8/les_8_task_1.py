'''Определение количества различных подстрок с использованием хеш-функции.'''

S = 'sova'

print(f"Строка {S} имеет длину {len(S)} сиволов.")

subs_set = set()

for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))

print("Количество различных подстрок в этой строке:", len(subs_set))
