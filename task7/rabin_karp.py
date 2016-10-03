p = 101  # god number


def code(c):
    return ord(c)


def hash_rk(q):
    res = 0
    for qi in q:
        res = res * p + code(qi)
    return res


def hash_rk_update(hash_old, len_sub, letter_old, letter_new):
    return (hash_old - code(letter_old) * p ** (len_sub - 1)) * p \
           + code(letter_new)


def search(s, sub):
    len_sub = len(sub)

    hash_sub = hash_rk(sub)
    hash_s_sub = hash_rk(s[:len_sub])

    for i in range(0, len(s) - len_sub):
        if hash_s_sub == hash_sub:
            if s[i:i + len_sub] == sub:
                return i
        hash_s_sub = hash_rk_update(hash_s_sub, len_sub,
                                    s[i], s[i + len_sub])
    if hash_s_sub == hash_sub:
            if s[len(s) - len_sub:] == sub:
                return len(s) - len_sub
    return -1


def main():
    # input from cmd string and substring
    s, sub = raw_input(), raw_input()
    print search(s, sub)


if __name__ == "__main__":
    main()
