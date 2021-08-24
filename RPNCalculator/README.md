# Katas-in-Python

This kata implements a calculator for computing expressions written in Reverse Polish Notation (RPN).

An RPN expression (or postfix expression) is one of the following:

* A number *X*, in which case the value of the expression is X.

* A sequence of the form *E1 E2 OP*, where E1 and E2 are RPN expressions and OP is an arithmetic operation.

Examples:

* 20 5 / is equivalent to 20/5 (which is equal to 4).

* 4 2 + 3 - is equivalent to (4+2)-3 (which is equal to 3).

3 5 8 * 7 + * is equivalent to ((5*8)+7)*3 (which is equal to 141).