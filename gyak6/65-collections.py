import collections

# https://docs.python.org/3/library/collections.html

jegyeim = [1, 3, 5, 5, 3, 2, 4, 5, 2, 2, 3, 4, 5, 5, 1, 5, 5, 3, 4, 3, 2, 1]

# Counter (ősosztálya a dict)
counter = collections.Counter(jegyeim)
print(counter.items())
print(counter.most_common())

counter.subtract([1, 1, 1])
print(counter)

# Deque
deque = collections.deque(["a", "b", "c"])
deque.append("d")
deque.appendleft("z")
print(deque)

deque.pop()
deque.popleft()
print(deque)
