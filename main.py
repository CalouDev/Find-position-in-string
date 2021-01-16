"""
_________     _____  .____    ________   ____ ___ 
\_   ___ \   /  _  \ |    |   \_____  \ |    |   \
/    \  \/  /  /_\  \|    |    /   |   \|    |   /
\     \____/    |    \    |___/    |    \    |  / 
 \______  /\____|__  /_______ \_______  /______/  
        \/         \/        \/       \/          
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice_user = input("Letter : ")

def find_position(alphabet, letter):
      for i in range(0, len(alphabet)): 
            if alphabet[i] == letter:
              result = i + 1
              print(result)
              break
  
find_position(letters, choice_user) # Run the function

""" 
But You can use the fonction 'find' ex: >>>a = 'character'
                                        >>>a.find('h')
                                        2
"""
