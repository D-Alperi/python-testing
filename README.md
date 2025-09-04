spel som har dig och gissa ett hemligt nummer och meddelar om gissningen var för stort, för litet eller rätt
för testspel är nummret fast men kan ändras till vad man vill, i testspel rand.1-100 hittar programmet ett slumpmässigt nummer mellan 1-100

def guess():
  num = 5
  while True:
    gissning = int(input("Gissa ett nummer: "))
    if gissning > num:
      print("Ditt nummer var för stort")
    if gissning < num:
      print("Ditt nummer var för litet")
    elif gissning == num:
      print("Grattis, du gissade rätt")
      break

      import random
def guess():
  num = random.randint(1,100)
  while True:
    gissning = int(input("Gissa ett nummer: "))
    if gissning > num:
      print("Ditt nummer var för stort")
    elif gissning < num:
      print("Ditt nummer var för litet")
    elif gissning == num:
      print("Grattis, du gissade rätt")
      break
