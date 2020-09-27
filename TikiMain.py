from TikiTarget import TikiTarget
from TikiHelper import getTargetFromFile 
import requests


TARGET_FILE = "target_list.txt"
targets = getTargetFromFile(TARGET_FILE)
for target in targets:
    print(target.info())


# ============================
target = targets[0]

print(target.getSearchLink(1))