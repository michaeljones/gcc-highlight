
G++ Highlighter
===============

A simple python & pygments based highligher for the output from G++.
The available alternatives I could find tended to be massively complicated
contraptions in C++ or Perl.

Only tested with C++ compilation output, no other flavours of gcc.

How to
------

Colour highlighting achieved in a bash shell with::

   g++ <compiler arguments and flags> | python /path/to/gcc-colour.py

Requirements
------------

- Python
- Pygments



