import pytest
from K_Subsets import k_subsets, all_k_subsets


# Tests for N = 4 and K = 0, 1, 2, 3, 4

def test_n_4_k_0():
    actual_sets = k_subsets(['a','b','c','d'], 0)
    expected_sets = [[]]
    assert expected_sets == actual_sets 

def test_n_4_k_1():
    actual_sets = k_subsets(['a','b','c','d'], 1)
    expected_sets = [['a'], ['b'], ['c'], ['d']]
    assert expected_sets == actual_sets

def test_n_4_k_2():
    actual_sets = k_subsets(['a','b','c','d'], 2)
    expected_sets = [['a','b'], ['a','c'], ['a','d'], ['b','c'], ['b','d'], ['c','d']]
    assert expected_sets == actual_sets  

def test_n_4_k_3():
    actual_sets = k_subsets(['a','b','c','d'], 3)
    expected_sets = [['a','b','c'], ['a','b','d'], ['a','c','d'], ['b','c','d']]
    assert expected_sets == actual_sets

def test_n_4_k_4():
    actual_sets = k_subsets(['a','b','c','d'], 4)
    expected_sets = [['a','b','c','d']]
    assert expected_sets == actual_sets


# Tests for N = 5 and K = 0, 1, 2, 3, 4, 5

def test_n_5_k_0():
    actual_sets = k_subsets(['a','b','c','d','e'], 0)
    expected_sets = [[]]
    assert expected_sets == actual_sets

def test_n_5_k_1():
    actual_sets = k_subsets(['a','b','c','d','e'], 1)
    expected_sets = [['a'], ['b'], ['c'], ['d'], ['e']]
    assert expected_sets == actual_sets

def test_n_5_k_2():
    actual_sets = k_subsets(['a','b','c','d','e'], 2)
    expected_sets = [['a','b'], ['a','c'], ['a','d'], ['a','e'], ['b','c'], ['b','d'], ['b','e'], ['c','d'], ['c','e'], ['d','e']]
    assert expected_sets == actual_sets

def test_n_5_k_3():
    actual_sets = k_subsets(['a','b','c','d','e'], 3)
    expected_sets = [['a','b','c'], ['a','b','d'], ['a','b','e'], ['a','c','d'], ['a','c','e'], ['a','d','e'], ['b','c','d'], ['b','c','e'], ['b','d','e'], ['c','d','e']]
    assert expected_sets == actual_sets

def test_n_5_k_4():
    actual_sets = k_subsets(['a','b','c','d','e'], 4)
    expected_sets = [['a','b','c','d'], ['a','b','c','e'], ['a','b','d','e'], ['a','c','d','e'], ['b','c','d','e']]
    assert expected_sets == actual_sets

def test_n_5_k_5():
    actual_sets = k_subsets(['a','b','c','d','e'], 5)
    expected_sets = [['a','b','c','d','e']]
    assert expected_sets == actual_sets


# Acceptance test

def test_all_k_subsets():
    actual_sets = all_k_subsets(['a','b','c','d','e'])
    expected_sets = [
        [],
        ['a'], ['b'], ['c'], ['d'], ['e'],
        ['a','b'], ['a','c'], ['a','d'], ['a','e'], ['b','c'], ['b','d'], ['b','e'], ['c','d'], ['c','e'], ['d','e'],
        ['a','b','c'], ['a','b','d'], ['a','b','e'], ['a','c','d'], ['a','c','e'], ['a','d','e'], ['b','c','d'], ['b','c','e'], ['b','d','e'], ['c','d','e'],
        ['a','b','c','d'], ['a','b','c','e'], ['a','b','d','e'], ['a','c','d','e'], ['b','c','d','e'],
        ['a','b','c','d','e']
    ]
    assert expected_sets == actual_sets