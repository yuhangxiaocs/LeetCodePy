'''

    input: aabcccccaaa
    output:a2b1c5a3

    if len(output) > len(input) return input instead
'''


def compression(input):
    res = []
    i = 0
    while i < len(input):

        cur = input[i]
        count = 1
        res.append(str(cur))

        while i + 1 < len(input) and input[i + 1] == input[i]:
            i += 1
            count += 1
        res.append(str(count))

        i += 1

    res = "".join(res)

    return res if len(res) < len(input) else input


if __name__ == '__main__':
    print(compression("aabcccccaaa"))
