#!/usr/bin/env python

'''Bangbang'''

__copyright__ = '''\
Copyright (C) 2013  Volker Grabsch <v@njh.eu>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

import sys

from expected import expected_a

s = set()

next_state_c = {
    ('dbl', '_'): ('dbl', '_'),
    ('dbl', 'b'): ('dbl', 'r'),
    ('dbl', 'c'): ('dbl', 'c'),
    ('dbl', 'd'): ('out', 'd'),
    ('dbl', 's'): ('dbl', 's'),
    ('out', '_'): ('out', '_'),
    ('out', 'b'): ('out', 'r'),
    ('out', 'c'): ('out', 'c'),
    ('out', 'd'): ('dbl', 'd'),
    ('out', 's'): ('sgl', 's'),
    ('sgl', '_'): ('sgl', '_'),
    ('sgl', 'b'): ('sgl', 'b'),
    ('sgl', 'c'): ('sgl', 'c'),
    ('sgl', 'd'): ('sgl', 'd'),
    ('sgl', 's'): ('out', 's'),
}

def next_noreplace(cur):
    result = ''
    state = 'out'
    for i, c in enumerate(cur):
        if i % 1000000 == 0:
            sys.stderr.write('%.2f%%    \r' % (i * 100.0 / len(cur),))
        state, new_c = next_state_c[(state, c)]
        result = result + new_c
    sys.stderr.write('           \r')
    return result

def next(cur, repl):
    return next_noreplace(cur).replace('r', repl)

def next_count_b(cur, repl):
    cur_b = cur.count('b')
    next_string = next_noreplace(cur)
    next_b = next_string.count('b')
    next_r = next_string.count('r')
    return next_b + (next_r * cur_b)

translate_char = {
    'b': '!!',
    'c': ': ',
    'd': '"',
    's': "'",
    '_': ' ',
}

def translate(s):
    return ''.join(translate_char[c] for c in s)

a0 = 'csbs'
a1 = 'cdbd_sbs'
a2 = next(a1, a0)
a3 = next(a2, a2) # Note: This is not a bug, but actual shell behaviour!
a4 = next(a3, a3)
a5 = next(a4, a4)
a6 = next(a5, a5)
a7 = next(a6, a6)
a8 = next(a7, a7)

a = [a0, a1, a2, a3, a4, a5, a6, a7, a8]

assert [translate(ai) for ai in a[:len(expected_a)]] == expected_a
assert all(next_count_b(a[i-1], a[i-1]) == a[i].count('b') for i in xrange(3, len(a)))

a9_count_b = next_count_b(a8, a8)

counts_b = [ai.count('b') for ai in a] + [a9_count_b]
print
print 'Number of bangbangs: ', counts_b
print
