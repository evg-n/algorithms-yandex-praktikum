def match(p, s):
    n = len(s)

    def re_match(p_idx, s_idx):
        if p_idx == len(p) and s_idx == n:
            return True
        elif s_idx == n or p_idx == len(p):
            return False

        if p[p_idx] == "*":
            for i in range(s_idx, n + 1):
                if re_match(p_idx + 1, i):
                    return True
            return False
        elif p[p_idx] == "?":
            return re_match(p_idx + 1, s_idx + 1)
        elif p[p_idx] == s[s_idx]:
            return re_match(p_idx + 1, s_idx + 1)

        return False

    return re_match(0, 0)


def match_dp(p, s):
    n, m = len(p), len(s)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    # Note: we only need prev and cur lines in the dp. Memory usage could be improved

    for i, pch in enumerate(p, start=1):
        early_exit = True
        if pch == "*":
            for j in range(m + 1):
                if dp[i - 1][j] or dp[i][j - 1]:
                    dp[i][j] = True
                    early_exit = False
        else:
            for j, sch in enumerate(s, start=1):
                if dp[i - 1][j - 1] and (pch == "?" or sch == pch):
                    dp[i][j] = True
                    early_exit = False
        if early_exit:
            return False
    return dp[-1][-1]


if __name__ == "__main__":
    p = input()
    s = input()
    print("YES" if match_dp(p, s) else "NO")
