# The Zen of Python
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


def calculate_tax(income, state):
    tax = income
    if state == "NY":
        tax *= 0.06
    elif state == "NJ":
        tax *= 0.05
    elif state == "CT":
        tax *= 0.04
    elif state == "FL":
        tax *= 0.03
    return tax


income = 20000
print(f"NY Tax: {calculate_tax(income, 'NY')}")
print(f"NJ Tax: {calculate_tax(income, 'NJ')}")
print(f"CT Tax: {calculate_tax(income, 'CT')}")
print(f"FL Tax: {calculate_tax(income, 'FL')}")


