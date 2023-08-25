def age_assignment(*args, **kwargs):
    result = []
    for letter in kwargs.keys():
        for name in args:
            if letter in name:
                result.append(f"{name} is {kwargs[letter]} years old.")
    sorted_result = sorted(result)
    return "\n".join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
