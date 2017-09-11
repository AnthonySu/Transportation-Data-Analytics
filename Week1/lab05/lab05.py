## The linked list and trees implementations are included.

## Linked Lists ##

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def isempty(s):
    """Returns True iff s is the empty list."""
    return s is empty


def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    if linked_lst == empty:
        return []
    return [first(linked_lst)] + link_to_list(rest(linked_lst))


## Trees ##

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
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

def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    "*** YOUR CODE HERE ***"
    return tree(username, 
                [tree('pop', 
                    [tree('justin bieber', 
                        [tree('single', 
                            [tree('what do you mean?')])]), 
                    tree('2015 pop mashup')]), 
                tree('trance', [tree('darude', [tree('sandstorm')])])])


def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 1
    return sum([num_songs(branch) for branch in branches(t)])


def find(t, target):
    """Returns True if t contains a node with the value TARGET and False
    otherwise.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> find(my_account, 'korean')
    True
    >>> find(my_account, 'blank space')
    True
    >>> find(my_account, 'bad blood')
    False
    """
    "*** YOUR CODE HERE ***"
    if root(t) == target:
        return True

    if sum([find(branch, target) for branch in branches(t)]) > 0:
        return True

    return False

