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

def next(cur, repl):
    state = 'out'
    result = []
    for c in cur:
        state, new_c = next_state_c[(state, c)]
        if new_c == 'r':
            result.append(repl)
        else:
            result.append(new_c)
    return ''.join(result)

translation = [
    ('!!', 'b'),
    (': ', 'c'),
    ('"', 'd'),
    ("'", 's'),
    (' ', '_'),
]

def translate(s):
    for src, dest in translation:
        s = s.replace(src, dest)
    return s

def untranslate(s):
    for src, dest in reversed(translation):
        s = s.replace(dest, src)
    return s

def next_translate(cur, repl):
    return untranslate(next(translate(cur), translate(repl)))

a0 = """: '!!'"""
a1 = """: "!!" '!!'"""
a2 = next_translate(a1, a0)
a3 = next_translate(a2, a2) # Note: This is not a bug, but actual shell behaviour!
a4 = next_translate(a3, a3)
a5 = next_translate(a4, a4)
a6 = next_translate(a5, a5)
a7 = next_translate(a6, a6)

a = [a0, a1, a2, a3, a4, a5, a6, a7]

print
print 'Test result: ', [(i, a[i] == expected_a[i]) for i in xrange(len(expected_a))]
print

# Warning: Do not enable this unless you have at least 4 GiB of RAM!
#a8 = next_translate(a7, a7)
#a.append(a8)

print 'Number of characters:', [len(ai) for ai in a]
print 'Number of bangbangs: ', [ai.count('!!') for ai in a]
print
