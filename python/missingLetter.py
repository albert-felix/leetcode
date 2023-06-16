def missingLetter(words):
    prevCode = None
    result = []
    for i in range(len(words)):
        if prevCode == None:
            prevCode = ord(words[i])
            continue
        if (ord(words[i]) - prevCode) != 1:
            missingCode = ord(words[i]) - 1
            missingLetter = chr(missingCode)
            result.append(missingLetter)
            prevCode = missingCode + 1
        else:
            prevCode = ord(words[i])

    if len(result):
        return ','.join(result)
    return None

print(missingLetter('bdefghijklmnpqrstuvxyz'))