from learntools.core import *
import pandas as pd, numpy as np

ex1_sol = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
ex2_sol = pd.DataFrame({'ser1': list('iloveyou'), 'ser2': range(8)})
ex3_sol = pd.Series([11, 12, 13, 16, 17, 18])
ex4_sol = pd.Series([10, 20, 0, 11, 90, 0, 55, 14, 0, 25, 75, 35], name="Sale", dtype=np.float64)
ex5_sol = pd.Series([10, 20, 37, 11, 90, 37, 55, 14, 37, 25, 75, 35], name="Sale", dtype=np.float64)
ex6_sol = 8
ex7_sol = 55
ex8_sol = 1991
ex9_sol = 'pass'
ex10_sol = pd.read_csv('answers/q10_answer.csv')
ex11_sol = 1974
ex12_sol = 202.12
ex13_sol = 33701

ex14_sol = pd.read_csv("answers/q14_answer.csv", index_col=0).squeeze()
ex14_sol.name = None

ex15_sol = pd.read_csv('answers/q15_answer.csv', index_col=0).squeeze()
ex16_sol = pd.read_csv('answers/q16_answer.csv', index_col=0).squeeze()
ex17_sol = pd.read_csv('answers/q17_answer.csv', index_col=0)
ex18_sol = 'pass'
ex19_sol = (0.805, 0.302)
ex20_sol = pd.read_csv('answers/q20_answer.csv', index_col=0).squeeze()

class Exercise1(EqualityCheckProblem):
    _solution = None
    _var = "ex1_sol"
    _expected = ex1_sol
    _hint = ("")

class Exercise2(EqualityCheckProblem):
    _solution = None
    _var = "ex2_sol"
    _expected = ex2_sol
    _hint = ("Try concat().")

class Exercise3(EqualityCheckProblem):
    _solution = None
    _var = "ex3_sol"
    _expected = ex3_sol
    _hint = ("Rephrased question: Find elements that are in the union set of A and B but not in the common set of A and B.")

class Exercise4(EqualityCheckProblem):
    _solution = None
    _var = "ex4_sol"
    _expected = ex4_sol
    _hint = ("")

class Exercise5(EqualityCheckProblem):
    _solution = None
    _var = "ex5_sol"
    _expected = ex5_sol
    _hint = ("Have you rounded the mean to integer?")

class Exercise6(EqualityCheckProblem):
    _solution = None
    _var = "ex6_sol"
    _expected = ex6_sol
    _hint = ("In other words, how many unique IDs are there?")

class Exercise7(EqualityCheckProblem):
    _solution = None
    _var = "ex7_sol"
    _expected = ex7_sol
    _hint = ("In other words, how many unique Years are there?")

class Exercise8(EqualityCheckProblem):
    _solution = None
    _var = "ex8_sol"
    _expected = ex8_sol
    _hint = ("Find the row index with the highest crime in the column 'Property', then extract the value in 'Year'. Have you tried idxmax()")

class Exercise9(EqualityCheckProblem):
    _solution = None
    _var = "ex9_sol"
    _expected = ex9_sol
    _hint = ("Convert the Year column first and then assign it back to itself.")

class Exercise10(EqualityCheckProblem):
    _solution = None
    _var = "ex10_sol"
    _expected = ex10_sol
    _hint = ("Find the any column contains 'theft' in their name and revert the result by using 'not' or '~'")

class Exercise11(EqualityCheckProblem):
    _solution = None
    _var = "ex11_sol"
    _expected = ex11_sol
    _hint = ("Ever heard of pct_change()?")

class Exercise12(EqualityCheckProblem):
    _solution = None
    _var = "ex12_sol"
    _expected = ex12_sol
    _hint = ("You can retrieve the values of the two given years and calculate with the formula given.")

class Exercise13(EqualityCheckProblem):
    _solution = None
    _var = "ex13_sol"
    _expected = ex13_sol
    _hint = ("")

class Exercise14(EqualityCheckProblem):
    _solution = None
    _var = "ex14_sol"
    _expected = ex14_sol
    _hint = ("Find all values that are NaN with isnull() or isna().")

class Exercise15(EqualityCheckProblem):
    _solution = None
    _var = "ex15_sol"
    _expected = ex15_sol
    _hint = ("")

class Exercise16(EqualityCheckProblem):
    _solution = None
    _var = "ex16_sol"
    _expected = ex16_sol
    _hint = ("")

class Exercise17(EqualityCheckProblem):
    _solution = None
    _var = "ex17_sol"
    _expected = ex17_sol
    _hint = ("")

class Exercise18(EqualityCheckProblem):
    _solution = None
    _var = "ex18_sol"
    _expected = ex18_sol
    _hint = ("In other words, show a table which has values from the 'categories' column as indices, 'countries' as columns, and their values are the mean of 'carbohydrates_100g'")

class Exercise19(EqualityCheckProblem):
    _solution = None
    _var = "ex19_sol"
    _expected = ex19_sol
    _hint = ("Try writing a function to check if the input keyword matches any of the words in the list. Then use apply() to create a column 'is_processed'.")


class Exercise20(EqualityCheckProblem):
    _solution = None
    _var = "ex20_sol"
    _expected = ex20_sol
    _hint = ("Remember to 'strip' your main ingredients ( ͡° ͜ʖ ͡°)")

qvars = bind_exercises(globals(), [
    Exercise1,
    Exercise2,
    Exercise3,
    Exercise4,
    Exercise5,
    Exercise6,
    Exercise7,
    Exercise8,
    Exercise9,
    Exercise10,
    Exercise11,
    Exercise12,
    Exercise13,
    Exercise14,
    Exercise15,
    Exercise16,
    Exercise17,
    Exercise18,
    Exercise19,
    Exercise20
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)