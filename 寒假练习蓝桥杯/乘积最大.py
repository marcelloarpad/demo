def maximize_product(digits, N, K):
    max_product = 0

    for i in range(1, K + 1):
        prefix = int("".join(map(str, digits[:i])))
        suffix = int("".join(map(str, digits[i:])))
        current_product = prefix * suffix

        if current_product > max_product:
            max_product = current_product

    return max_product

def main():
    # 输入数字串长度 N 和乘号数量 K
    N = int(input("请输入数字串的长度 N："))
    K = int(input("请输入乘号的数量 K："))

    # 输入数字串，假设是一个字符串
    digits_str = input("请输入数字串（不含空格）：")

    # 将字符串转换为数字列表
    digits = [int(digit) for digit in digits_str]

    # 求解最大乘积
    result = maximize_product(digits, N, K)

    print(f"最大乘积为：{result}")

if __name__ == "__main__":
    main()
