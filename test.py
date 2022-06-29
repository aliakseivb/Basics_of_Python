def gen_range (start, stop, step): # функция генератор
    rez = start
    lst = []
    while rez <= stop:
        # print(f'\t\t Перед yeild')
        lst.append(rez)
        yield rez, lst # в этом месте функция запоминает свой итератор и заканчивает один проход возвращая найденное значение
        # print(f'\t\t После yeild')
        rez += step

gen1 = gen_range(1, 10, 2)
for x in gen1:
    print(x)
