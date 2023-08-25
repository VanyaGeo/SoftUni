def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for name, amount in sorted_cheeses:
        result += f"{name}\n"
        reversed_amount = sorted(amount, reverse=True)
        for quantity in reversed_amount:
            result += f"{quantity}\n"

    return result


print(
    sorting_cheeses(
    Parmesan=[102, 120, 135],
    Camembert=[100, 100, 105, 500, 430],
    Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
    Parmigiano=[165, 215],
    Feta=[150, 515],
    Brie=[150, 125]
    )
)
