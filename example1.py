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

import math


def m_and_sd(nums):
    t = 0; for n in nums: t += n
    m = t / len(nums)

    ssd = 0
    for n in nums: ssd += (n - m)**2
    v = ssd / len(nums)
    sd = math.sqrt(v)

    return m, sd


numbers = [1, 2, 3, 4, 5]
m, sd = m_and_sd(numbers)

print(f"Mean: {m}")
print(f"Standard deviation: {sd}")

