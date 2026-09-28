"""
Lab 1 · Truth-Table Engine
Discrete Mathematics (YMT211) · Fall 2026

Your job: fill in every function marked TODO.
Check yourself any time with:      python check.py
Submit when you are happy with:    gh student submit

Rules
- A "formula" in this lab is a Python function that takes booleans and returns a boolean,
  for example   lambda p, q: implies(p, q) and not q
- Do not change function names or parameters: the autograder calls them by name.
- You may use the standard library (itertools is especially useful). No other packages.
"""

from itertools import product


# ---------------------------------------------------------------------------
# Part A · Connectives
# Python already has `not`, `and`, `or`. Write the other three.
# ---------------------------------------------------------------------------

def implies(p: bool, q: bool) -> bool:
    return (not p) or q
    """p → q. False only when p is True and q is False."""
    # TODO
    raise NotImplementedError


def iff(p: bool, q: bool) -> bool:
    return p == q
    """p ↔ q. True when p and q have the same truth value."""
    # TODO
    raise NotImplementedError


def xor(p: bool, q: bool) -> bool:
    return p or q
    """p ⊕ q. True when exactly one of p, q is True."""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part B · All the rows of a truth table
# ---------------------------------------------------------------------------

def rows(n: int) -> list[tuple[bool, ...]]:
    
    """
    Return every assignment of n variables, in standard truth-table order
    (True before False, the last variable changes fastest).

    rows(2) == [(True, True), (True, False), (False, True), (False, False)]
    rows(0) == [()]          # one row: the empty assignment
    Hint: itertools.product
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part C · Truth tables and their verdicts
# ---------------------------------------------------------------------------

def truth_table(f, n: int) -> list[tuple[tuple[bool, ...], bool]]:
    """
    Return [(row, f(*row)) for every row of n variables], in the order of rows(n).

    truth_table(lambda p: not p, 1) == [((True,), False), ((False,), True)]
    """
    # TODO
    raise NotImplementedError


def is_tautology(f, n: int) -> bool:
    """True if f is True in every row."""
    # TODO
    raise NotImplementedError


def is_contradiction(f, n: int) -> bool:
    """True if f is False in every row."""
    # TODO
    raise NotImplementedError


def is_satisfiable(f, n: int) -> bool:
    """True if f is True in at least one row."""
    # TODO
    raise NotImplementedError


def equivalent(f, g, n: int) -> bool:
    """True if f and g have the same value in every row (f ≡ g)."""
    # TODO
    raise NotImplementedError


def count_true(f, n: int) -> int:
    """How many rows make f True?"""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part D · Pretty printing
# ---------------------------------------------------------------------------

def format_table(f, names: list[str], label: str = "result") -> str:
    """
    Return the truth table as text, one line per row, using 1 and 0.
    Columns are separated by a single space, and the result column by " | ".

    format_table(lambda p, q: p and q, ["p", "q"], "p∧q") returns

        p q | p∧q
        1 1 | 1
        1 0 | 0
        0 1 | 0
        0 0 | 0

    (lines joined with "\\n", no trailing newline, no extra spaces)
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Part E · From English to Python
# p: "the server is overloaded"   q: "the request is served from cache"   r: "the response is slow"
# Each function must return the truth value of the sentence for the given p, q, r.
# ---------------------------------------------------------------------------

def spec1(p: bool, q: bool, r: bool) -> bool:
    """The response is slow only if the server is overloaded and the request is not served from cache."""
    # TODO
    raise NotImplementedError


def spec2(p: bool, q: bool, r: bool) -> bool:
    """The request is served from cache unless the server is overloaded."""
    # TODO
    raise NotImplementedError


def spec3(p: bool, q: bool, r: bool) -> bool:
    """Neither is the server overloaded nor is the response slow."""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Try it: run   python truth.py   to see your engine at work.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    contrapositive = lambda p, q: iff(implies(p, q), implies(not q, not p))
    converse = lambda p, q: iff(implies(p, q), implies(q, p))

    print(format_table(lambda p, q: implies(p, q), ["p", "q"], "p→q"))
    print()
    print("(p → q) ↔ (¬q → ¬p) is a tautology:", is_tautology(contrapositive, 2))
    print("(p → q) ↔ (q → p)   is a tautology:", is_tautology(converse, 2))
