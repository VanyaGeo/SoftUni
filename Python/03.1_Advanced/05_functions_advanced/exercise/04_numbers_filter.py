def even_odd_filter(**kwargs):
    even_odd_dict = {}
    for key, value in kwargs.items():
        if key == "odd":
            even_odd_dict["odd"] = [num for num in kwargs["odd"] if num % 2 != 0]

        if key == "even":
            even_odd_dict["even"] = [num for num in kwargs["even"] if num % 2 == 0]

    return dict(sorted(even_odd_dict.items(), key=lambda x: -len(x[1])))


# Test inputs:
print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
# print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))