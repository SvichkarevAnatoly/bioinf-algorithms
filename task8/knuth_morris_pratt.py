def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k += 1
        v[i] = k
    return v


def search(s, sub):
    index = -1
    f = prefix(sub)
    k = 0
    for i in range(len(s)):
        while k > 0 and sub[k] != s[i]:
            k = f[k - 1]
        if sub[k] == s[i]:
            k += 1
        if k == len(sub):
            index = i - len(sub) + 1
            break
    return index


def main():
    # input from cmd string and substring
    s, sub = raw_input(), raw_input()
    print search(s, sub)


if __name__ == "__main__":
    main()
