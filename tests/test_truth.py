"""Tests for Lab 1. Run them with:  python check.py   (or: python -m pytest)"""
import pytest

import truth as t

B = [True, False]
PAIRS = [(p, q) for p in B for q in B]


# Part A ---------------------------------------------------------------------

def test_implies():
    """implies(p, q) matches the truth table of p → q"""
    expected = {(True, True): True, (True, False): False, (False, True): True, (False, False): True}
    for (p, q), v in expected.items():
        assert t.implies(p, q) is v, f"implies({p}, {q}) should be {v}"


def test_iff():
    """iff(p, q) matches the truth table of p ↔ q"""
    for p, q in PAIRS:
        assert t.iff(p, q) is (p == q), f"iff({p}, {q}) should be {p == q}"


def test_xor():
    """xor(p, q) matches the truth table of p ⊕ q"""
    for p, q in PAIRS:
        assert t.xor(p, q) is (p != q), f"xor({p}, {q}) should be {p != q}"


# Part B ---------------------------------------------------------------------

def test_rows_two():
    """rows(2) lists the 4 rows in standard order"""
    assert t.rows(2) == [(True, True), (True, False), (False, True), (False, False)]


@pytest.mark.parametrize("n", [0, 1, 3, 5])
def test_rows_count(n):
    """rows(n) has 2ⁿ distinct rows of length n"""
    r = t.rows(n)
    assert len(r) == 2 ** n, f"rows({n}) should have {2 ** n} rows, got {len(r)}"
    assert len(set(r)) == 2 ** n, "rows must be distinct"
    assert all(len(x) == n for x in r), f"every row of rows({n}) must have length {n}"
    assert all(type(v) is bool for x in r for v in x), "values must be True/False, not 1/0"


def test_rows_order():
    """rows(3) starts with all True and ends with all False, last variable fastest"""
    r = t.rows(3)
    assert r[0] == (True, True, True) and r[1] == (True, True, False) and r[-1] == (False, False, False)


# Part C ---------------------------------------------------------------------

def test_truth_table_negation():
    """truth_table(¬p, 1) is [((True,), False), ((False,), True)]"""
    assert t.truth_table(lambda p: not p, 1) == [((True,), False), ((False,), True)]


def test_truth_table_three_vars():
    """truth_table((p ∧ q) → r, 3) has the right 8 rows"""
    f = lambda p, q, r: (not (p and q)) or r
    expected = [(row, f(*row)) for row in [(a, b, c) for a in B for b in B for c in B]]
    assert t.truth_table(f, 3) == expected


def test_tautology():
    """is_tautology recognizes p ∨ ¬p and the contrapositive, rejects the converse"""
    assert t.is_tautology(lambda p: p or not p, 1)
    assert t.is_tautology(lambda p, q: ((not p) or q) == (q or not p), 2)
    contra = lambda p, q: ((not p) or q) == ((not (not q)) or (not p))   # (p→q) ↔ (¬q→¬p)
    assert t.is_tautology(contra, 2)
    converse = lambda p, q: ((not p) or q) == ((not q) or p)
    assert not t.is_tautology(converse, 2)


def test_contradiction():
    """is_contradiction recognizes p ∧ ¬p and rejects p ∨ q"""
    assert t.is_contradiction(lambda p: p and not p, 1)
    assert not t.is_contradiction(lambda p, q: p or q, 2)


def test_satisfiable():
    """is_satisfiable is True for p ∧ q and False for (p ⊕ q) ∧ (p ↔ q)"""
    assert t.is_satisfiable(lambda p, q: p and q, 2)
    assert not t.is_satisfiable(lambda p, q: (p != q) and (p == q), 2)


def test_equivalent():
    """equivalent: De Morgan holds, and p → q is not q → p"""
    assert t.equivalent(lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2)
    assert t.equivalent(lambda p, q: not (p or q), lambda p, q: (not p) and (not q), 2)
    assert not t.equivalent(lambda p, q: (not p) or q, lambda p, q: (not q) or p, 2)


def test_count_true():
    """count_true counts satisfying rows (p ∨ q ∨ r is true in 7 of 8)"""
    assert t.count_true(lambda p, q, r: p or q or r, 3) == 7
    assert t.count_true(lambda p, q: p and q, 2) == 1
    assert t.count_true(lambda p: p and not p, 1) == 0


# Part D ---------------------------------------------------------------------

def test_format_table():
    """format_table prints the AND table exactly as specified"""
    got = t.format_table(lambda p, q: p and q, ["p", "q"], "p∧q")
    assert got == "p q | p∧q\n1 1 | 1\n1 0 | 0\n0 1 | 0\n0 0 | 0", f"got:\n{got}"


def test_format_table_default_label():
    """format_table uses 'result' as the default label"""
    got = t.format_table(lambda p: not p, ["p"])
    assert got == "p | result\n1 | 0\n0 | 1", f"got:\n{got}"


# Part E ---------------------------------------------------------------------

TRIPLES = [(p, q, r) for p in B for q in B for r in B]


def test_spec1():
    """spec1: r → (p ∧ ¬q)"""
    for p, q, r in TRIPLES:
        assert t.spec1(p, q, r) == ((not r) or (p and not q)), f"spec1{(p, q, r)}"


def test_spec2():
    """spec2: ¬p → q   (“q unless p”)"""
    for p, q, r in TRIPLES:
        assert t.spec2(p, q, r) == (p or q), f"spec2{(p, q, r)}"


def test_spec3():
    """spec3: ¬p ∧ ¬r"""
    for p, q, r in TRIPLES:
        assert t.spec3(p, q, r) == ((not p) and (not r)), f"spec3{(p, q, r)}"
