from typing import Callable

# texy to analize total income
text = "Загальний дохід працівника складається з декількох частин: \
        1000.01 як основний дохід, \
        доповнений додатковими надходженнями 27.45 i 324.00 доларів."


def generator_numbers(text: str):
    """Generator with required argument - text: str
        yields all real numbers from text by turning them into 'float'"""
    for income in text.split():
        if any(ch.isdigit() for ch in income):
            yield float(income)

def sum_profit(text: str, func: Callable):
    """Function with required arguments - 'text: str, func: Callable',
        func must be 'generator'!
        returns sumary of all numbers taken from func"""
    sum = float()
    for incom in func(text):
        sum += incom
    return sum

total_income = sum_profit(text, generator_numbers) #Count total income from procesd text 

print(f"Загальний дохід: {total_income}")
