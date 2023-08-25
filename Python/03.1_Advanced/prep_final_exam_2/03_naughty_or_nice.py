def naughty_or_nice_list(all_kids_list, *args, **kwargs):
    santa_list = [list(t) for t in all_kids_list]
    nice_kids = []
    naughty_kids = []
    result = ""

    def find_kids_list():
        if len(kids) == 1:
            
            nice_kids.append(kids[0][1]) if type_of_kid == "Nice" else naughty_kids.append(kids[0][1])
            santa_list.remove(*kids)

    for kid_data in args:
        number, type_of_kid = kid_data.split("-")
        kids = [info for info in santa_list if info[0] == int(number)]
        find_kids_list()

    for name, type_of_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        find_kids_list()

    not_found = [info[1] for info in santa_list]

    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result


# print(naughty_or_nice_list( [
# (6, "John"),
# (4, "Karen"),
# (2, "Tim"),
# (1, "Merry"),
# (6, "Frank"),
# ],
# "6-Nice",
# "5-Naughty",
# "4-Nice",
# "3-Naughty",
# "2-Nice",
# "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty",
# ))
