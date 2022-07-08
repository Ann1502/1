def LevenshteinDistance(s, t):
    n, m = len(t), len(s)

    v0 = [0] * (n + 1)
    v1 = [0] * (n + 1)

    for i in range(n):
        v0[i] = i

    for i in range(m):
        v1[0] = i + 1
        for j in range(n):
            deletionCost = v0[j + 1] + 1
            insertionCost = v1[j] + 1
            if s[i] == t[j]:
                substitutionCost = v0[j]
            else:
                substitutionCost = v0[j] + 1

            v1[j + 1] = min(deletionCost, insertionCost, substitutionCost)

        v0, v1 = v1, v0

    return round(v0[n], 2)
    # return round(v0[n]*100/max(len(s), len(t)), 2)
    # полученное значение преобразую в процентное значение и округляю до 2 знака после запятой
    # 0 - строка s полностью похожа на t
    # 100 - строка s полностью не похожа на t


if __name__ == "__main__":
    for s, t in L:
        print(s, t, LevenshteinDistance(s, t))