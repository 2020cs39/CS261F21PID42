

class LinearSearch:
    def search(self , toSearch, Array , column):
        searchFindInArray = 0
        for i in range(0 , len(Array)):
            if Array[i].data[column] == toSearch:
                temp = Array[searchFindInArray]
                Array[searchFindInArray] = Array[i]
                Array[i] = temp
                searchFindInArray = searchFindInArray+1
        return Array
