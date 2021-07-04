strings = ['a', 'b', 'c', 'd']

strings[2]

#push
strings.append('e') #O(1)

#pop
strings.pop() #O(1)
strings.pop()

#insert(pos, element)
strings.insert(0, 'x') #O(n)
strings.insert(2, 'alien')

#remove(element)
strings.remove('alien')

print(strings)