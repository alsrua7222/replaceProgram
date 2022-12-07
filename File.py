from random import randint
def getReplaceDict(path: str) -> dict:
    replaceDict = {}
    with open(path, "r", encoding="utf-8") as f:
        for query in f.readlines():
            key, values = query.split("|")
            replaceDict[key] = values.split(',')
    return replaceDict

def setReplaceConvertToStr(replaceDictionary: dict, OriginString: str) -> str:
    for key, values in replaceDictionary.items():
        length = len(values)
        OriginString = OriginString.replace(key, values[randint(0, length - 1)].rstrip())
    return OriginString
