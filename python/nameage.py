import time
start_time = time.time()

print('what is your name')

myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')

myAge = input()

runtime= int(time.time()-start_time)

print('%s? Thats funny, Im only %s seconds old.' %(myAge, runtime))

print('I wish I was %s years old.' %(int(myAge)*2))

time.sleep(3)

print('Im tired. I go sleep sleep now')