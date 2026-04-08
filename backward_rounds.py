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
#permutation = [31, 6, 29, 14, 1, 12, 21, 8, 27, 2, 3, 0, 25, 4, 23, 10,15, 22, 13, 30, 17, 28, 5, 24, 11, 18, 19, 16, 9, 20, 7, 26] #解密
permutation = [11, 4, 9, 10, 13, 22, 1, 30, 7, 28, 15, 24, 5, 18, 3, 16, 27, 20, 25, 26, 29, 6, 17, 14, 23, 12, 31, 8, 21, 2, 19, 0]  #加密

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

    # 将数字1置换后的位置按照从小到大的顺序排列
    sorted_new_ones_positions = sorted(new_ones_positions)

    print("数字1置换后的新位置:", sorted_new_ones_positions)

    # 统计当前轮次中置换后1在奇数位置的个数
    odd_count_after = sum(1 for pos in sorted_new_ones_positions if pos % 2 != 0)  # 统计奇数位置
    total_odd_count_after += odd_count_after  # 累加到总奇数计数

    # 根据奇偶规则生成下一轮的输入
    next_ones_positions = []
    for pos in sorted_new_ones_positions:
        next_ones_positions.append(pos)
        if pos % 2 != 0:  # 如果是奇数
            if pos - 1 >= 0:  # 如果减去1后不超出范围
                next_ones_positions.append(pos - 1)  # 将奇数减1并加入

    # 检查重复的输入位置并标记 (M)
    seen_positions = set()
    marked_positions = []
    for pos in next_ones_positions:
        if pos in seen_positions:
            if f"{pos}(M)" not in marked_positions:  # 确保仅标记一次
                marked_positions.append(f"{pos}(M)")
        else:
            marked_positions.append(pos)
            seen_positions.add(pos)
    next_ones_positions = marked_positions

    # 如果下一轮输入包含标记 (M)，更新置换后的列表
    permuted_list_with_m = []
    for pos in next_ones_positions:
        if isinstance(pos, str) and "(M)" in pos:  # 如果是标记 (M) 的位置
            permuted_list_with_m.append(f"{pos}")  # 保持原样，直接添加字符串
        else:  # 常规位置
            permuted_list_with_m.append(permuted_list[pos])  # 根据位置从permuted_list中取值

    # 输出当前轮次结果
    print(f"第{round_num}轮:")
    print("置换前的列表:", original_list)
    print("置换后的列表:", permuted_list_with_m)
    print("数字1置换后的新位置:", next_ones_positions)
    print(f"当前轮次置换后1在奇数位置的个数: {odd_count_after}")
    print(f"累计置换后1在奇数位置的总个数: {total_odd_count_after}")
    print("下一轮的输入位置:", next_ones_positions)
    print()

    # 更新当前数字1的位置
    current_ones_positions = [int(pos.split('(M)')[0]) if isinstance(pos, str) and "(M)" in pos else pos for pos in next_ones_positions]
