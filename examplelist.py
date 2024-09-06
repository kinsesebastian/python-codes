num = [1, 2, 3]
print(num)
ani = ['cat', 'bat', 'rat', 'elephant']
print(ani)
mix = ['hello', 3.1415, True, None, 42]
print(mix)
spam = ['cat','bat','rat','elephant']
print(spam[0])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] )
print(spam[-1])
print(spam[-3])
print("The " + spam[-1] + ' kill the' + spam[-3])

print('\nSlicing')
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])

print('\nChanging Value')
spam[1] = 'Goldie'
print(spam[0:4])
spam[1] = spam[3]
print(spam[0:4])