electron_amount = int(input())
shell = 1
electron_in_shell_amount = 0
list_shells = []

while electron_amount > 0:
    electron_in_shell_amount = 2 * (shell ** 2)
    if electron_amount < electron_in_shell_amount:
        list_shells.append(electron_amount)
        break
    list_shells.append(electron_in_shell_amount)
    electron_amount -= electron_in_shell_amount
    shell += 1
print(list_shells)


