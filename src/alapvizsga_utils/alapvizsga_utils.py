from dataclasses import dataclass
from typing import Any
from os import system as cmd
from os import name as os_name

__all__ = ( # ezeket fogja importálni, ha     `from alapvizsga_utils import *`
    "easy_class",
    "clear_screen",
    "is_numeric",
    "remove_non_numeric",
    "max_from_iter",
    "min_from_iter",
    "most_common",
    "is_in_inter",
    "endswith",
    "read_from_file",
    "remove_duplicates",
    "update_class_values",
    "write_to_file",
    "search_class_list",
    "class_list_atlag"
)

def easy_class(cls=None) -> type:
    """
    ### Paraméterek
    -----
    ## \-

    ### Return
    -----
    -> Class

    ### Példa
    -------
    ::
        
        @easy_class
        class Alma:
            fajta: str
            darab: int
            cikksz: int

        alma = Alma("gold", 10, 123)
        print(alma) -> Alma(fajta='gold', darab=10, cikksz=123)

        
    """
    
    return dataclass(cls, init = True, repr=True, eq=True, order = False, unsafe_hash = False, frozen = False, match_args=True, kw_only=False, slots=True, weakref_slot = False)

def clear_screen():
    cmd('cls' if os_name == 'nt' else 'clear')

def is_numeric(value: Any) -> None | float | int:
    """
    Megvizsgálja, hogy a paraméterként kapott érték szám-e.

    ### Paraméterek
    -----
    value: :class:`any`

    ### Return
    -----
    -> :class:`None`
    -> :class:`float`
    -> :class:`int`

    ### Példa
    ------
    ::
    
        print(is_numeric(10)) -> True\n
        print(is_numeric("10")) -> True\n
        print(is_numeric(10.0)) -> True\n
        print(is_numeric("10.0")) -> True\n
        print(is_numeric("alma")) -> False
    """
    try:
        return float(value)
    except:
        try:
            return int(value)
        except:
            return None

def remove_non_numeric(iterable: tuple | dict | list | set) -> list | None:
    """
    Visszaadja az iterable-ből az összes számot.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`

    ### Return
    -----
    -> :class:`list`
    -> None (Ha az iterable nem tartalmaz class:`int`-et vagy :class:`float`-ot)

    ### Példa
    ------
    ::

        x = remove_non_numeric([10,312,"alma",4])
        print(x) -> [10, 312, 4]

        x = remove_non_numeric(dict(a=10, b=312, c="alma", d=4))
        print(x) -> [10, 312, 4]
    """
    if isinstance(iterable, (tuple, list, set)):
        return iterable, [x for x in iterable if is_numeric(x)]
    elif isinstance(iterable, dict):
        return iterable, {x: y for x, y in iterable.items() if is_numeric(y)}
    else: return iterable, None

def max_from_iter(iterable: tuple | dict | list | set) -> list | None:
    """
    Visszaadja az iterable legmagasabb értékét, és annak indexét.
    Ha az iterable nem tartalmaz :class:`int`-et vagy :class:`float`-ot, akkor None-t ad vissza.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`

    ### Return
    -----
    -> [index: :class:`str` | :class:`int`, value: :class:`int` | :class:`float`]\n
    -> None (Ha az iterable nem tartalmaz class:`int`-et vagy :class:`float`-ot)

    ### Példa
    ------
    ::

        x = max_from_iter(list[10,312,412,4])
        print(x) -> [2, 412]

        x = max_from_iter(dict(a=10, b=312, c=412, d=4))
        print(x) -> ['c', 412]
    """
    original, iterable = remove_non_numeric(iterable)
    if len(iterable) == 0:
        return None
    
    if isinstance(original, (tuple, list)):
        return max(iterable)
    
    elif isinstance(original, dict):
        return max(iterable.values())

    else: return None

