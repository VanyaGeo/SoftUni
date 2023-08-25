# I

cards = input().split()    # a b c d e f g h
count_of_faro_shuffles = int(input())  # 5

final_cards_order = []

for shuffle in range(count_of_faro_shuffles):
    final_cards_order = []
    half_cards_length = len(cards) // 2
    left_half_cards = cards[0:half_cards_length]
    right_half_cards = cards[half_cards_length::]
    for card in range(len(left_half_cards)):
        final_cards_order.append(left_half_cards[card])
        final_cards_order.append(right_half_cards[card])
    cards = final_cards_order

print(final_cards_order)

# II

# starting_cards = input().split()
# shuffles = int(input())
#
# shuffled_cards = []
#
# for shuffle in range(shuffles):
#     left_half = starting_cards[:len(starting_cards)//2]
#     right_half = starting_cards[len(starting_cards)//2:]
#     for card in zip(left_half, right_half):
#         shuffled_cards.extend(card)
#     starting_cards = shuffled_cards
#     shuffled_cards = []
# print(starting_cards)

