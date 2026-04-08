def warp_sbox(hex_input):
    """
    WARP 算法的 S 盒 (基于 Midori 的 S 盒).
    查找表: 0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6
    """
    sbox_table = [
        0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7,
        0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6
    ]
    return sbox_table[hex_input]


def compute_ddt(sbox_func, n=4):
    """
    计算给定 S 盒的差分分布表 (DDT).

    参数:
        sbox_func: S 盒函数，接受整数输入并返回整数输出。
        n: S 盒的位宽 (WARP 是 4 位).
    返回:
        一个二维列表 (size 2^n x 2^n), DDT[输入差分][输出差分] = 个数.
    """
    size = 1 << n  # 2^n
    ddt = [[0] * size for _ in range(size)]

    for input_x in range(size):
        for input_y in range(size):
            input_diff = input_x ^ input_y
            output_diff = sbox_func(input_x) ^ sbox_func(input_y)
            ddt[input_diff][output_diff] += 1

    return ddt


def print_ddt(ddt):
    """
    以美观的表格形式打印差分分布表 (DDT).
    """
    size = len(ddt)
    print("WARP S-box DDT (Input Diff -> Output Diff):")
    print("    " + " ".join(f"{i:2d}" for i in range(size)))
    print("    " + "-" * (3 * size))

    for i in range(size):
        row = ddt[i]
        # 可选: 高亮显示最大概率 (2^(n-1) = 8 对于 4 位 S 盒)
        print(f"{i:2d}: " + " ".join(f"{val:2d}" for val in row))


def analyze_ddt(ddt):
    """
    分析 DDT 并打印关键统计信息.
    """
    size = len(ddt)
    max_val = 0
    max_count = 0

    for i in range(size):
        for j in range(size):
            if ddt[i][j] > max_val:
                max_val = ddt[i][j]
                max_count = 1
            elif ddt[i][j] == max_val and ddt[i][j] > 0:
                max_count += 1

    print("\n--- DDT 分析 ---")
    print(f"最大 DDT 条目: {max_val}")
    print(f"达到最大值的条目数 (输入差分!=0 或输出差分!=0): {max_count}")

    # 检查差分均匀性
    if max_val == 4:  # 对于 4 位 S 盒通常是 4
        print("结论: S 盒是差分 4-均匀的 (对于分组密码来说是良好的特性).")
    else:
        print(f"结论: 最大差分概率 = {max_val}/{size} = {max_val / size:.2f}")


# --- 主程序执行 ---
if __name__ == "__main__":
    # 1. 计算 DDT
    ddt_table = compute_ddt(warp_sbox)

    # 2. 打印表格
    print_ddt(ddt_table)

    # 3. 分析结果
    analyze_ddt(ddt_table)
