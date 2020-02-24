'''
    given a string, check if it is a permutation of a palindrome

    input: Tact Coa
    output: true (taco cat" 也就是忽略空格和大小写区别


    思路：每个元素是不是2的倍数 其中允许一个元素个数为奇数
'''


def check(s):
    dic = {}

    for ch in s:
        if ch in [' ', '\t']: continue
        "".isalnum()
        # ignore low and upper case
        if ch.isupper(): ch = ch.lower()
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    odds = 0
    for k, v in dic.items():
        if v & 1: odds += 1

        if odds > 1: return False

    return True


if __name__ == '__main__':
    print(check("Tact Coa"))
