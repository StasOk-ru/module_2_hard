# Задание "Слишком древний шифр":

import random
n = random.randint(3, 20)
print('Случайное число', n)

result = []
app = []

for i in range(1, n+1):

    for j in range(1, n+1):

        if n % (i + j) == 0 and i != j and i < j:
            app.append(i)
            app.append(j)
            #print(f'Пара {i} - {j} кратна {n}')
            result.append(app)
            #print('добавлена пара',app)
        app = []
print('список подходящих пар',result)
