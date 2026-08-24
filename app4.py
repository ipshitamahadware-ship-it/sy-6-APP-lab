def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = ""
    i = m
    j = n

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

result = longest_common_subsequence(X, Y)

print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))