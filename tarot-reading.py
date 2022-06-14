tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

import random
num1 = random.randint(1, 22)
num2 = random.randint(1, 22)
num3 = random.randint(1, 22)
spread = {}

x = input("Enter your name:")
print("Hello, " + x)
print('Hello, ' + str(x) + ', here is your reading: ')

spread['past'] = tarot.pop(num1, num1)
spread['present'] = tarot.pop(num2, num2)
spread['future'] = tarot.pop(num3, num3)

for key, value in spread.items():
  print(
    'Your ' + key + ' is the ' + str(value) + ' card.'
  )


