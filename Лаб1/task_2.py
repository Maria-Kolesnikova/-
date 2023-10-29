# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024
page = 100
line = 50
sym = 25
el = 4

result1 = page * line * sym * el
result2 = int(disk // result1)
print("Количество книг, помещающихся на дискету:", result2)
