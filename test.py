data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]


min_valid = 100
max_valid = 200

stop= 0
for i , j in enumerate(data):
        if j >= min_valid:
                stop = i
                break
print(stop)
del data[:stop]
print(data)


