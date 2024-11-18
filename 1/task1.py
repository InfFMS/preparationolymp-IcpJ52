n = int(input())
m = int(input())
print(n + m - 2 + min(n // 2, m // 2) + min(n // 2, m - 1 - m // 2) + min(n - 1 - n // 2, m // 2) + min(n - 1 - n // 2,
                                                                                                        m - 1 - m // 2))
