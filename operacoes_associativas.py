# coding: utf-8
"""Operações Associativas para um conjunto {a, b, c}"""

a, b, c = "a", "b", "c"
con = {a, b, c}


def is_assoc(op):
     for x in con:
         for y in con:
             for z in con:
                 if op(op(x, y), z) != op(x, op(y, z)):
                     return False
     return True


def all_ops():
    op = {a: {a: 0, b: 0, c: 0}, b: {a: 0, b: 0, c: 0}, c: {a: 0, b: 0, c:0}}
    for aa in con:
        op[a][a] = aa
        for ab in con:
            op[a][b] = ab
            for ac in con:
                op[a][c] = ac
                for ba in con:
                    op[b][a] = ba
                    for bb in con:
                        op[b][b] = bb
                        for bc in con:
                            op[b][c] = bc
                            for ca in con:
                                op[c][a] = ca
                                for cb in con:
                                    op[c][b] = cb
                                    for cc in con:
                                        op[c][c] = cc
                                        def _op(x, y):
                                            return op[x][y]
                                        yield _op


if __name__ == "__main__":
    count = {"true": 0, "false": 0}
    for o in all_ops():
        if is_assoc(o):
            count["true"] += 1
        else:
            count["false"] += 1

    print "Operações associativas:     {true}".format(**count)
    print "Operações não associativas: {false}".format(**count)


