total_steps = 0

while True:
    input_steps = input()

    if input_steps != "Going home":
        steps = int(input_steps)
        total_steps = total_steps + steps
        diff = abs(total_steps - 10000)
        if total_steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break

    if input_steps == "Going home":
        steps_back = int(input())
        total_steps = total_steps + steps_back
        diff = abs(total_steps - 10000)
        if total_steps < 10000:
            print(f"{diff} more steps to reach goal.")
        elif total_steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
        break


