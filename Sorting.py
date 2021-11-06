import os
import sys

class Electronic:
    data = []
    def __init__(self , name , price , ratings , reviews , discount , brand , country , installments):
        self.data = [name , price ,  ratings , reviews ,  discount , brand , country , installments]


class InsertionSort:
    def getSortedArray(self , Array , cloumn , asc):

        for i in range(1 , len(Array)):
            key = Array[i].data[cloumn]
            keys = Array[i]
            j = i-1
            while j>=0 and ((key<Array[j].data[cloumn]) == asc):
                Array[j+1] = Array[j]
                j = j-1
            Array[j+1] = keys
        return Array



class BubbleSort:
    def getSortedArray(self , Array , column , asc):

        for i in range(0 , len(Array)):
            for j in range(0 , len(Array)-1):
                if (Array[j].data[column] > Array[j+1].data[column]) == asc:
                    temp = Array[j+1]
                    Array[j+1] = Array[j]
                    Array[j] = temp
        return Array


class SelectionSort:
    def getSortedArray(self , Array , column , asc):

        for x in range(0 , len(Array)-1):
            index = x
            for y in range(x+1 , len(Array)):
                if (Array[y].data[column] < Array[index].data[column]) == asc:         
                    index = y
            if index != x:
                temp = Array[index]
                Array[index] = Array[x]
                Array[x] = temp
        return Array


class QuickSort:
# Code quick sort for string
    def quickSort(self , A , low , high , column , asc):
        if low < high:
            pivotI = self.partitionStr(A, low, high , column , asc)

            self.quickSort(A , low , pivotI-1 , column  , asc)
            self.quickSort(A , pivotI+1 , high , column , asc)

    def partitionStr(self , Array , low , high , column , asc):
        pivot = Array[high].data[column]
        i = low-1
        for j in range(low , high):
            if (Array[j].data[column] < pivot) == asc:
                i = i+1
                tempL = Array[i]
                Array[i] = Array[j]
                Array[j] = tempL
        temp = Array[i+1]
        Array[i+1] = Array[high]
        Array[high] = temp
        return i+1

    def getSortedArray(self , Array  , column , asce):
        length = len(Array)

        self.quickSort(Array , 0 , length-1 , column , asce)
        return Array

class MergeSort:

    def merge(self , Array , p , q , m , col , asce):
        left = []
        right = []

        for i in range(p , m+1):
            left.append(Array[i])
        for j in range(m+1 , q+1):
            right.append(Array[j])

        left.append(sys.maxsize)
        right.append(sys.maxsize)

        j=0
        i=0
        for k in range(p,q+1):
            if (left.data[col] <= right.data[col]) == asce:
                Array[k]=left[i]
                i+=1
            else:
                Array[k]=right[j]
                j+=1
        
    def merge_sort(self , A ,   l , m , col , asce):
        if l < m:
            mid = (l+m)//2
            self.merge_sort(A , l , mid , col , asce)
            self.merge_sort(A , mid+1 , m , col , asce)
            
            self.merge(A, l , m , mid , col , asce)

    def getSortedArray(self , Array , col ,asce):
        length = len(Array)
        self.merge_sort(Array , 0 , length-1 , col , asce)
        return Array



