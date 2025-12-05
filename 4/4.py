with open("4/input.txt", "r") as f:
    paper = [[c for c in line.strip()] for line in f]

print(paper, "paper")
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

r, c = 0, 0

res = 0

rows = len(paper)
cols = len(paper[0])


while True:
    rows_to_remove = []
    r = 0
    while r < rows:
        c = 0
        while c < cols:
            if paper[r][c] == "@":
                paper_number = 0
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if paper[new_row][new_col] == "@":
                            paper_number += 1

                if paper_number < 4:
                    print(f"{r, c} has greater less than 4 adjacent paper rolls")
                    rows_to_remove.append((r, c))
                    res += 1
            c += 1
        r += 1
    if not rows_to_remove:
        break
    for rmr, rmc in rows_to_remove:
        paper[rmr][rmc] = "."
print(res)
