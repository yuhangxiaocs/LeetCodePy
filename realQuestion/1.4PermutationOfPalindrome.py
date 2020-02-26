'''
    given a string, check if it is a permutation of a palindrome

    input: Tact Coa
    output: true (taco cat" 也就是忽略空格和大小写区别


    思路：每个元素是不是2的倍数 其中允许一个元素个数为奇数

    Solution
    答案思路就是这样

    有个小的优化 就是可以在第一遍循环的时候就算出结果 思路是这样：如果对于x 加到dic[x]的次数上面 然后如果是奇数 就odd++
    否则odd-- 最终看odd <= 1即可 这样可以省去最后一个循环 但是在第一个循环中引入了多余的操作 时间复杂度还是没变 只是形式上好看了一些
    甚至在实际中更慢也是可能的
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
