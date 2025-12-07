
scores = [5, 4, 5, 3]
for s in scores:
    print("оценка:", s)


for i in range(5):  # 0,1,2,3,4 — пять раз
    print("шаг", i)


for ch in "hello":
    print(ch)



names = ["Оля", "Кирилл", "Ира"]
scores = [10, 8, 9]
for name, score in zip(names, scores):
    print(name, "получил", score)


for x in range(2, 11, 2):  # 2,4,6,8,10
    print(x)