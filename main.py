#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

with open("enable1.txt", "r") as f:
    # All uppercase
    REAL_WORDS = set(map(lambda x: x.strip().upper(), f.readlines()))

CHARS = {n: chr(n + 64) for n in xrange(1, 27)}


def is_valid(s):
    """
    Check if a string is a real word or a string of real words.
    Get all substrings from 1 to len(s), check which are words,
    and pass the rest to is_valid().

    A string is valid if we reach a point where s is "" or a real word.

    The string also may not be a real sentence. It just needs to contain
    only real words.
    """
    if s is "" or s in REAL_WORDS:
        return True
    for i in xrange(1, len(s)):
        if s[:i] in REAL_WORDS and is_valid(s[i:]):
            return True
    return False


def trimmed_digits(n, digits):
    """
    Get the first digits of a number.
    return:
        the trimmed digits in a tuple
    """
    assert digits >= 0
    s = str(n)
    head = int(s[:digits])
    rest = None if digits >= len(s) else int(s[digits:])
    return head, rest


def decode(n, buff="", use_rw=False):
    """
    Given an int n, and a buffer to append the decoded output
    to, parse the first digits of the int, append it to the buffer,
    and call decode recursively.
    """
    l = []
    if n is None:
        if not use_rw or is_valid(buff):
            l.append(buff)
        return l

    # Cover both case in which you only get the first digit
    # and possibly get the first 2 digits.
    head1, rest = trimmed_digits(n, 1)
    if head1 in CHARS:
        l += decode(rest, buff + CHARS[head1], use_rw=use_rw)
    head2, rest = trimmed_digits(n, 2)
    if head2 in CHARS:
        l += decode(rest, buff + CHARS[head2], use_rw=use_rw)
    return set(l)


def main():
    if len(sys.argv) < 2:
        print("Usage: python {} int".format(*sys.argv), file=sys.stderr)
        return 1

    n = int(sys.argv[1])
    print("Regular:", decode(n, use_rw=False))
    print("Using real words:", decode(n, use_rw=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