class HeapSort:
    def heap(self , A , n , index , col , asce):
        large = index
        l = 2*index+1
        r = 2*index+2
        if l < n and ((A[large].data[col] < A[l].data[col]) == asce):
            large = l

        if r < n and ((A[large].data[col] < A[r].data[col]) == asce):
            large = r
        
        if large != index:
            A[index], A[large] = A[large] , A[index]
            self.heap(A , n , large , col , asce)

    def heapSort(self , A , col , asce):
        n = len(A)
        for i in range(n//2-1 , -1 , -1):
            self.heap(A , n , i , col , asce)

        for i in range(n-1 , 0 , -1):
            A[i] , A[0] = A[0], A[i]
            self.heap(A , i , 0 , col , asce)

    def getSortedArray(self , Array , col , asce):
        self.heapSort(Array , col , asce)
        return Array

class ShellSort:
    def getSortedArray(self , Array , col ,  asce):
        space = len(Array)
        while space > 0:
            i = 0
            j = space
            while j < len(Array):
                if (Array[i].data[col] > Array[j].data[col]) == asce:
                    temp = Array[i]
                    Array[i] = Array[j]
                    Array[j] = temp
                i = i+1
                j = j+1
                k = 1
                while k -space > -1:
                    if (Array[k-space].data[col] > Array[k].data[col]) == asce:
                        temp = Array[k-space]
                        Array[k-space] = Array[k]
                        Array[k] = temp
                    k = k-1
            space = space//2
        return Array

class CountingSort:
    def findLargest(self , Aray , col):
        largest = -100000
        for i in range(0 , len(Aray)):
            if Aray[i].data[col] > largest:
                largest = Aray[i].data[col]
        return largest

    def findSmallest(self , Aray , col):
        smallest = 100000
        for i in range(0 , len(Aray)):
            if Aray[i].data[col] < smallest:
                smallest = Aray[i].data[col]
        return smallest        

    def getSortedArray(self , Array , col ,  asce):
        if type(Array[3].data[col]) == int:
            smaller = self.findSmallest(Array , col)
            if smaller < 0:
                adder = smaller*-1
                for i in range(0 , len(Array)):
                    Array[i].data[col] = Array[i].data[col]+adder
            
            count = []
            B = []
            k = self.findLargest(Array , col)
            
            for i in range(0 , len(Array)):
                B.append(0)
            
            for i in range(0 , k+1): # Array of zeros of k+1 length
                count.append(0)

            for j in range(0 , len(Array)):
                count[Array[j].data[col]] = count[Array[j].data[col]] + 1

            for j in range(1 , k+1):
                count[j] = count[j]+count[j-1]


            for i in range(len(Array)-1 , -1, -1):
                count[Array[i].data[col]] = count[Array[i].data[col]]- 1
                B[count[Array[i].data[col]]] = Array[i]


            if smaller < 0:
                for i in range(0 , len(Array)):
                    B[i].data[col] = B[i].data[col]+smaller
            if asce==True:
                return B
        else:
            count = []
            B = []
            
            for i in range(0 , 256):
                B.append(0)
            
            for i in range(0 , 256): # Array of zeros
                count.append(0)

            answer = ["" for _ in Array]

            for j in range(0 , len(Array)):
                sAttribute = Array[j].data[col]

                index = ord(sAttribute[0])
                count[index] = count[index] + 1

            for j in range(1 , 256):
                count[j] = count[j]+count[j-1]

            for i in range(0 , len(Array)):
                sAttribute = Array[i].data[col]
                index = ord(sAttribute[0])
                B[count[index]] = Array[i]
                count[index] = count[index]- 1

            for i in range(0 , len(Array)):
                answer.append(B[i])
            return answer  

        

class RadixSort:
    def getSortedArray(self , Array , column , asce):
        return Array


class BucketSort:
    def insertionSort(Array):
        for i in range(1 , len(Array)):
            key = Array[i]
            j = i-1
            while j>=0 and key<Array[j]:
                Array[j+1] = Array[j]
                j = j-1
            Array[j+1] = key
        return Array

    def getSortedArray(self , Array , prdType , asc):
        if type(prdType) == int:
            bucket = [[]  for i in range(len(Array))]
            for i in range(len(Array)):
                index = int(10*Array[i])
                bucket[index].append(Array[i])
                
            for i in range(0 , len(Array)):
                bucket[i] = self.insertionSort(bucket[i])        
            C = []   
            i = 0
            if asc == False:
                for k in reversed(bucket):
                    for j in reversed( range(0 , len(k))):
                        C.append(k[j])
                return C
            else:
                for k in bucket:
                    for j in range(0 , len(k)):
                        C.append(k[j])
                return C




def runner():
    sortingAlgorithms = []
    Aray = []
    objInsertionSort = InsertionSort()
    objBubbleSort = BubbleSort()
    objSelectionSort = SelectionSort()
    quickSort = QuickSort()
    sortingAlgorithms = [objInsertionSort , objBubbleSort , objSelectionSort , quickSort]
    useAlg = int(input("Enter Zero for insertion and one for bubble "))
   # useAl = int(input("Enter Zero for insertion "))
    case = input("Enter yes for insertion ")
    if case == "yes":
        a = True
    else:
        a = False

    objAlg = sortingAlgorithms[useAlg]

    i = objAlg.getSortedArray(Aray , "10" ,  a)
    #b = objAlg.getSortedArray(Aray , "10" ,  a)

    for j in i:
        print(str(j.intPrd)+"        "+str(j.stringPrd))

#runner()