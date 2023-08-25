import math

tv_show = input()
episode_length = int(input())
break_length = int(input())

time_to_eat = break_length * 1/8
time_to_relax = break_length * 1/4

needed_time = episode_length + time_to_eat + time_to_relax

if needed_time <= break_length:
    print(f"You have enough time to watch {tv_show} and left with {math.ceil(break_length - needed_time)} "
          f"minutes free time.")

else:
    print(f"You don't have enough time to watch {tv_show}, you need {math.ceil(needed_time - break_length)}"
          f" more minutes.")
