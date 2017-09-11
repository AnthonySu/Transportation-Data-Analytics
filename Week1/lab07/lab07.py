# Control
def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    if a == b:
        return True

    if a % 2 == 0 and b % 2 == 0:
        return True

    if a % 2 == 1 and b % 2 == 1:
        return False

    if a % 2 == 0 and b % 2 == 1:
        if a <= b*3+1:
            return True
        return False

    if a % 2 == 1 and b % 2 == 0:
        return same_hailstone(b, a)


def amicable(n):
    """Return the smallest amicable number greater than positive integer n.

    Every amicable number x has a buddy y different from x, such that
    the sum of the proper divisors of x equals y, and
    the sum of the proper divisors of y equals x.

    For example, 220 and 284 are both amicable because
    1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 is 284, and
    1 + 2 + 4 + 71 + 142 is 220

    >>> amicable(5)
    220
    >>> amicable(220)
    284
    >>> amicable(284)
    1184
    >>> r = amicable(5000)
    >>> r
    5020

    """
    "*** YOUR CODE HERE ***"
    '''def amicable_helper(x):
        total1 = 0
        for i in range(1, x//2+1):
            if x % i == 0:
                total1 += i
        total2 = 0
        for i in range(1, total1//2+1):
            if total1 % i == 0:
                total2 += i
        if total1 == x:
            return False
        elif total2 == x:
            return [x, total1]
        else: 
            return False

    temp = amicable_helper(n)
    if temp == False:
        return amicable(n+1)
    elif min(temp) < n:
        return amicable(n+1)
    elif min(temp) == n:
        return max(temp)
    else:
        return min(temp)'''


    def compute_amicable(x):
        result = 0
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                result = result + i
        return result

    temp = compute_amicable(n + 1)
    if n + 1 == compute_amicable(temp) and n + 1 != temp:
        return n + 1
    else:
        return amicable(n + 1)


# HOF
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        def fu(result):
            quotient = x // 3
            remainder = x % 3

            while quotient > 0:
                result = f3(f2(f1(result)))
                quotient = quotient - 1
            if remainder == 0:
                result = result
            elif remainder == 1:
                result = f1(result)
            else:
                result = f2(f1(result))
            return result
        return fu
    return f


# Recursion
def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    >>> part(10)
    42
    >>> part(15)
    176
    >>> part(20)
    627
    """
    "*** YOUR CODE HERE ***"
    def part_helper(a, b):
        if a == 0:
            return 1
        elif a < 0 or b <= 0:
            return 0
        else:
            return part_helper(a-b, b) + part_helper(a, b - 1)

    return part_helper(n, n)



def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    "*** YOUR CODE HERE ***"
    '''def f(weights, values, c, total):
        if min(weights) > c:
            return total

        for i in range(len(weights)):
            weight, value = weights[i], values[i]
            if weight < c:
                del weights[i]
                del values[i]
                f(weights, values, c - weight, total + value)

    return knapsack(weights, values, c, 0)'''

    if weights == []:
        return 0

    else:
        weight1, weight2= weights[0], weights[1:]
        value1, value2 = values[0], values[1:]
        with_first = value1 + knapsack(weight2, value2, c - weight1)
        without_first = knapsack(weight2, value2, c)

        if weight1 <= c:
            return max(with_first, without_first)
        return without_first


# Trees
# Tree definition

def tree(root, branches=[]):
    """Construct a tree with the given root value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    """Return the root value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(root(t), [tree(i) for i in vals])

    return tree(root(t), [sprout_leaves(branch, vals) for branch in branches(t)])


# Lists
def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a list of sequences, each
    corresponding to a group.

    >>> group(range(14))
    [range(0, 4), range(4, 9), range(9, 14)]
    >>> group(list(range(17)))
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15, 16]]
    """
    num = len(seq)
    assert num >= 12
    "*** YOUR CODE HERE ***"
    if num % 4 == 0:
        return [seq[i:i+4] for i in range(num) if i%4==0]
    elif num % 4 == 1:
        return [seq[i:i+4] for i in range(num - 5) if i%4==0] + [seq[-5:]]
    elif num % 4 == 2:
        return [seq[i:i+4] for i in range(num - 10) if i%4==0] + [seq[-10:-5]] + [seq[-5:]]
    elif num % 4 == 3:
        return [seq[i:i+4] for i in range(num - 15) if i%4==0] + [seq[-15:-10]]+ [seq[-10:-5]] + [seq[-5:]]


def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    >>> x = []
    >>> for i in range(100):
    ...     x = [x] + [i]       # very deep list
    ...
    >>> deep_len(x)
    100
    """
    "*** YOUR CODE HERE ***"
    '''if lst == empty:
        return 0

    length = 0
    for i in range(len(lst)):
        if type(lst[i]) == list:
            length += deep_len(lst[i])
        else:
            length += 1 

    return length'''
    if not isinstance(lst, list):
        return 1
    else:
        return sum([deep_len(e) for e in lst])


# Linked Lists
# Linked List abstraction

empty = 'X'

def link(first, rest=empty):
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(lnk):
    assert is_link(lnk), 'first only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no first element.'
    return lnk[0]

def rest(lnk):
    assert is_link(lnk), 'rest only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no rest.'
    return lnk[1]

def is_link(lnk):
    return lnk == empty or \
        type(lnk) == list and len(lnk) == 2 and is_link(lnk[1])

# Useful print_link function, used for testing.

def print_link(lnk):
    """Prints out a non-deep linked list."""
    line = ''
    while lnk != empty:
        if line:
            line += ' '
        line += str(first(lnk))
        lnk = rest(lnk)
    print('<{}>'.format(line))

def deep_reverse(lnk):
    """Return a reversed version of a possibly deep linked list lnk.

    >>> print_link(deep_reverse(empty))
    <>
    >>> print_link(deep_reverse(link(1, link(2, empty))))
    <2 1>

    >>> deep = link(1, link(link(2, link(3, empty)), empty))
    >>> deep_reversed = deep_reverse(deep)
    >>> print_link(first(deep_reversed))
    <3 2>
    >>> first(rest(deep_reversed))
    1
    >>> rest(rest(deep_reversed)) == empty
    True

    """
    "*** YOUR CODE HERE ***"
    deep_reversed = empty
    while lnk != empty:
        elem = first(lnk)
        if is_link(elem):
            deep_reversed = link(deep_reverse(elem), deep_reversed)
        else:
            deep_reversed = link(elem, deep_reversed)
        lnk = rest(lnk)

    return deep_reversed



