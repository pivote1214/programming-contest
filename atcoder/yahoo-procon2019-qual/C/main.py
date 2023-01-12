#!/usr/bin/env python3
import sys


def solve(K: int, A: int, B: int):
    if A >= B - 2:
        ans = K + 1
    else:
        if K <= A - 1:
            ans = K + 1
        else:
            ans = (B - A) * ((K - A + 1) // 2) + ((K - A + 1) % 2) + A

    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(K, A, B)

if __name__ == '__main__':
    main()