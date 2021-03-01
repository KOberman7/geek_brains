#Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
import cProfile
import timeit

#1
s = '''
if year % 4 == 0:
    print(f'{year} високосный')
elif year % 100 != 0:
    if year % 400 == 0:
        print(f'{year} високосный')
else:
    print(f'{year} не високосный')'''
year = 2000
print(timeit.timeit('s', number=100, globals=globals())) #1.0200000000001874e-05
year = 2019
print(timeit.timeit('s', number=100, globals=globals())) #6.3000000000007494e-06
year = 1984
print(timeit.timeit('s', number=100, globals=globals())) #5.800000000000249e-06
cProfile.run('s')
#3 function calls in 0.000 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
     #   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('***')

#2
def vis(n):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False

print(vis(year))
year = 2000
print(timeit.timeit('vis(year)', number=100, globals=globals())) #6.369999999999987e-05
year = 2019
print(timeit.timeit('vis(year)', number=100, globals=globals())) #3.6099999999997245e-05
year = 1984
print(timeit.timeit('vis(year)', number=100, globals=globals())) #4.859999999999587e-05
cProfile.run('vis(2000)')
#4 function calls in 0.000 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     #   1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(vis)
      #  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('vis(2019)')
#4 function calls in 0.000 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     #   1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(vis)
      #  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('vis(1984)')
#4 function calls in 0.000 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #    1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(vis)
     #   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      #  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('***')
#3
p = '''
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')'''
year = 2000
print(timeit.timeit('p', number=100, globals=globals())) #6.3000000000007494e-06
year = 2019
print(timeit.timeit('p', number=100, globals=globals())) #6.199999999997874e-06
year = 1984
print(timeit.timeit('p', number=100, globals=globals())) #5.800000000000249e-06

cProfile.run('p')
#3 function calls in 0.000 seconds

   #Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     #   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      #  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: 3-й алгоритм работает быстрее всех