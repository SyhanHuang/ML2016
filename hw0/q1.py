import numpy as np
import sys
column = int(sys.argv[1])
input_name = sys.argv[2]
a = np.genfromtxt(input_name, delimiter = " ", dtype = "str")
a = a.astype(float)
b = a[:, column]
b.sort()
b = b.astype(str)
with open("ans1.txt", "w") as out:
	out.write(",".join(map(str, b)))
