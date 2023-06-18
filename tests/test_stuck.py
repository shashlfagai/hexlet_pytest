def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptines():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)
    stack.pop()
    assert not stack

import pytest

def test_pop_in_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()

