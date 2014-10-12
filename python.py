#!/usr/bin/env python

""" This is an example module

>>> get_camel_case('camel_case')
'CamelCase'

>>> get_camel_case('AlreadyCamelCase')
'Alreadycamelcase'
>>> is_prime(2)
True

"""


class First(object):
    def __init__(self, param):
        super(First, self).__init__()
        print "first", param


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print "second"


class Third(object):
    def __init__(self):
        super(Third, self).__init__()
        print "third"
    def do_something(self):
        print 'Third did something'


class Fourth(First, Second, Third):
    def __init__(self, param):
        Third.do_something(self)
        super(Fourth, self).__init__(param)
        print "that's it"


def is_prime(x):
    """ Doc string
    >>> [is_prime(n) for n in range(6)]
    [False, False, True, True, False, True]
    >>> is_prime(5003)
    True
    >>> is_prime('a')
    Traceback (most recent call last):
        ...
    TypeError: range() integer end argument expected, got str.
    """
    if x < 2:
        return False
    elif x == 2:
        return True
    for numbers in range(2, x):
        if x % numbers == 0:
            return False
    return True



class parent(object):
    def __init__(self, param):
        self.v1 = param

class child(parent):
    def __init__(self, param):
        super(child, self).__init__(param)
        self.v2 = param


def get_camel_case(camel_case):
    """Return the camelCase version of the parameter. This is the doc string.
    >>> get_camel_case('this_is_a_python_variable')
    'ThisIsAPythonVariable'
    """
    camel_case = camel_case.title()
    camel_case = camel_case.replace('_', '')
    return camel_case

if __name__ == "__main__":
    # ./python.py -v  to see output
    #import doctest
    #doctest.testmod()

    # x = None
    # sum = 0
    # while x != 0:
    #     x = raw_input('Enter an integer: ')
    #     sum += len(x)
    #     x = int(x)
    #     if 0 < x < 60:
    #         print 'its cold'
    #     elif 100 > x > 60:
    #         print 'its right'
    #     elif x > 100:
    #         print 'its hot'
    #     elif x == 0:
    #         break
    # print "you entered ", sum , "characters."

    c = child(11)
    print c.v1, c.v2
    # f = Fourth('hi')
    # print f.v1
    # print f.v2