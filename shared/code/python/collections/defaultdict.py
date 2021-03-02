import collections


colors = collections.defaultdict(set)
colors["Mésange"].update(["bleu", "blanc", "jaune"])
print(colors)
