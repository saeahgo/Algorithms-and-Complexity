# The longest common subsequence in Python
import timeit # to measure the execution time

def LCSDP(S1, S2, m, n):
	L = [[0 for x in range(n+1)] for x in range(m+1)]

	# Building the matrix in bottom-up way
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif S1[i-1] == S2[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	index = L[m][n]

	LCSDP = [""] * (index+1)
	LCSDP[index] = ""

	i = m
	j = n
	while i > 0 and j > 0:

		if S1[i-1] == S2[j-1]:
			LCSDP[index-1] = S1[i-1]
			i -= 1
			j -= 1
			index -= 1

		elif L[i-1][j] > L[i][j-1]:
			i -= 1
		else:
			j -= 1
			
	# Printing the subsequences
	print("X : " + X + "\nY : " + Y)
	print("LCS w/ Dynamic Programming length is:", len(LCSDP)-1)
	print("LCS w/ Dynamic Programming is: " + "".join(LCSDP))

X = []
Y = []

X = input("Enter a string: ")
Y = input("Enter another string: ")

m = len(X)
n = len(Y)

start = timeit.default_timer()
LCSDP(X, Y, m, n)
end = timeit.default_timer()

print("Running time: ", end - start)