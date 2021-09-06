print('input first object')
x = int(input())
print('input last object')
y = int(input())
print('duration time years or month')
w = int(input())

a1 = 1 / w

h1 = y / x
h2 = h1 ** a1
h3 = h2 - 1
h4 = h3 * 100
h5 = round(h4,2)
print(f'{h5} %')