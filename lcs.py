word1="applsdsafsde"
word2="aspdsfasfsddlgpeg"

dp=[[0 for m in range(len(word2)+1)] for n in range(len(word1)+1)]

for i in range(1,len(word1)+1):
	for j in range(1,len(word2)+1):
		# print i,j
		if word1[i-1]==word2[j-1]:
			dp[i][j]=dp[i-1][j-1]+1
		else:
			if dp[i-1][j]>dp[i][j-1]:
				dp[i][j]=dp[i-1][j]
			else :
				dp[i][j]=dp[i][j-1]
		
		# print dp

print dp[len(word1)][len(word2)]
			
