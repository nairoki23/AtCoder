def main():
    ans = []
    for i in range(2, 1 << 10):  # 修正が必要
        x = 0
        for j in range(9, -1, -1):
            if i & (1 << j):
                x *= 10
                x += j
        ans.append(x)

    ans.sort()

    k = int(input())
    print(ans[k - 1])

if __name__ == "__main__":
    main()