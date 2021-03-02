import collections


colors = collections.deque(maxlen=2)
colors.append("bleu")
colors.appendleft("blanc")
colors.append("jaune")
print(colors)
