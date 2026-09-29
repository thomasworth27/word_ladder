#!/bin/python3


from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.

    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472> for a discussion about a common memory management bug that causes the generated word ladders to be too long in some cases.
    '''
    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None

    with open(dictionary_file) as f:
        dictionary = set(f.read().split())
    dictionary.discard(start_word)

    stack = [start_word]
    queue = deque()
    queue.append(stack)

    while queue:
        stack = queue.popleft()
        for word in list(dictionary):
            if _adjacent(word, stack[-1]):
                if word == end_word:
                    return stack + [word]
                new_stack = stack.copy()
                new_stack.append(word)
                queue.append(new_stack)
                dictionary.remove(word)

    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    differences = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            differences += 1
            if differences > 1:
                return False
    return differences == 1