def min_from_iter(iterable: tuple | dict | list | set) -> list | None:
    """
    Visszaadja az iterable legkisebb értékét, és annak indexét.
    Ha az iterable nem tartalmaz :class:`int`-et vagy :class:`float`-ot, akkor None-t ad vissza.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`

    ### Return
    -----
    -> [index: :class:`str` | :class:`int`, value: :class:`int` | :class:`float`]\n
    -> None (Ha az iterable nem tartalmaz class:`int`-et vagy :class:`float`-ot)

    ### Példa
    ------
    ::
    
        x = min_from_iter(list[10,312,412,4])
        print(x) -> [3, 4]

        x = min_from_iter(dict(a=10, b=312, c=412, d=4))
        print(x) -> ['d', 4]
    """
    
    original, iterable = remove_non_numeric(iterable)
    if len(iterable) == 0:
        return None
    
    if isinstance(original, (tuple, list)):
        return min(iterable)
    
    elif isinstance(original, dict):
        return min(iterable.values())

    else: return None

def most_common(iterable: tuple | dict | list | set) -> Any:
    """
    Visszaadja az iterable-ben leggyakrabban előforduló elemet.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`

    ### Return
    -----
    -> :class:`Any`

    ### Példa
    ------
    ::
    
        print(most_common([1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 7])) -> 4\n
        print(most_common([1, 2, 3, 4, 5, 6, 7])) -> 1\n
        print(most_common([1, "asd", 3, 4, 5, "asd", 7])) -> "asd"\n
        print(most_common(dict(a=999, b=312, c=312, d="312", e = "999", f = "999", g = "999"))) -> 999\n
        print(most_common(dict(a=999, b=312, c=312, d="312", e = "999", f = 999, g = 999))) -> 999\n
        print(most_common(dict(a=999, b="312", c="312", d="312", e = "312", f = 999, g = 999))) -> 312
    """

    if isinstance(iterable, (tuple, list, set)): return max(list(iterable), key=iterable.count)
    
    if isinstance(iterable, dict):
        
        return max([int(value) if is_numeric(value) else str(value) for value in iterable.values()], key=[int(value) if is_numeric(value) else str(value) for value in iterable.values()].count)

def is_in_inter(iterable: tuple | dict | list | set, value: Any) -> bool:
    """
    Megvizsgálja, hogy a value benne van-e az iterable-ben.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`
    value: :class:`Any`

    ### Return
    -----
    -> :class:`bool`

    ### Példa
    ------
    ::

        print(is_in_inter([10, 312,"alma", 4], 10)) -> True\n
        print(is_in_inter([10, 312,"alma", 4], 11)) -> False\n
        print(is_in_inter(dict(a=10, b=312, c="alma", d=4), 10)) -> True
    """
    if isinstance(iterable, (tuple, list, set)):
        return value in iterable

    if isinstance(iterable, dict):
        return value in iterable.values()

def endswith(value: str, suffix: str) -> bool:
    """Visszaadja, hogy a value a suffix string-gel végződik-e.

    Paraméterek
    -----
    value: :class:`str`
    suffix: :class:`str`

    ### Return
    -----
    -> :class:`bool`
    -> True

    ### Példa
    ------
    ::
        print(endswith("alma.txt", ".txt")) -> True\n
        print(endswith("alma.txt", "txt")) -> True\n
        print(endswith("alma.txt", ".csv")) -> False
    """
    return value[-len(suffix):] == suffix
    
def read_from_file(path: str, delimiter: str = ",", ignore_first_line: bool = True, cls: type | None = None, debug: bool = False) -> list[type | list[str]]:
    """
    Beolvassa a fájlt, és visszaadja a tartalmát, opcionálisan class-t is létrehoz.

    ### Paraméterek
    -----
    path: :class:`str`
        A fájl elérési útja.
    delimiter: :class:`str`
        A fájlban használt elválasztó karakter.
    ignore_first_line: :class:`bool`
        Ha True, akkor az első sort nem olvassa be.
    cls: :class:`type` | None
        Ha nem None, akkor létrehoz egy class-t, és az adatokat ebbe a class-ba olvassa be.

    ### Return
    -----
    -> :class:`list[Class]`
    -> :class:`list[list[str, str, ...]]`

    ### Példa
    ------
    ::
        # data.txt => fajta,darab,cikksz\n
        class_list = read_from_file("data", ignore_first_line=True, cls=make_dataclass("Alma", [("fajta", str), ("darab", int), ("cikksz", int)])

        # data.csv => fajta;darab;cikksz\n
        class_list = read_from_file("data", delmimiter=True,)
    """
    if not endswith(path, ".csv") and not endswith(path, ".txt"):
        path += ".txt"
        
    with open(path, "r", encoding="utf-8") as f:
        if ignore_first_line:
            f.readline()
        lines = f.readlines()
        data = [line.strip().split(delimiter) for line in lines]
        if debug: print(data)
        if cls:
            data = [cls(*[int(y) if is_numeric(y) else str(y) for y in x]) for x in data]
            if debug: print(data)
        return data

