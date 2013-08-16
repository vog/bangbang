Bangbang
========

This is a small Python script
with a small test suite
to analyze the "bangbang" question
outside the shell.

Background information:

* [Original Article: Bang Bang !!](http://shadabahmed.com/blog/2013/08/16/bang-bang) by Shadab Ahmed
* [Discussion on Hacker News](https://news.ycombinator.com/item?id=6223022)

More efficient implementation:

* [bangbang_counter.py](https://gist.github.com/robinhouston/6251775) by Robin Houston

Proposed sequence to OEIS:

* [A228162](https://oeis.org/draft/A228162)


Results
-------

Current results of this script:

    Number of bangbangs:  [1, 2, 2, 3, 5, 17, 161, 15681, 159591041, 16866847940875521]

This script uses a different internal representation
of singe quote, double quote, colon-space and bangbang
to allow for a slightly simpler implemenation.
Maybe this second representation also
allows for easier analysis.
