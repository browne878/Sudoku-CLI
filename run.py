from classes.board import Board

# print("¦===================================¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦===========¦===========¦===========¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦===========¦===========¦===========¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦ 0 | 0 | 0 ¦")
# print("¦===================================¦")

board = Board('normal')
board.populate_board()

for row in board.board:
    print(row)

if not board.edit_board(1, 3, '3'):
    print('Incorrect number or invalid Index')
else:
    for row in board.board:
        print(row)

print(board.check_complete())