def remove_duplicates(iterable: tuple | dict | list | set) -> list:
    """
    Eltávolítja az iterből a duplikált elemeket, a sorrendet megtartva.

    ### Paraméterek
    -----
    iterable: :class:`tuple` | :class:`dict` | :class:`list` | :class:`set`

    ### Return
    -----
    -> :class:`list`

    ### Példa
    ------
    ::

        print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7])) -> [1, 2, 3, 4, 5, 6, 7]\n
        print(remove_duplicates([1, 2, 3, 4, 5, 6, 7])) -> [1, 2, 3, 4, 5, 6, 7]\n
        print(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) -> [1]\n
        print(remove_duplicates({"x": 1, "a": 1, "y": 5})) -> {'a': 1, 'y': 5}
    """
    
    removed_indexes = []
    original = iterable
    if isinstance(iterable, dict):
        iterable = list(iterable.values())
    
    for index, x in enumerate(iterable):
        while iterable.count(x) > 1: iterable.remove(x), removed_indexes.append(index)

    if isinstance(original, dict):
        for index in removed_indexes:
            original.pop(list(original.keys())[index])
        return original
    return iterable

def search_class_list(class_list: list[type], key: str | None, value: Any | None) -> list:
    """
    Visszaadja azokat az elemeket, amelyeknek a key attribútuma megegyezik a value-val.

    ### Paraméterek
    -----
    class_list: :class:`list[type]`
    key: :class:`str` | None
    value: :class:`Any` | None

    ### Return
    -----
    -> :class:`list[type]`

    ### Példa
    ------
    ::

        # Alma(szin, szarm_orszag, ar)
        class_list = [Alma("gold", "Magyarország", 234), Alma("gold", "Németország", 423), Alma("red", "Magyarország", 533), Alma("green", "Magyarország", 754)]
        print(search_class_list(class_list, "szin", "gold")) -> [Alma("golden", "Magyarország", 234), Alma("gold", "Németország", 423)]
    """
    return [x for x in class_list if getattr(x, key) == value]

def class_list_atlag(class_list: list[type], key: str) -> float:
    """
    Visszaadja a class_list átlagát a key attribútum alapján.

    ### Paraméterek
    -----
    class_list: :class:`list[type]`
    key: :class:`str`

    ### Return
    -----
    -> :class:`float`

    ### Példa
    ------
    ::
        # Alma(szin, szarm_orszag, ar)
        class_list = [Alma("gold", "Magyarország", 234), Alma("red", "Magyarország", 533), Alma("green", "Magyarország", 754)]
        print(class_atlag(class_list, "ar")) -> 507.0
    """
    return sum([getattr(x, key) for x in class_list]) / len(class_list)

def write_to_file(file_name_and_path: str, class_list: list[type], schema: list[list], header_line: str | None = None) -> None:
    """
    Kiírja a class_list tartalmát a file_name_and_path-ba.

    ### Paraméterek
    -----
    file_name_and_path: :class:`str`
        A file neve és elérési útja.
    class_list: :class:`list[type]
        A class-ok listája.
    schema: :class:`list[attr, delimiter, attr]` => ["name", ";", "salary"]
        A class attribútumainak sorrendje és elválasztó karaktere.
    header_line: :class:`str` | None =>
        A fájl első sora, ha None, akkor nem ír fejlécet.
    """

    with open(file_name_and_path, "w", encoding="utf-8") as file:
        if header_line: file.write(header_line + "\n")
        [file.write(f"{getattr(x, schema[0])}{schema[1]}{getattr(x, schema[2])}\n") for x in class_list]

