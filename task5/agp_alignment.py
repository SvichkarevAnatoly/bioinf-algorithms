# coding=utf-8
from copy import deepcopy

match = 5
m = 1
p = 11
d = 1


def score(vi, wj):
    return match if vi == wj else -m


def lcs_backtrack(v, w):
    v_len = len(v)
    w_len = len(w)

    backtrack = [[0] * w_len for _ in range(v_len)]

    middle = [[0] * (w_len + 1) for _ in range(v_len + 1)]
    lower = deepcopy(middle)
    upper = deepcopy(middle)

    for i in range(1, w_len + 1):
        lower[0][i] = -p
    for i in range(1, v_len + 1):
        upper[i][0] = -p

    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            lower[i][j] = max(
                lower[i - 1][j] - d,
                middle[i - 1][j] - p
            )

            upper[i][j] = max(
                upper[i][j - 1] - d,
                middle[i][j - 1] - p
            )

            middle[i][j] = max(
                lower[i][j],
                middle[i - 1][j - 1] + score(v[i - 1], w[j - 1]),
                upper[i][j]
            )

            if middle[i][j] == lower[i][j]:
                backtrack[i - 1][j - 1] = "↓"
            elif middle[i][j] == upper[i][j]:
                backtrack[i - 1][j - 1] = "→"
            elif middle[i][j] == middle[i - 1][j - 1] + score(v[i - 1], w[j - 1]):
                backtrack[i - 1][j - 1] = "↘"
    return backtrack, middle[v_len][w_len]


def output_lcs(backtrack, v, w, alignment):
    i, j = len(v) - 1, len(w) - 1
    while j >= 0:
        if backtrack[i][j] == "↘":
            alignment[v].append(v[i])
            alignment[w].append(w[j])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            alignment[v].append(v[i])
            alignment[w].append('-')
            i -= 1
        else:
            alignment[v].append('-')
            alignment[w].append(w[j])
            j -= 1
    alignment[v].reverse()
    alignment[w].reverse()
    alignment[v] = "".join(alignment[v])
    alignment[w] = "".join(alignment[w])


def alignment_str(align, v, w, score):
    return align[v] + '\n' + \
           align[w] + '\n' + \
           "score = " + str(score)


def alignment(v, w):
    backtrack, score = lcs_backtrack(v, w)
    align = {v: [], w: []}
    output_lcs(backtrack, v, w, align)
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
