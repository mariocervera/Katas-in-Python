import pytest
import RPNCalculator

# Tests

def test_singleOperand_shouldReturnOperand():
    verify_evaluation('3', 3)
    verify_evaluation('5', 5)
    verify_evaluation('9', 9)

def test_oneOperation_shouldReturnCorrectResult():
    verify_evaluation('3 1 +',  4)
    verify_evaluation('3 2 +',  5)
    verify_evaluation('4 2 +',  6)
    verify_evaluation('3 1 -', 2)
    verify_evaluation('5 2 -', 3)
    verify_evaluation('5 2 *', 10)
    verify_evaluation('2 3 *', 6)
    verify_evaluation('9 3 /', 3)
    verify_evaluation('10 5 /', 2)

def test_oneNestedOperation_shouldReturnCorrectResult():
    verify_evaluation('3 1 + 1 +', 5)
    verify_evaluation('4 2 - 1 +', 3)
    verify_evaluation('6 2 * 1 -', 11)
    verify_evaluation('10 3 * 2 /', 15)
    verify_evaluation('1 2 3 * +', 7)

def test_twoNestedOperations_shouldReturnCorrectResult():
    verify_evaluation('3 5 8 * 7 + *', 141)
    verify_evaluation('1 2 3 4 * 5 - 6 * + +', 45)

# Verification methods

def verify_evaluation(rpn_expression, expected_result):
    assert RPNCalculator.evaluate(rpn_expression) == expected_result