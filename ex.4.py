# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если 
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите высоту плитки: ")
a = int(input())
print("Введите ширину плитки: ")
b = int(input())
print("Введите сколько долек хотите отломить: ")
c = int(input())

if c<a*b and ((c%a==0 or c%b==0)): 
    print("ок")
else:
    print("NO")