def update_class_values(object: type, key: str, value: Any) -> type:
    """
    Frissíti a class attribútumát.

    ### Paraméterek
    -----
    object: :class:`type`
        A class.
    key: :class:`str`
        Az attribútum neve.
    value: :class:`Any`
        Az attribútum új értéke.

    ### Return
    -----
    -> :class:`type`

    ### Példa
    ------
    ::

        # Alma(szin, szarm_orszag, ar)
        class_list = [Alma("gold", "Magyarország", 234), Alma("red", "Magyarország", 533), Alma("green", "Magyarország", 754)]
        print(update_class_values(class_list[0], "ar", 999)) -> Alma("gold", "Magyarország", 999)
    """
    try:
        setattr(object, key, value)
    except Exception as e:
        print("Hiba történt a frissítés során:", e)

    return object




    
#                                                Unit tests
"""----------------------------------------------------------------------------------------------------"""
def unit_test():
    passing = 0
    failing = 0
    def test(res, expected_return) -> bool:
        nonlocal passing, failing
        result = res == expected_return
        if result: passing += 1
        else: failing += 1

        print(f"| {str(result).center(50)} |\t {str(expected_return).center(50)} | {str(res).center(50)} |")
        return

    clear_screen()
    print("Unit tests".center(162))
    print('--------------------------------------------------------'.center(162))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    test(is_numeric(10), 10.0)
    test(is_numeric("10"), 10.0)
    test(is_numeric(10.0), 10.0)
    test(is_numeric("10.0"), 10.0)
    test(is_numeric("alma"), None)

    test(max_from_iter([10,312,412,4]), 412)
    test(max_from_iter(dict(a=10, b=312, c=412, d=4)), 412)
    test(max_from_iter([10, 312, "alma", 4]), 312)
    test(max_from_iter(dict(a=10, b=312, c="alma", d=4)), 312)
    test(max_from_iter({"one": "string"}), None)

    test(min_from_iter([10,312,412,4]), 4)
    test(min_from_iter(dict(a=10, b=312, c=412, d=4)), 4)
    test(min_from_iter([10, 312, "alma", 4]), 4)
    test(min_from_iter(dict(a=10, b=312, c="alma", d=4)), 4)
    test(min_from_iter({"one": "string"}), None)

    test(endswith("alma.txt", ".txt"), True)
    test(endswith("alma.txt", "txt"), True)
    test(endswith("alma.txt", ".csv"), False)

    test(remove_non_numeric([10,312,"alma",4])[1], [10, 312, 4])
    test(remove_non_numeric(dict(a=10, b=312, c="alma", d=4))[1], {'a': 10, 'b': 312, 'd': 4})

    test(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
    test(remove_duplicates([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
    test(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1])
    test(remove_duplicates({"x": 1, "a": 1, "y": 5}), {'a': 1, 'y': 5})

    test(most_common([1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 7]), 4)
    test(most_common([1, 2, 3, 4, 5, 6, 7]), 1)
    test(most_common([1, "asd", 3, 4, 5, "asd", 7]), "asd")
    test(most_common(dict(a=999, b=312, c=312, d="312", e = "999", f = "999", g = "999")), 999)
    test(most_common(dict(a=999, b=312, c=312, d="312", e = "999", f = 999, g = 999)), 999)
    test(most_common(dict(a=999, b="312", c="312", d="312", e = "312", f = 999, g = 999)), 312)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('--------------------------------------------------------'.center(162))
    print(f"Total: {passing + failing} | Passing: {passing} ({int(passing / (passing + failing) * 100)}%)".center(162))
    print("\n")
    
if __name__ == "__main__":
    unit_test()
    # print(class_list := read_from_file("data", ignore_first_line=True, cls=create_class("Alma", [("fajta", str), ("darab", int), ("cikksz", int)])))

