# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)


# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0                  
shiftedPosition = 0
shiftedMessage = ""

# Run code

# Introduction
print("Welcome! This program will encrypt/decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters)
print("For messages with multiple words, you may separate the words with spaces.")
useProgram = input("\nAre you ready to begin? Enter 'yes' to get started or 'no' to quit: ")

# Receive user input
while useProgram.lower() == "yes":
  initialPosition = 0                  # Resets variables each time program repeats
  shiftedPosition = 0
  shiftedMessage = ""
  initialMessage = input("What is your message? Type in all caps: ").upper()
  key = int(input("What is your key? Enter a number from 0-25: "))
  mode = input("Would you like to (a) encrypt or (b) decrypt? Enter (a) or (b): ")
  
  # Encrypt or decrypt the message
  for character in initialMessage: 
    if character in possibleCharacters:
      initialPosition = possibleCharacters.find(character)      
      
      if mode.lower() == "a":     
        shiftedPosition = initialPosition + key
      elif mode.lower() == "b":
        shiftedPosition = initialPosition - key
    
      if shiftedPosition >= len(possibleCharacters):
        shiftedPosition = shiftedPosition - len(possibleCharacters)
      elif shiftedPosition < 0:
        shiftedPosition = shiftedPosition + len(possibleCharacters)
        
      shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
    else:
      shiftedMessage = shiftedMessage + character
  
  # Print the shifted message
  if mode.lower() == "a":
      print("Your encrypted message is " + shiftedMessage)
  elif mode.lower() == "b":
      print("Your decrypted message is " + shiftedMessage)

  # Repeat program
  useProgram = input("\nWould you like to encrypt/decrypt another message? Enter 'yes' to continue or 'no' to quit: ")

  
# End program
while useProgram.lower() == "no":
  print("\nThanks for using this program. Have a nice day :)")
  break
  
