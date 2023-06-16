# Defining the function with params
def missingLetter(words):
    prevCode = None
    result = []
    # Looping through the letters in the words
    for i in range(len(words)):
        # For the firstLoop saving the letterCode as it is
        if prevCode == None:
            prevCode = ord(words[i])
            continue
        # Checking for any missing letters based on unicode number and updating the prevCode
        # and appending the missing letter to the result[] 
        if (ord(words[i]) - prevCode) != 1:
            missingCode = ord(words[i]) - 1
            missingLetter = chr(missingCode)
            result.append(missingLetter)
            prevCode = missingCode + 1
        else:
            prevCode = ord(words[i])

    # If result, converting the array to string and returning
    if len(result):
        return ','.join(result)
    return None

print(missingLetter('acde'))
# Output --> b

"""
Inbuilt Functions Used
----------------------
ord()
- returns the unicode number of characters
- ord('a') --> 97
- ord('b') --> 98

chr()
- returns the character for the unicode number
- chr(97) --> 'a'
- chr(98) --> 'b'
"""