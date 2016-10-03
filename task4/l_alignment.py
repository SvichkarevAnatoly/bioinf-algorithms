# coding=utf-8

# parameters for algorithm
d = 1
m = 1


def lcs_backtrack(v, w):
    v_len = len(v)
    w_len = len(w)
    s = [[0] * (w_len + 1) for _ in range(v_len + 1)]
    backtrack = [[0] * w_len for _ in range(v_len)]

    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            s[i][j] = max(
                0,
                s[i - 1][j] - d,
                s[i][j - 1] - d,
                s[i - 1][j - 1] + (1 if v[i - 1] == w[j - 1] else -m)
            )

            if s[i][j] == s[i - 1][j] - d:
                backtrack[i - 1][j - 1] = '↓'
            elif s[i][j] == s[i][j - 1] - d:
                backtrack[i - 1][j - 1] = '→'
            elif s[i][j] == s[i - 1][j - 1] + (1 if v[i - 1] == w[j - 1] else -m):
                backtrack[i - 1][j - 1] = '↘'

    v_max_ind = w_max_ind = 1
    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            if s[v_max_ind][w_max_ind] < s[i][j]:
                v_max_ind, w_max_ind = i, j

    return backtrack, s, (v_max_ind, w_max_ind)


def output_lcs(backtrack, s, v, w, i, j, align):
    while i >= 0 and j >= 0 and s[i + 1][j + 1] != 0:
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

    align[v].reverse()
    align[w].reverse()
    align[v] = "".join(align[v])
    align[w] = "".join(align[w])


def alignment_str(align, v, w, score):
    return align[v] + '\n' + \
           align[w] + '\n' + \
           "score = " + str(score)


def alignment(v, w):
    backtrack, s, (v_max_ind, w_max_ind) = lcs_backtrack(v, w)
    score = s[v_max_ind][w_max_ind]

    align = {v: [], w: []}
    output_lcs(backtrack, s, v, w, v_max_ind - 1, w_max_ind - 1, align)
    return align, score


def output_alignment(v, w):
    align, score = alignment(v, w)
    return alignment_str(align, v, w, score)


def main():
    # input from cmd
    v, w = raw_input(), raw_input()
    print output_alignment(v, w)


if __name__ == "__main__":
    main()
