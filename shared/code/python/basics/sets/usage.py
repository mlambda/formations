my_set = set()  # Création d'un ensemble vide
my_set = {"a"}  # Création d'un ensemble avec éléments
my_set = set(["a"])  # Création à partir d'un itérable
my_set.add("b")  # my_set vaut maintenant {"a", "b"}
my_set.update(["c", "d"])  # my_set vaut maintenant {"a", "b", "c", "d"}
"a" in my_set  # True
"e" in my_set  # False
my_set | {"e", "f"}  # {"a", "b", "c", "d", "e", "f"}
my_set & {"a", "e"}  # {"a"}
my_set - {"a", "e"}  # {"b", "c", "d"}
my_set ^ {"a", "e"}  # {"b", "c", "d", "e"}
my_set < {"a", "b", "c", "d", "e"}  # True
my_set < {"a", "b", "c", "d"}  # False
my_set <= {"a", "b", "c", "d"}  # True
