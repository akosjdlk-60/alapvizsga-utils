from dataclasses import make_dataclass


def create_class(cls_name = "ClassName", *field_names) -> type:
    """
    Paraméterek
    -----
    name: :class:`str`
        A class neve.
    *field_names: :class:`list[(str, type), (str, type), ...]`
        A Class attribútumainak listája és ezek típusa

    Return
    -----
    -> Class

    Példa
    ------
    ::

        Alma = create_class(name="Alma", [("fajta", str), ("szarm_orszag", str), ("termek_kod", int)])
        golden = Alma("golden", "Magyarország", 767254)

        print(golden) -> 'Alma(golden, Magyarország, 767254)'
        print(golden.fajta) -> "golden"
    """
    cls = make_dataclass(cls_name, *field_names, slots=True)
    return cls

def max_from_iter(iterable: [tuple | dict | list | set]) -> [int, int]:
    """
    Visszaadja az iterable legmagasabb értékét, és annak indexét.

    Paraméterek
    -----
    iterable: :class:`tuple | dict | list | set`

    Return
    -----
    -> [index, ]

    Példa
    ------
    ::

        Alma = create_class(name="Alma", [("fajta", str), ("szarm_orszag", str), ("termek_kod", int)])
        golden = Alma("golden", "Magyarország", 767254)

        print(golden) -> 'Alma(golden, Magyarország, 767254)'
        print(golden.fajta) -> "golden"
    """
