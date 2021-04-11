my_dict = {}  # Création d'un dictionnaire vide
my_dict = {"a": 1, "b": 2}  # Création d'un dictionnaire avec éléments
my_dict = dict([("a", 1), ("b", 2)])  # Création à partir d'un itérable
my_dict = dict(a=1, b=2)  # Création par arguments mots-clefs
my_dict["c"] = 3  # my_dict vaut maintenant {"a": 1, "b": 2, "c": 3}
my_dict["a"]  # 1
"a" in my_dict  # True
"d" in my_dict  # False
1 in my_dict  # False
my_dict.keys()  # dict_keys(['a', 'b', 'c'])
my_dict.values()  # dict_values([1, 2, 3])
my_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for k, v in my_dict.items():
    print(k, v)
