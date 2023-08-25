actor_name = input()
point = float(input())
people = int(input())

final_points = point


for i in range(1, people + 1):
    juri = input()
    juri_points = float(input())
    current_points = len(juri) * juri_points / 2
    final_points = final_points + current_points

    if final_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - final_points:.1f} more!")
