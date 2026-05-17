class Solution:

    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        res = ""
        maxLen = 0

        # every single character is palindrome
        for i in range(n):

            dp[i][i] = True

            res = s[i]
            maxLen = 1

        # check substrings
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                # characters match
                if s[i] == s[j]:

                    # length 2 OR inside substring palindrome
                    if length == 2 or dp[i + 1][j - 1]:

                        dp[i][j] = True

                        if length > maxLen:

                            maxLen = length
                            res = s[i:j + 1]

        return res