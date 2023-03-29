


trips = [[2,1,5],[3,3,7]]
capacity = 4


trips2 = []
for c, x, y in trips:
    trips2.append((x,c))
    trips2.append((y,-c))

trips2
# trips2.sorted(key = lambda (x,y): )

trips2 = sorted(trips2)


passages = 0
for (location, number) in trips2:
    passages += number
    if passages > capacity:
        print(passages)
        break


