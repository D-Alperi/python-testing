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
