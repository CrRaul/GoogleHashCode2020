input_file = open("f_libraries_of_the_world.txt", "r")
nr_c, nr_b, nr_z = input_file.readline().strip().split(" ")
score = input_file.readline().strip().split(" ")

B = []
C = []
for i in range(int(nr_b)):
	fL = input_file.readline().strip().split(" ")
	sL = input_file.readline().strip().split(" ")
	B.append(fL)
	C.append(sL)	

zile = []
for i in range(len(B)):
	zile.append(int(B[i][1]))

sumaZile = [zile[0]]
for i in range(1,len(B)):
	sumaZile.append(sumaZile[i-1]+zile[i])

sumaZF = []
for i in range(len(sumaZile)):
	if sumaZile[i] < int(nr_z):
		sumaZF.append(sumaZile[i])

input_file.close()
outputFileName = "world.out"
with open(outputFileName, "w") as out:
	out.write(str(len(sumaZF))+"\n")
	for i in range(len(sumaZF)):
		out.write(str(i) +" "+ str(len(C[i])) +"\n")

		for j in range(len(C[i])):
			out.write(C[i][j]+" ")
		out.write("\n")
		