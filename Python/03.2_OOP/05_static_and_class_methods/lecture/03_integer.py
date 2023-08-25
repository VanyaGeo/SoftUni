import math


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if isinstance(float_value, float):
            return cls(math.floor(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(value)):
            if i < len(value) - 1 and roman_values[value[i]] < roman_values[value[i + 1]]:
                total -= roman_values[value[i]]
            else:
                total += roman_values[value[i]]

        return cls(total)

    @classmethod
    def from_string(cls, value: str):
        try:
            number = int(value)
            if not isinstance(value, str):
                raise ValueError
            return cls(number)
        except ValueError:
            return "wrong type"


# first_num = Integer(10)
# print(first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num.value)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))

# first_num = Integer(1)
# print(first_num.value)
# print(Integer.from_float(2.5))
# print(Integer.from_float("2.5"))
# print(Integer.from_roman("XIX"))
# print(Integer.from_string("10"))
# print(Integer.from_string(1.5))
