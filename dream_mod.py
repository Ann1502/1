class LevenshteinDistance:
    def lev_dist(self, s, t):
        self.s = s
        self.t = t
        n, m = len(self.t), len(self.s)

        v0 = [0] * (n + 1)
        v1 = [0] * (n + 1)

        for i in range(n):
            v0[i] = i

        for i in range(m):
            v1[0] = i + 1
            for j in range(n):
                deletionCost = v0[j + 1] + 1
                insertionCost = v1[j] + 1
                if self.s[i] == self.t[j]:
                    substitutionCost = v0[j]
                else:
                    substitutionCost = v0[j] + 1

                v1[j + 1] = min(deletionCost, insertionCost, substitutionCost)

            v0, v1 = v1, v0

        return round(v0[n], 2)


dist = LevenshteinDistance()

if __name__ == "__main__":
    for dist.s, dist.t in l:
        print(dist.s, dist.t, dist.lev_dist(dist.s, dist.t))