# 11
print("11:", random.randint(1, 6))

# 12
print("12:", random.randint(1000, 9999))

# 13
lst13 = [5, 10, 15, 20, 25, 30]
print("13:", random.sample(lst13, 2))

# 14
n14 = random.randint(0, 100)
print("14:", n14, "juft" if n14 % 2 == 0 else "toq")

# 15
print("15:", ''.join(random.choice(string.ascii_lowercase) for _ in range(10)))

# 16
n16 = random.randint(1, 100)
print("16:", n16, "katta" if n16 > 50 else "kichik")

# 17
print("17:", random.choice(["heads", "tails"]))

# 18
n18 = random.randint(1, 20)
print("18:", n18, "3 ga bo'linadi" if n18 % 3 == 0 else "3 ga bo'linmaydi")

# 19
lst19 = [100, 200, 300, 400, 500]
elem19 = random.choice(lst19)
lst19.remove(elem19)
print("19:", elem19, lst19)

# 20
n20 = random.randint(1, 1000)
print("20:", n20, n20 * n20)
