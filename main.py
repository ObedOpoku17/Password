correctPassword = "pa55word"
guesses = 0
guess = ""

while guess != correctPassword:
  guess = input("Try to guess the password")
  guesses = guesses + 1

  print("Password guessed correctly")
  
  if guesses == 1:
    print("That took you 1 guess.")
  else:
      print("That took you " + str(guesses) + " goes.")