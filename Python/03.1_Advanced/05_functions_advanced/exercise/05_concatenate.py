def concatenate(*args, **kwargs):
    result = ""
    for word in args:
        result += word

    for key in kwargs.keys():
        result = result.replace(key, kwargs[key])

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
