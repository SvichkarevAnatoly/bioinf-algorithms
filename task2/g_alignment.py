# coding=utf-8

# parameters for algorithm
d = 1
# change to constant for same penalty for mismatch
m = {
    'A': {'A': 5, 'R': -2, 'N': -1, 'K': -1},
    'R': {'A': -2, 'R': 7, 'N': -1, 'K': 3},
    'N': {'A': -1, 'R': -1, 'N': 7, 'K': 0},
    'K': {'A': -1, 'R': 3, 'N': 0, 'K': 6},
}


def lcs_backtrack(v, w):
    v_len = len(v)
    w_len = len(w)
    s = [[0] * (w_len + 1) for _ in range(v_len + 1)]
    backtrack = [[0] * w_len for _ in range(v_len)]

    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            s[i][j] = max(
                s[i - 1][j] - d,
                s[i][j - 1] - d,
                s[i - 1][j - 1] + m[v[i - 1]][w[j - 1]]
            )

            if s[i][j] == s[i - 1][j] - d:
                backtrack[i - 1][j - 1] = '↓'
            elif s[i][j] == s[i][j - 1] - d:
                backtrack[i - 1][j - 1] = '→'
            elif s[i][j] == s[i - 1][j - 1] + m[v[i - 1]][w[j - 1]]:
                backtrack[i - 1][j - 1] = '↘'
    return backtrack, s[v_len][w_len]


def output_lcs(backtrack, v, w, i, j, align):
    while i >= 0 and j >= 0:
        if backtrack[i][j] == '↘':
            align[v].append(v[i])
            align[w].append(w[j])
            i -= 1
            j -= 1
        elif backtrack[i][j] == '↓':
            align[v].append(v[i])
            align[w].append('-')
            i -= 1
        else:
            align[v].append('-')
            align[w].append(w[j])
            j -= 1

    while j < 0 <= i:
        align[v].append(v[i])
        align[w].append('-')
        i -= 1
    while i < 0 <= j:
        align[v].append('-')
        align[w].append(w[j])
        j -= 1
    align[v].reverse()
    align[w].reverse()
    align[v] = "".join(align[v])
    align[w] = "".join(align[w])


def alignment_str(align, v, w, score):
    return align[v] + '\n' + \
           align[w] + '\n' + \
           "score = " + str(score)


def alignment(v, w):
    backtrack, score = lcs_backtrack(v, w)
    align = {v: [], w: []}
    v_last, w_last = len(v) - 1, len(w) - 1
    output_lcs(backtrack, v, w, v_last, w_last, align)
    return align, score


def output_alignment(v, w):
    align, score = alignment(v, w)
    return alignment_str(align, v, w, score)


def main():
    # input from cmd
    # v, w = raw_input(), raw_input()
    v, w = "AKRANR", "KAAANK"
    print output_alignment(v, w)


if __name__ == "__main__":
    main()
