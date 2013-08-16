Bangbang
========

This is a small Python script
with a small test suite
to analyze the "bang-bang" question
outside the shell.

More information:

* [Original Article: Bang Bang !!](http://shadabahmed.com/blog/2013/08/16/bang-bang)
* [Discussion on Hacker News](https://news.ycombinator.com/item?id=6223022)

Current results:

    Number of characters: [6, 11, 15, 28, 54, 210, 2082, 203842, 2074683522]
    Number of bangbangs:  [1, 2, 2, 3, 5, 17, 161, 15681, 159591041]

This script uses a different internal representation
of singe quote, double quote, colon-space and bangbang
to allow for a slightly simpler implemenation.
Maybe this second representation also
allows for easier analysis.
