with open("2/input.txt", "r") as f:
    line = f.readline().strip()
ranges = line.split(",")

res = 0


def pattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            pattern = s[:i]
            if pattern * (n // i) == s:
                return True
    return False


for r in ranges:
    split_range = r.split("-")
    start = split_range[0]
    end = split_range[1]
    for i in range(int(start), int(end) + 1):
        if pattern(str(i)):
            res += i
print(res)
