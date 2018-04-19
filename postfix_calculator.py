"""
    POSTFIX CALCULATOR
    18-April-2018

    This problem can be solved using a stack

    Algorithm:
        foreach token
            if token is integer
                push token
            else if token is operator
                pop right-side value
                pop left-side value
                evaluate operator
                push result
        next
"""
import unittest
from stack.stack import Stack


class PostfixCalculator(object):
    def __init__(self, tokens_string=""):
        self._tokens_string = tokens_string
        self._stack = Stack()
        self._result = 0

    @property
    def tokens(self):
        return self._tokens_string

    def _tokenize(self):
        return self._tokens_string.split()

    def _do_operation(self, operator):
        # """ This method mimics a switch statement """
        rhs = self._stack.pop()  # right hand side operand
        lhs = self._stack.pop()  # left hand side operand
        # switch
        return {
            "+": int(lhs)+ int(rhs),
            "-": int(lhs) - int(rhs),
            "*": int(lhs) * int(rhs),
            "/": int(lhs) / int(rhs),
        }.get(operator, "unknown operator {}".format(operator))

    def calculate(self):
        """ Execute postfix algorithm here """
        tokens = self._tokenize()
        for token in tokens:
            try:
                self._stack.push(int(token))
            except ValueError:
                self._stack.push(self._do_operation(token))
        # Peek at the top of the stack to get the result
        self._result = self._stack.peek()

    @property
    def result(self):
        return self._result

# Tests


class TestPostfixCalc(unittest.TestCase):

    def setUp(self):
        self.calc = PostfixCalculator("5 6 7 * + 1 -")

    def test_calculator(self):
        self.calc.calculate()
        self.assertEqual(self.calc.result, 46)


if __name__ == '__main__':
    unittest.main()