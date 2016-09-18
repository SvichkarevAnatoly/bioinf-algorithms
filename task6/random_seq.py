import random

nucleotides = ['A', 'C', 'G', 'T']
ranges = [100, 1000, 100000]


def main():
    # input from cmd
    # n = int(raw_input())
    for n in ranges:
        print ''.join(random.choice(nucleotides) for _ in range(n))


if __name__ == "__main__":
    main()
