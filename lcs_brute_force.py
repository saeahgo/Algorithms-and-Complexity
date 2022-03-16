import timeit # to measure the execution time

# Function to find the longest common subsequence of string `X[0…m-1]` and `Y[0…n-1]`
def LCSBF(X, Y, m, n, lookup):

	# return an empty string if the end of either sequence is reached
	if m == 0 or n == 0:
		return str()

	# if the last character of `X` and `Y` matches
	if X[m - 1] == Y[n - 1]:
		# append current character (`X[m-1]` or `Y[n-1]`) to LCS of
		# substring `X[0…m-2]` and `Y[0…n-2]`
		return LCSBF(X, Y, m - 1, n - 1, lookup) + X[m - 1]

	# otherwise, if the last character of `X` and `Y` are different

	# if a top cell of the current cell has more value than the left
	# cell, then drop the current character of string `X` and find LCS
	# of substring `X[0…m-2]`, `Y[0…n-1]`

	if lookup[m - 1][n] > lookup[m][n - 1]:
		return LCSBF(X, Y, m - 1, n, lookup)
	else:
		# if a left cell of the current cell has more value than the top
		# cell, then drop the current character of string `Y` and find LCS
		# of substring `X[0…m-1]`, `Y[0…n-2]`
		return LCSBF(X, Y, m, n - 1, lookup)


# Function to fill the lookup table by finding the length of LCS
# of substring `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y, m, n, lookup):

	# fill the lookup table in a bottom-up manner
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			# if current character of `X` and `Y` matches
			if X[i - 1] == Y[j - 1]:
				lookup[i][j] = lookup[i - 1][j - 1] + 1
			# otherwise, if the current character of `X` and `Y` don't match
			else:
				lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


if __name__ == '__main__':

	X = []
	Y = []

	X = input("Enter a string: ")
	Y = input("Enter another string: ")

	m = len(X)
	n = len(Y)

	start = timeit.default_timer()	

	# lookup[i][j] stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
	lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]
	
	# fill lookup table
	LCSLength(X, Y, m, n, lookup)
	
	# find the longest common subsequence
	maxseq = LCSBF(X, Y, m, n, lookup)
	end = timeit.default_timer()

	# Printing the subsequences
	print("X : " + X + "\nY : " + Y)
	print("LCS w/ Brute Force length is:", len(maxseq))
	print("LCS w/ Brute force is: ", maxseq)
	print("Running time: ", end - start)
