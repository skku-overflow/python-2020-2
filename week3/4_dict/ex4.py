# dict와 iterator

l = [2, 3, 5, 7, 9, 11, 13, 17, 19]
squared = dict([(i, i * i) for i in l])
print(squared)

print('Keys')
for k in squared.keys():
    print(k)

print('Values')
for v in squared.values():
    print(v)

print('Items')
for k, v in squared.items():
    print(k, v)
