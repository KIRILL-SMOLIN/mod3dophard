    #  Дополнительное практическое задание по модулю: "Подробнее о функциях."

def razbor(i):
    global sum1
    if isinstance(i, int):
        sum1 += i
    if isinstance(i, float):
        sum1 += i
    if isinstance(i, list):
        spis_kort_mnozh(i)
    if isinstance(i, str):
        sum1 += len(i)
    if isinstance(i, dict):
        slovar(i)
    if isinstance(i, tuple):
        spis_kort_mnozh(i)
    if isinstance(i, set):
        spis_kort_mnozh(i)
    return

def spis_kort_mnozh(spis):
    for i1 in spis:
        razbor(i1)
    return

def slovar(dict1):
    spis_kort_mnozh(dict1.keys())
    spis_kort_mnozh(dict1.values())
    return

def calculate_structure_sum(list_):
    global sum1
    sum1=0
    for j in list_:
        razbor(j)
    return sum1


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)