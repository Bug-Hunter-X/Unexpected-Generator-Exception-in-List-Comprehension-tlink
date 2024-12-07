# Unexpected Generator Exception in List Comprehension

This repository demonstrates a subtle bug in Python related to using generator expressions within list comprehensions. The bug arises when a generator in the list comprehension throws an exception.  Standard exception handling may not catch this in the intuitive way.