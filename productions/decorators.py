from productions.utils import find_isomorphisms

def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G):
            isomorphism = None
            isomorphisms = find_isomorphisms(G, left_side)
            if len(isomorphisms) > 0:
                isomorphism = isomorphisms[0]
            return apply_fun(G, isomorphism=isomorphism)

        return inner
    return outer
