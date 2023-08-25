from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = deque(int(x) for x in input().split())

while substances and tools:
    if challenges:
        cur_subst = substances.pop()
        cur_tool = tools.popleft()
        multiplied_amount = cur_tool * cur_subst

        if multiplied_amount in challenges:
            challenges.remove(multiplied_amount)
        else:
            cur_tool += 1
            tools.append(cur_tool)
            cur_subst -= 1
            if cur_subst > 0:
                substances.append(cur_subst)
    else:
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
if len(challenges) == 0:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")

