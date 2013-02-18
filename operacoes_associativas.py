# coding: utf-8
"""Operações Associativas para um conjunto {a, b, c}"""


class GroupFactory():

    def __init__(self, _set):
        """Use a set to create groups."""
        self._set = set(_set)

    def all_ops(self):
        """Generator to iterate over all possible operations."""
        op_table = {}

        for x in self._set:
            op_table[x] = {}
            for y in self._set:
                op_table[x][y] = None

        _iter_list = list(self._set)
        _iter_last = len(_iter_list) - 1

        def _next_pair(i, k):
            if i < _iter_last:
                i = i + 1
            else:
                i = 0
                if k < _iter_last:
                    k = k + 1
                else:
                    i = _iter_last
                    return None
            return (i, k)

        def _iter_table(i, k):
            x = _iter_list[i]
            y = _iter_list[k]
            for ele in self._set:
                op_table[x][y] = ele
                next_pair = _next_pair(i, k)
                if next_pair is not None:
                    for op in _iter_table(*next_pair):
                        yield op
                else:
                    def _op(x, y):
                        return op_table[x][y]
                    yield _op

        return _iter_table(0, 0)

    def is_assoc(self, op):
        """True if the operation op is associative."""
        for x in self._set:
            for y in self._set:
                for z in self._set:
                    if op(op(x, y), z) != op(x, op(y, z)):
                        return False
        return True

    def count_assoc_ops(self):
        """Returns a dict {'assoc': number_of_assoc_ops, 'other': non_assoc_ops}.

        The complexity of this algorithm is O(n ** (2 + n ** 2)), that is,
        for a group of size 3, the time is proportional to 177147, while
        for a gruop of size 4, the time is proportional to 68719476736.

        It is not feasible to run this for a group of size 4 or larger.
        """
        count = {"assoc": 0, "other": 0}
        for op in self.all_ops():
            if self.is_assoc(op):
                count['assoc'] += 1
                print count['assoc']
            else:
                count['other'] += 1
        return count

if __name__ == "__main__":
    group = GroupFactory([1, 2, 3])
    count = group.count_assoc_ops()

    print('Associatives:     {assoc}'.format(**count))
    print('Non-Associatives: {other}'.format(**count))


