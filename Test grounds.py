is_whites_turn = True
x = 0
for is_whites_turn in range (0,5):
    print(is_whites_turn)
    is_whites_turn = not is_whites_turn
while x < 5:
    print(is_whites_turn)
    is_whites_turn = not is_whites_turn
