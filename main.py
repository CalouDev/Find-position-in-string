letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice_user = input("Letter : ")

def findPosition(alphabet, letter):
      for i in range(0, len(alphabet)):
            if alphabet[i] == letter:
              result = i + 1
              print(result)
              break
  
findPosition(letters, choice_user)

""" 
But You can use the fonction 'find' ex: >>>a = 'character'
                                        >>>a.find('h')
                                        2
"""
