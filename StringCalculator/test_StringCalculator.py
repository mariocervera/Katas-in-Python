import pytest
import StringCalculator

# Tests

def test_emptyString_shouldReturnO():
    verify_add('', '0')

def test_singleNumber_shouldReturnSameNumber():
    verify_add('1', '1')
    verify_add('2', '2')
    verify_add('10', '10')

def test_twoIntegerNumbers_shouldReturnCorrectSum():
    verify_add('1,2', '3')
    verify_add('4,12', '16')

def test_singleFloatNumber_shouldReturnSameNumber():
    verify_add('1.2', '1.2')

def test_twoFloatNumbers_shouldReturnCorrectSum():
    verify_add('1.2,3.9', '5.1')
    verify_add('1.2,3.8', '5.0')

def test_twoNumbersMixedTypes_shouldReturnCorrectSum():
    verify_add('1.2,3', '4.2')
    verify_add('11.2,5', '16.2')

def test_threeIntegerNumbers_shouldReturnCorrectSum():
    verify_add('1,2,3', '6')
    verify_add('1,21,30', '52')

def test_threeNumbersMixedTypes_shouldReturnCorrectSum():
    verify_add('1,2,3.1', '6.1')
    verify_add('1.2,2.2,3', '6.4')

def test_numbersWithDifferentDelimiters_shouldReturnCorrectSum():
    verify_add('1,2\n3', '6')

def test_missingNumbers_shouldReturnErrorMessage():
    verify_add('1,', 'Number expected but EOF found.')
    verify_add('1,1.2,', 'Number expected but EOF found.')
    verify_add('1,,4', 'Number expected but EOF found.')

def test_negativeNumbers_shouldReturnErrorContainingNumber():
    verify_add('-1,2', "Negative not allowed : ['-1']")
    verify_add('-1,2,-3', "Negative not allowed : ['-1', '-3']")


# Verification methods

def verify_add(input_number, expected_result):
    assert StringCalculator.add(input_number) == expected_result