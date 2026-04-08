def permute_and_find_ones(ones_positions, permutation):
    """
    根据置换规则对二进制列表位置进行置换，并输出置换前后列表和数字1所在的位置。

    :param ones_positions: 输入的数字1所在的位置列表（位置从0到31）
    :param permutation: 置换规则（列表形式，表示新的索引顺序）
    :return: 置换前的二进制列表，置换后的二进制列表，以及数字1的新位置列表
    """
    if any(pos < 0 or pos > 31 for pos in ones_positions):
        raise ValueError("输入错误！位置必须在0到31之间。")

    # 构造置换前的二进制列表
    binary_list = [1 if i in ones_positions else 0 for i in range(32)]

    # 根据置换规则调整数字位置
    permuted_list = [binary_list[i] for i in permutation]

    # 找到置换后数字1的位置
    new_ones_positions = [index for index, value in enumerate(permuted_list) if value == 1]

    return binary_list, permuted_list, new_ones_positions


# 设置置换规则（根据需求修改）
permutation = [31, 6, 29, 14, 1, 12, 21, 8, 27, 2, 3, 0, 25, 4, 23, 10, 15, 22, 13, 30, 17, 28, 5, 24, 11, 18, 19, 16, 9, 20, 7, 26]  # 解密

# 输入第一轮数字1的位置和循环轮次
print("请输入第一轮数字1所在的位置（用空格分隔，位置范围为0到31）：")
initial_ones_positions = list(map(int, input().split()))
print("请输入需要循环的轮次数量：")
num_rounds = int(input())

# 初始化当前数字1的位置
current_ones_positions = initial_ones_positions

# 初始化统计变量
total_odd_count_after = 0  # 累计置换后奇数位置的1的总个数

for round_num in range(1, num_rounds + 1):
    # 执行置换
    original_list, permuted_list, new_ones_positions = permute_and_find_ones(current_ones_positions, permutation)

    # 输出当前轮次置换前和置换后的列表
    print(f"第{round_num}轮:")
    print("置换前的列表:", original_list)
    print("置换后的列表:", permuted_list)
    print("数字1置换后的新位置:", new_ones_positions)

    # 统计当前轮次中置换后1在奇数位置的个数
    odd_count_after = sum(1 for pos in new_ones_positions if pos % 2 == 1)
    total_odd_count_after += odd_count_after  # 累加到总奇数计数

    # 根据奇偶规则生成下一轮的输入
    next_ones_positions = []
    seen_positions = set()  # 用于检测重复的位置
    for pos in new_ones_positions:
        if pos % 2 == 0:  # 偶数
            next_ones_positions.append(pos)  # 直接使用偶数位置
        else:  # 奇数
            next_ones_positions.append(pos)  # 加入当前奇数位置
            if pos - 1 >= 0:  # 保证不超出范围
                next_ones_positions.append(pos - 1)  # 该奇数减1后的数作为输入

    # 检测重复的输入位置，并标记 (M)
    next_ones_positions_with_M = []
    seen_positions.clear()
    for pos in next_ones_positions:
        if pos in seen_positions:
            next_ones_positions_with_M.append(f"{pos}(M)")  # 标记为 (M)
        else:
            next_ones_positions_with_M.append(pos)
            seen_positions.add(pos)

    # 排序下一轮的输入位置，确保整数优先，带有(M)的字符串后面
    next_ones_positions_with_M.sort(key=lambda x: (int(str(x).split('(M)')[0]), str(x)))

    # 输出下一轮的输入位置
    print("下一轮的输入位置:", next_ones_positions_with_M)
    print(f"当前轮次置换后1在奇数位置的个数: {odd_count_after}")
    print(f"累计置换后1在奇数位置的总个数: {total_odd_count_after}")
    print()

    # 更新当前数字1的位置
    current_ones_positions = [int(pos.split('(M)')[0]) if isinstance(pos, str) and "(M)" in pos else pos for pos in next_ones_positions_with_M]
1