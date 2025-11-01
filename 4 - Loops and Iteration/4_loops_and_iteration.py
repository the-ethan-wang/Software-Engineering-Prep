import decimal
import fractions

test_1 = .1 + .2
test_2 = float(test_1)
test_3 = 0.1 * int(10 * test_1)

test_4 = float(decimal.Decimal('.1') + decimal.Decimal('.2'))
test_5 = float(fractions.Fraction('0.1') + fractions.Fraction('0.2'))

tests = [test_1, test_2, test_3, test_4, test_5]

for test in tests:
    if test == 0.3:
        print("Test successful!")
    else:
        print("Test failed. returned {}".format(test))

