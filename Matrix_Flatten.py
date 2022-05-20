# create 3d array
n = 3
m = 3
p = 3
threeD_List = []
num3 = 0


# add items to 3d array
for i in range(n):
    threeD_List.append([])

    for j in range(m):
        threeD_List[i].append([])

        for k in range(p):
            threeD_List[i][j].append(num3)
            num3 += 1

# print 3d array
for i in range(n):
    print()
    print()
    for j in range(m):
        print()
        for k in range(p):
            print(threeD_List[i][j][k], end=' ')


# 1D vector suitable for storing 3D matrix
def oneD_size(n,m,p):
	q = n*m*p
	return q

# from 3d to 1d
def ThreeD_To_OneD(i, j, k, n, m, p):
	# achieving O(1)
    index = k + j * n + i * m * p
    return index


# create 1d array
oneD_List = []

# add items to 1d array
for i in range(n):
    for j in range(m):
        for k in range(p):
            oneD_List.append(threeD_List[i][j][k])

# print 1d array
print()
print(oneD_List)

# test 3d to 1 d
def validate_OneD(oneD_List, threeD_List):
	num1 = 0
	s = 0
	print("size of 1D vector= " + str(oneD_size(n,m,p)))
	for i in range(n):
		for j in range(m):
			for k in range(p):
				#print("i = ", s)
				s += 1
				index = ThreeD_To_OneD(i, j, k, n, m, p)
				if not (threeD_List[i][j][k] == oneD_List[index]):
					print("validation failed")
					return False
	
	print("validation passed")
	return True

validate_OneD(oneD_List, threeD_List)











