rows, columns, sections = map(int, input().strip().split())
board = []
for i in range(rows):
    row = str(input().strip())
    values = [int(x) for x in row.split(" ")]
    board.append(values)
print(board)