from TikiTarget import TikiTarget


def getTargetFromFile(filename):
    targetFile = open(filename, "r")
    lines = targetFile.readlines()
    targetFile.close()

    TikiTargets = []

    numberOfLines = len(lines)
    i = 0
    while i < numberOfLines:
        newLinePartern = lines[i].strip()
        newLineUrl = lines[i+1].strip()
        newTarget = TikiTarget(newLinePartern, newLineUrl)
        TikiTargets.append(newTarget)
        i = i + 2
   

    return TikiTargets