class TikiTarget:
    def __init__(self, parternStr = "", categoryStr = ""):
        self.parternStr = parternStr
        self.parterns = self.__splitPartern()
        self.categoryUrl = categoryStr

    def info(self):
        return "Partterns : "  +  str(self.parterns) +  \
        "| Category: " + self.categoryUrl

    def __splitPartern(self):
        newList = self.parternStr.split(",")
        newList = [item.strip() for item in newList]
        return newList

    def getKeyword(self):
        keyword = " ".join(self.parterns)
        return keyword

    def getSearchLink(self, pageNumber):
        searchLink = self.categoryUrl + "?q=" + self.getKeyword() + "&ref=categorySearch&page" + str(pageNumber)
        return searchLink