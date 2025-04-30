playername = "bhupendra patil"

print("Length of player name is:", len(playername))
print("Player name in lowercase:", playername.lower())

findStringLetter = input("Enter a letter to check if the name starts with it: ")
for letter in findStringLetter:
      if findStringLetter == letter :
            reversename = playername[::-1]
            print("Reversed player name:", reversename)
      else:
            continue