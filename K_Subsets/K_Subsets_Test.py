import pytest
from K_Subsets import k_subsets, all_k_subsets


# Tests for N = 4 and K = 0,1,2,3,4

def test_n_4_k_0():
    result = k_subsets(['a','b','c','d'], 0)
    assert result == [[]]

def test_n_4_k_1():
    result = k_subsets(['a','b','c','d'], 1)
    assert result == [['a'], ['b'], ['c'], ['d']]

def test_n_4_k_2():
    result = k_subsets(['a','b','c','d'], 2)
    assert result == [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]

def test_n_4_k_3():
    result = k_subsets(['a','b','c','d'], 3)
    assert result == [['a', 'b','c'], ['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd']]

def test_n_4_k_4():
    result = k_subsets(['a','b','c','d'], 4)
    assert result == [['a', 'b','c','d']]


# Tests for N = 5 and K = 0,1,2,3,4,5

def test_n_5_k_0():
    result = k_subsets(['a','b','c','d', 'e'], 0)
    assert result == [[]]

def test_n_5_k_1():
    result = k_subsets(['a','b','c','d', 'e'], 1)
    assert result == [['a'], ['b'], ['c'], ['d'], ['e']]

def test_n_5_k_2():
    result = k_subsets(['a','b','c','d','e'], 2)
    assert result == [['a', 'b'], ['a', 'c'], ['a', 'd'], ['a', 'e'], ['b', 'c'], ['b', 'd'], ['b', 'e'], ['c', 'd'], ['c', 'e'], ['d', 'e']]

def test_n_5_k_3():
    result = k_subsets(['a','b','c','d','e'], 3)
    assert result == [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'd'], ['a', 'c', 'e'], ['a', 'd', 'e'], ['b', 'c', 'd'], ['b', 'c', 'e'], ['b', 'd', 'e'], ['c', 'd', 'e']]

def test_n_5_k_4():
    result = k_subsets(['a','b','c','d','e'], 4)
    assert result == [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['b', 'c', 'd','e']]

def test_n_5_k_5():
    result = k_subsets(['a','b','c','d','e'], 5)
    assert result == [['a', 'b', 'c', 'd', 'e']]


# Acceptance test

def test_all_k_subsets():
    result = all_k_subsets(['a','b','c','d','e'])
    assert result == [
        [],
        ['a'], ['b'], ['c'], ['d'], ['e'],
        ['a', 'b'], ['a', 'c'], ['a', 'd'], ['a', 'e'], ['b', 'c'], ['b', 'd'], ['b', 'e'], ['c', 'd'], ['c', 'e'], ['d', 'e'],
        ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'd'], ['a', 'c', 'e'], ['a', 'd', 'e'], ['b', 'c', 'd'], ['b', 'c', 'e'], ['b', 'd', 'e'], ['c', 'd', 'e'],
        ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['b', 'c', 'd','e'],
        ['a', 'b', 'c', 'd', 'e']
    ]