# I

player_cards = input().split()

team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

for card in player_cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")

# II

# player_cards = input().split()
#
# team_a_players_count = []
# team_b_players_count = []
#
# for card in player_cards:
#     if card in team_a_players_count or card in team_b_players_count:
#         continue
#
#     card_args = card.split("-")  # args = arguments
#     team_name = card_args[0]
#     player_number = card_args[1]
#
#     if team_name == "A":
#         team_a_players_count.append(card)
#     else:
#         team_b_players_count.append(card)
#
#     if len(team_a_players_count) > 4 or len(team_b_players_count) > 4:
#         break
#
# print(f"Team A - {11 - len(team_a_players_count)}; Team B - {11 - len(team_b_players_count)}")
# if len(team_a_players_count) < 7 or len(team_b_players_count) < 7:
#     print("Game was terminated")
