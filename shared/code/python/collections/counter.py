import collections


counter = collections.Counter()
counter.update(
    "Elle avait épousé un beau garçon sans fortune, mort au "
    "commencement de 1809, en lui laissant deux enfants très jeunes "
    "avec une quantité de dettes."
)
counter.most_common(5)
