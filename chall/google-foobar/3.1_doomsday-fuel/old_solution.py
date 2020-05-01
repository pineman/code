# -*- coding: utf-8 -*-

import copy
from fractions import Fraction, gcd


# Fazer uma lista de caminhos (tuples), ignorando self-jumps e backtracking.
# Se um caminho é acessível sem backtracking, também será com.
# I just implemented depth first search didn't I
def find_paths(m, paths, cur_state=0, cur_path=None):
    if cur_path is None:
        cur_path = []

    cur_path.append(cur_state)

    next_states = m[cur_state]
    # Ignore self-jumps
    m[cur_state][cur_state] = 0

    if sum(next_states) == 0:
        # Completed cur_path, found terminal state.
        paths[cur_path[-1]].append(cur_path)
        return

    for next_state, n in enumerate(next_states):
        if n == 0:
            continue
        # Ignore backtracking. TODO: this doesn't work. :)
        ign_backtrack = False
        for past_state in cur_path:
            if m[next_state][past_state] != 0:
                ign_backtrack = True
        if ign_backtrack:
            continue
        # New path found, but not complete yet.
        find_paths(m, paths, next_state, copy.deepcopy(cur_path))


def convert_exact_rational(m):
    for i, state in enumerate(m):
        den = sum(state)
        if den == 0:
            continue
        for j, n in enumerate(state):
            if n == 0:
                continue
            m[i][j] = Fraction(m[i][j], den)

    # Correct for self-jump
    for i, next_states in enumerate(m):
        if next_states[i] == 0:
            continue
        num_next = len([n for n in next_states if n != 0])
        self_jump_correction = Fraction(
            next_states[i].numerator, next_states[i].denominator * (num_next - 1)
        )
        next_states[i] = 0
        for next_state, n in enumerate(next_states):
            if n == 0:
                continue
            m[i][next_state] += self_jump_correction

    # Correct for backtracking
    for i, next_states in enumerate(m):
        for j, fwd_prob in enumerate(next_states):
            if fwd_prob == 0:
                continue
            if m[j][i] == 0:
                continue
            # Found that i, j are a backtracking pair.
            backtracking_correction = Fraction(1, 1 - (m[i][j] * m[j][i]))
            for x, n in enumerate(m[i]):
                if n == 0:
                    continue
                m[i][x] *= backtracking_correction
            m[j][i] = 0


def calc_path_prob(m, path, count=0):
    cur_state = path[count]
    next_states = m[cur_state]

    if sum(next_states) == 0:
        return 1
    count += 1
    return next_states[path[count]] * calc_path_prob(m, path, count)


def solution(m):
    __import__("sys").setrecursionlimit(9999999)
    # m is a square matrix, at most 10 by 10.
    if len(m) == 1:
        return [1, 1]

    paths = [[] for _ in range(len(m))]
    find_paths(copy.deepcopy(m), paths)

    convert_exact_rational(m)
    t = []
    for end, paths in enumerate(paths):
        if not paths and sum(m[end]) != 0:
            continue  # not a terminal node
        r = 0
        for path in paths:
            r += calc_path_prob(m, path)
        t.append(r)

    den = 1
    for x in t:
        den = gcd(r, x)
    for i in range(len(t)):
        t[i] = (t[i] * den.denominator).numerator
    t.append(den.denominator)
    return t


print "test one", "=" * 50
one = solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)
print one
print one == [7, 6, 8, 21]

print "test two", "=" * 50
two = solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)
print two
print two == [0, 3, 2, 9, 14]

print "test three", "=" * 50
three = solution(
    [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)
print three
print three == [1, 2, 3]

print "test four", "=" * 50
four = solution([[0]])
print four
print four == [1, 1]

print "test five", "=" * 50
five = solution(
    [
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print five
print five == [1, 2, 3, 4, 5, 15]

print "test six", "=" * 50
six = solution(
    [
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print six
print six == [4, 5, 5, 4, 2, 20]

print "test seven", "=" * 50
seven = solution(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print seven
print seven == [1, 1, 1, 1, 1, 5]

print "test eight", "=" * 50
eight = solution(
    [
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print eight
print eight == [2, 1, 1, 1, 1, 6]

print "test nine", "=" * 50
nine = solution(
    [
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print nine
print nine == [6, 44, 4, 11, 22, 13, 100]

print "test ten", "=" * 50
ten = solution(
    [
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
print ten
print ten == [1, 1, 1, 2, 5]
