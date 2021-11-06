from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
from Search import LinearSearch
from Sorting import Electronic
from Sorting import InsertionSort
from Sorting import BubbleSort
from Sorting import QuickSort
from Sorting import SelectionSort
from Sorting import MergeSort
from Sorting import ShellSort
from Sorting import HeapSort
from Sorting import CountingSort
from Sorting import RadixSort
from Sorting import BucketSort
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton, QProgressBar, QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from UserInterface import Ui_MainWindow
#from UserInterface import Ui_timeUse
#Global Variables

resumeOrPauseScraping = False

class Worker(QThread):
    def run(self):
        widowRunner = Ui_timeUse()
        widowRunner.runner()


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_timeUse(object):
    def setupUi(self, timeUse):
        timeUse.setObjectName("timeUse")
        timeUse.resize(997, 597)
        timeUse.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Times New Roman\";")
        self.centralwidget = QtWidgets.QWidget(timeUse)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(210, 190, 741, 381))
        self.tableWidget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(386, 40, 281, 61))
        self.label.setStyleSheet("font: 26pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.startStopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startStopBtn.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.startStopBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.startStopBtn.setObjectName("startStopBtn")
        self.pauseRexumeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pauseRexumeBtn.setGeometry(QtCore.QRect(40, 170, 75, 23))
        self.pauseRexumeBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.pauseRexumeBtn.setObjectName("pauseRexumeBtn")
        self.sortingAlgo = QtWidgets.QComboBox(self.centralwidget)
        self.sortingAlgo.setGeometry(QtCore.QRect(320, 120, 101, 22))
        self.sortingAlgo.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.sortingAlgo.setObjectName("sortingAlgo")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.sortingAlgo.addItem("")
        self.ascendingDescending = QtWidgets.QComboBox(self.centralwidget)
        self.ascendingDescending.setGeometry(QtCore.QRect(210, 120, 101, 22))
        self.ascendingDescending.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.ascendingDescending.setObjectName("ascendingDescending")
        self.ascendingDescending.addItem("")
        self.ascendingDescending.addItem("")
        self.sortNameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortNameBtn.setGeometry(QtCore.QRect(240, 160, 81, 23))
        self.sortNameBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.sortNameBtn.setObjectName("sortNameBtn")
        self.getDataToSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.getDataToSearch.setGeometry(QtCore.QRect(40, 260, 151, 31))
        self.getDataToSearch.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"border-color: rgb(0, 0, 0);")
        self.getDataToSearch.setObjectName("getDataToSearch")
        self.searchCombo = QtWidgets.QComboBox(self.centralwidget)
        self.searchCombo.setGeometry(QtCore.QRect(40, 310, 101, 21))
        self.searchCombo.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.searchCombo.setObjectName("searchCombo")
        self.searchCombo.addItem("")
        self.searchCombo.addItem("")
        self.searchCombo.addItem("")
        self.searchCombo.addItem("")
        self.searchCombo.addItem("")
        self.searchDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchDataBtn.setGeometry(QtCore.QRect(40, 350, 75, 23))
        self.searchDataBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.searchDataBtn.setObjectName("searchDataBtn")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 530, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 500, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 500, 47, 13))
        self.label_3.setObjectName("label_3")
        self.sortPriceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortPriceBtn.setGeometry(QtCore.QRect(340, 160, 81, 23))
        self.sortPriceBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.sortPriceBtn.setObjectName("sortPriceBtn")
        self.sortBrandBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortBrandBtn.setGeometry(QtCore.QRect(440, 160, 81, 23))
        self.sortBrandBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.sortBrandBtn.setObjectName("sortBrandBtn")
        self.sortRatingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortRatingBtn.setGeometry(QtCore.QRect(550, 160, 81, 23))
        self.sortRatingBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.sortRatingBtn.setObjectName("sortRatingBtn")
        self.sortDiscountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sortDiscountBtn.setGeometry(QtCore.QRect(710, 160, 101, 23))
        self.sortDiscountBtn.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.sortDiscountBtn.setObjectName("sortDiscountBtn")
        timeUse.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(timeUse)
        self.statusbar.setObjectName("statusbar")
        timeUse.setStatusBar(self.statusbar)

        self.retranslateUi(timeUse)

        self.startStopBtn.clicked.connect(self.startScraping)
        self.pauseRexumeBtn.clicked.connect(self.pauseOrResumecraping)
        self.sortNameBtn.clicked.connect(self.applySortingOnName)
        self.sortPriceBtn.clicked.connect(self.applySortingOnPrice)
        self.sortBrandBtn.clicked.connect(self.applySortingOnBrand)
        self.sortRatingBtn.clicked.connect(self.applySortingOnRating)
        self.sortDiscountBtn.clicked.connect(self.applySortingOnDiscount)
        self.searchDataBtn.clicked.connect(self.applySearch)


        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################


        QtCore.QMetaObject.connectSlotsByName(timeUse)


    array_all_data_list = [] # This is the array that will contain all data of products
    #This function is for purpose when start button clicks scraping starts
    name_list = []
    price_list = []
    rating_list = []
    review_list = []
    discount_list = []
    brand_list = []
    country_list = []
    installment_list = []

    def loadDataIntoArrayFromFile(self):
        df  = pd.read_csv('PrdEln.csv')

        self.name_list = (df["Name"].tolist())
        self.price_list = (df["Price"].tolist())
        self.rating_list = (df["Ratings"].tolist())
        self.review_list = (df["Reviews"].tolist())
        self.discount_list = (df["Discount"].tolist())
        self.brand_list = (df["Brand"].tolist())
        self.country_list = (df["Country"].tolist())
        self.installment_list = (df["Installments"].tolist())

        for i in range(0 , len(self.name_list)):

            obj = Electronic(self.name_list[i] , self.price_list[i] , self.rating_list[i] , self.review_list[i] , self.discount_list[i] , self.brand_list[i] , self.country_list[i] , self.installment_list[i])
            self.array_all_data_list.append(obj)

    def startScraping(self):
        self.startStopBtn.setText(self._translate("MainWindow", "Stop"))
        self.loadDataIntoArrayFromFile()
        self.loadDataIntoGrid(self.array_all_data_list)
        self.startStopBtn.clicked.connect(self.stopScraping)
        self.worker = Worker()
        self.worker.start()

    #This function is for purpose when stop button clicks scraping will stop
    def stopScraping(self):
        self.worker = Worker()
        self.worker.stop()

    def pauseOrResumecraping(self):
        textInbutton = self.pauseRexumeBtn.text()
        if textInbutton == "Pause":
            self.pauseScraping()
        elif textInbutton == "Resume":
            self.resumeScraping()

    def pauseScraping(self):
        global resumeOrPauseScraping
        resumeOrPauseScraping = True
        self.pauseRexumeBtn.setText(self._translate("MainWindow", "Resume"))

    def resumeScraping(self):
        global resumeOrPauseScraping
        resumeOrPauseScraping = False
        self.pauseRexumeBtn.setText(self._translate("MainWindow", "Pause"))


##THis function will load data into grid
    def loadDataIntoGrid(self , array): # This will load data in grid
        row = 0
        self.tableWidget.setRowCount(len(array))
        for i in array:
            data_of_prd = [{"Name": i.data[0] , "Price": i.data[1] ,"Ratings": i.data[2] , "Reviews": i.data[3]  , "Discounts": i.data[4] , "Brand": i.data[5] , "Country": i.data[6] ,  "Installments":i.data[7]  }]
            for products in data_of_prd:
                self.tableWidget.setItem(row , 0 , QtWidgets.QTableWidgetItem(products["Name"]))
                self.tableWidget.setItem(row , 1 , QtWidgets.QTableWidgetItem(products["Price"]))
                self.tableWidget.setItem(row , 2, QtWidgets.QTableWidgetItem(products["Brand"]))
                self.tableWidget.setItem(row , 3 , QtWidgets.QTableWidgetItem(products["Ratings"]))
                self.tableWidget.setItem(row , 4 , QtWidgets.QTableWidgetItem(products["Installments"]))
                self.tableWidget.setItem(row , 5 , QtWidgets.QTableWidgetItem(products["Discounts"]))
                self.tableWidget.setItem(row , 6 , QtWidgets.QTableWidgetItem(products["Country"]))
                row = row+1

###########################
############################
#           Here Works for sorting start

    objInsertionSort = InsertionSort()
    objBubbleSort = BubbleSort()
    objSelectionSort = SelectionSort()
    quickSort = QuickSort()
    mergeSort = MergeSort()
    shellSort = ShellSort()
    heapSort = HeapSort()
    countingSort = CountingSort()
    radixSort = RadixSort()
    bucketSort = BucketSort()
    sortingAlgorithms = [objInsertionSort , objSelectionSort  , objBubbleSort , mergeSort ,  quickSort , 
                          heapSort , shellSort , countingSort , radixSort , bucketSort]

    objLinearSearch = LinearSearch()
        #Functions for sorting the data
        #######################
        ######################
        #########################

    def applySortingOnName(self):
        ascending = True
        ind = self.sortingAlgo.currentIndex()
        asdIndex = self.ascendingDescending.currentIndex()
        if asdIndex == 0:
            ascending = True
        else:
            ascending = False
        use_alg = self.sortingAlgorithms[ind]
        obj = use_alg.getSortedArray(self.array_all_data_list  , 0 , ascending)
        self.loadDataIntoGrid(obj)

    def applySortingOnPrice(self):
        ascending = True
        ind = self.sortingAlgo.currentIndex()
        asdIndex = self.ascendingDescending.currentIndex()
        if asdIndex == 0:
            ascending = True
        else:
            ascending = False
        use_alg = self.sortingAlgorithms[ind]
        obj = use_alg.getSortedArray(self.array_all_data_list  , 1 , ascending)
        self.loadDataIntoGrid(obj)

    def applySortingOnRating(self):
        ascending = True
        ind = self.sortingAlgo.currentIndex()
        asdIndex = self.ascendingDescending.currentIndex()
        if asdIndex == 0:
            ascending = True
        else:
            ascending = False
        use_alg = self.sortingAlgorithms[ind]
        obj = use_alg.getSortedArray(self.array_all_data_list  , 2 , ascending)
        self.loadDataIntoGrid(obj)

    def applySortingOnDiscount(self):
        ascending = True
        ind = self.sortingAlgo.currentIndex()
        asdIndex = self.ascendingDescending.currentIndex()
        if asdIndex == 0:
            ascending = True
        else:
            ascending = False
        use_alg = self.sortingAlgorithms[ind]
        obj = use_alg.getSortedArray(self.array_all_data_list  , 4 , ascending)
        self.loadDataIntoGrid(obj)

    def applySortingOnBrand(self):
        ascending = True
        ind = self.sortingAlgo.currentIndex()
        asdIndex = self.ascendingDescending.currentIndex()
        if asdIndex == 0:
            ascending = True
        else:
            ascending = False
        use_alg = self.sortingAlgorithms[ind]
        obj = use_alg.getSortedArray(self.array_all_data_list  , 5 , ascending)
        self.loadDataIntoGrid(obj)



#############################
##################################
#######################################

#Function for applying search
    def applySearch(self):
        whichAttributeSearch = 0
        search = self.getDataToSearch.text()
        searchColumnIndex = self.searchCombo.currentIndex()

        if searchColumnIndex == 0:
            whichAttributeSearch = 0

        elif searchColumnIndex == 1:
            whichAttributeSearch = 1

        elif searchColumnIndex == 2:
            whichAttributeSearch = 4

        elif searchColumnIndex == 3:
            whichAttributeSearch = 6

        elif searchColumnIndex == 4:
            whichAttributeSearch = 5

        searchFind = self.objLinearSearch.search(search , self.array_all_data_list , whichAttributeSearch)
        self.loadDataIntoGrid(searchFind)

    def retranslateUi(self, timeUse):
        self._translate = QtCore.QCoreApplication.translate
        timeUse.setWindowTitle(self._translate("timeUse", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(self._translate("timeUse", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(self._translate("timeUse", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(self._translate("timeUse", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(self._translate("timeUse", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(self._translate("timeUse", "Installments"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(self._translate("timeUse", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(self._translate("timeUse", "Country"))
        self.label.setText(self._translate("timeUse", "Electronic Products"))
        self.startStopBtn.setText(self._translate("timeUse", "Start"))
        self.pauseRexumeBtn.setText(self._translate("timeUse", "Pause"))
        self.sortingAlgo.setItemText(0, self._translate("timeUse", "Insertion Sort"))
        self.sortingAlgo.setItemText(1, self._translate("timeUse", "Selection Sort"))
        self.sortingAlgo.setItemText(2, self._translate("timeUse", "Bubble Sort"))
        self.sortingAlgo.setItemText(3, self._translate("timeUse", "Merge Sort"))
        self.sortingAlgo.setItemText(4, self._translate("timeUse", "Quick Sort"))
        self.sortingAlgo.setItemText(5, self._translate("timeUse", "Heap Sort"))
        self.sortingAlgo.setItemText(6, self._translate("timeUse", "Shell Sort"))
        self.sortingAlgo.setItemText(7, self._translate("timeUse", "Counting Sort"))
        self.sortingAlgo.setItemText(8, self._translate("timeUse", "Radix Sort"))
        self.sortingAlgo.setItemText(9, self._translate("timeUse", "Bucket Sort"))
        self.ascendingDescending.setItemText(0, self._translate("timeUse", "Ascending"))
        self.ascendingDescending.setItemText(1, self._translate("timeUse", "Descending"))
        self.sortNameBtn.setText(self._translate("timeUse", "Sort Name"))
        self.searchCombo.setItemText(0, self._translate("timeUse", "Name"))
        self.searchCombo.setItemText(1, self._translate("timeUse", "Price"))
        self.searchCombo.setItemText(2, self._translate("timeUse", "Discounts"))
        self.searchCombo.setItemText(3, self._translate("timeUse", "Country"))
        self.searchCombo.setItemText(4, self._translate("timeUse", "Brand"))
        self.searchDataBtn.setText(self._translate("timeUse", "Search"))
        self.label_2.setText(self._translate("timeUse", "Time Elapsed:"))
        self.label_3.setText(self._translate("timeUse", "3s"))
        self.sortPriceBtn.setText(self._translate("timeUse", "Sort Price"))
        self.sortBrandBtn.setText(self._translate("timeUse", "Sort Brand"))
        self.sortRatingBtn.setText(self._translate("timeUse", "Sort Rating"))
        self.sortDiscountBtn.setText(self._translate("timeUse", "Sort Discount"))


# Here is code for scraping
###########################
###########################
########################
    driver = webdriver.Chrome(executable_path='D:\Semester 3\DSA LAB\week 2\Chrome Driver\chromedriver.exe')

    def load_data_InFile(self , array_list ):
        for i in array_list:
            data=[i.data[0],i.data[1], i.data[2] , i.data[3]  , i.data[4] , i.data[5] , i.data[6] , i.data[7]]
            with open("PrdEln.csv", "a", newline='',encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow(data)
        #self.loadDataIntoGrid() 


    def smartPhonescrap(self):
        array_list = []
        
        smartPhonepages = list(range(1 , 79))
        for smP in smartPhonepages:
            self.driver.get("https://www.daraz.pk/smartphones/?page={}&spm=a2a0e.searchlistcategory.cate_1.1.2ff05e4eQPmEY5".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = ""
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i > 12:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                        i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text

                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                
        header = ['Name', 'Price'  , 'Ratings' , 'Reviews' , 'Discount' , 'Brand' , 'Country' , 'Installments']
        with open("PrdEln.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)

        for i in self.array_list:
            data=[i.Name,i.Price, i.Ratings , i.Reviews  , i.Discount , i.Brand , i.Country , i.Installments]
            with open("PrdEln.csv", "a", newline='',encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow(data)


    def featurePhonescrap(self):
        
        array_list = [] 
        count = 0
        
        featurePhonepages = list(range(1 , 2))
        global resumeOrPauseScraping
        for smP in featurePhonepages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/featurephones/?page={}&spm=a2a0e.searchlistcategory.cate_1.2.5396c414KTrLcx".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                
                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                    
                    
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)
        #self.loadDataIntoGrid()
        self.load_data_InFile(array_list)


    def landLinePhonescrap(self):
        count = 0
        array_list = []     
        landLinePhonepages = list(range(1 , 54))
        global resumeOrPauseScraping
        for smP in landLinePhonepages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/corded-phones/?page={}&spm=a2a0e.searchlistcategory.cate_1.4.b3af7242YlNkvy".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                    
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text

                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
       

    def laptopscrap(self):
        count = 0
        array_list = [] 
        laptoppages = list(range(1 , 23))
        global resumeOrPauseScraping
        for smP in laptoppages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/laptops/?page={}&spm=a2a0e.searchlistcategory.cate_1.5".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                    
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments )
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def desktopscrap(self):  
        count = 0
        array_list = [] 
        desktoppages = list(range(1 , 9))
        global resumeOrPauseScraping
        for smP in desktoppages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/desktop-computer/?page={}&spm=a2a0e.searchlistca".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                
                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                    
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text

                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def smartWatchscrap(self):
        count = 0
        array_list = []    
        smartWatchpages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in smartWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/smart-watches/?page={}&spm=a2a0e.searchlistcategory.cate_1.7.b4914c06WQnbnH".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                
                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)

                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)

                
    def gamingConsolescrap(self):
        count = 0
        array_list = [] 
        gamingConsolepages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in gamingConsolepages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/gaming-consoles/?page={}&spm=a2a0e.searchlistcategory.cate_1.8.6aee6399VZLtuW".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text

                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def cameracrap(self):  
        count = 0
        array_list = []   
        camerapages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in camerapages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/camera/?page={}&spm=a2a0e.searchlistcategory.cate_1.9.21065d00etwuh1".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)

       
    def mobileAssessrycrap(self):
        count = 0
        array_list = []    
        mobileAssessrypages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in mobileAssessrypages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/mobiles-tablets-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_2.1.1f035df8TLn9Gd".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)

           
    def phoneCamerascrap(self):  
        count = 0
        array_list = []   
        phoneCamerapages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in phoneCamerapages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/phone-camera-flash-lights/?page={}&spm=a2a0e.searchlistcategory.cate_2_1.10.439c365dpxnsSX".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def mobileCoverscrap(self):    
        count = 0
        array_list = [] 
        mobileCOverspages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in mobileCOverspages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/mobile-cases-covers/?page={}&spm=a2a0e.searchlistcategory.cate_2_1.1.137d5a2f9lThVf".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)

                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def carChargerscrap(self):  
        count = 0
        array_list = []   
        carChargerpages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in carChargerpages :
            while resumeOrPauseScraping == True:
                count = count+1
            array_list=[]
            self.driver.get("https://www.daraz.pk/car-chargers/?page={}&spm=a2a0e.searchlistcategory.cate_2_1.8.31c615c6wDiQxh".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def otherComputerAssessryscrap(self):    
        count = 0
        array_list = []
        otherComputerAssessrypages = list(range(1 , 82))
        global resumeOrPauseScraping
        for smP in otherComputerAssessrypages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/other-computer-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_2_5.1.372915c6ByRzzG".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                
                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
         

    def pcAudioscrap(self):  
        count = 0
        array_list = []   
        pcAudiopages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in pcAudiopages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/pc-audio/?page={}&spm=a2a0e.searchlistcategory.cate_2_5.5.680f79e8TK6eLN".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def ledTvscrap(self):
        count = 0
        array_list = [] 
        ledTvpages = list(range(1 , 9))
        global resumeOrPauseScraping
        for smP in ledTvpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/led-tvs/?page={}&spm=a2a0e.searchlistcategory.cate_3.1.f4bc5e2a3PnmUo".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
        
    
    def tvAssessryscrap(self):    
        count = 0
        array_list = [] 
        tvAssessrypages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in tvAssessrypages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/tv-accessories/?page={}&spm=a2a0e.searchlistcategory.cate_3.4.dff23805VNJrCV".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
        

    def ironAppliancescrap(self):
        count = 0
        array_list = [] 
        ironpages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in ironpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/ironing-laundry-appliances/?page={}&spm=a2a0e.searchlistcategory.cate_3_9.1.1f977a40OBxZ2U".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
        

    def vacumCleanerscrap(self):
        count = 0
        array_list = [] 
        vacumCleanerpages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in vacumCleanerpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/vacuum-cleaners/?page={}&spm=a2a0e.searchlistcategory.cate_3_10.1.4534682dZOx2JZ".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 8:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)

        
    def washerDryerscrap(self):
        count = 0
        array_list = [] 
        washerDryerpages = list(range(1 , 50))
        global resumeOrPauseScraping
        for smP in washerDryerpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/washers-dryers/?page={}&spm=a2a0e.searchlistcategory.cate_3_12.3.155773f24EVwsd".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")
                

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)

          
    def mensWatchscrap(self):
        count = 0
        array_list = [] 
        mensWatchpages = list(range(1 , 67))
        global resumeOrPauseScraping
        for smP in mensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/mens-chronograph/?page={}&service=OS&spm=a2a0e.searchlistcategory.cate_10_1.2.78fa21c2Sgb2Ap".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = ""
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text
                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)
            

    def womensWatchscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 50))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/womens-fashion-watches-wsj/?page={}&service=OS&spm=a2a0e.searchlistcategory.cate_10_2.2.717221c204DeL3".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def securityCamerascrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 103))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/security-cameras/?page={}&spm=a2a0e.searchlistcategory.cate_1.10.691c6399HevvKV".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def freezerscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 6))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/freezers/?page={}&spm=a2a0e.searchlistcategory.cate_3_6.4.64e23382hZ4v9e".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def refregratorscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 39))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/refrigerators/?page={}&spm=a2a0e.searchlistcategory.cate_3_6.1.12547cd9inuYyG".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def ovenscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 9))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/large-ovens/?page={}&spm=a2a0e.searchlistcategory.cate_3_6.3.3f2d3224Ztmg5g".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def airConditionerscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 25))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/air-conditioners/?page={}&spm=a2a0e.searchlistcategory.cate_3_8.2.49972140uBNYSD".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def aircoolerscrap(self):
        count = 0
        array_list = [] 
        womensWatchpages = list(range(1 , 86))
        global resumeOrPauseScraping
        for smP in womensWatchpages:
            while resumeOrPauseScraping == True:
                count = count+1
            self.driver.get("https://www.daraz.pk/portable-ac/?page={}&spm=a2a0e.searchlistcategory.cate_3_8.3.4fad1547Yvwc08".format(smP))
            content = self.driver.page_source
            soup = BeautifulSoup(content)
            for a in soup.findAll('div',attrs={'class':'c5TXIP'}):
                brand = " "
                spaceFound = 0
                i = 0
                name=a.find('div' ,attrs={'class':'c16H9d'})
                while spaceFound == 0:
                    if name.text[i] == " " or i >= 10:
                        spaceFound = spaceFound+1
                    else:
                        brand = brand+name.text[i]
                    i = i+1
                price0 = a.find('span' ,attrs={'class':'c13VH6'})
                price = price0.text.replace("Rs. ","")

                reviews = a.find('span' ,attrs={'class':'c3XbGJ'})
                if reviews==None:
                    reviews="0"
                else:
                    reviews = reviews.text.replace("-","")

                discount = a.find('span' ,attrs={'class':'c1hkC1'})
                if discount==None:
                    discount="  0%"
                else:
                    discount= discount.text
                country = a.find('span' ,attrs={'class':'c2i43- '})
                if country == None:
                    country = "Pakistan"
                else: 
                    country = country.text

                ratings = a.find('ul' ,attrs={'class':'ant-rate ant-rate-disabled'})
                if ratings==None:
                    ratings="0"
                else:
                    ratings = ratings.text
                    
                installments = a.find('div' ,attrs={'class':'c3ubLI'})
                if installments == None:
                    installments = "No available"
                else: 
                    installments = installments.text
                obj = Electronic(name.text , price , ratings , reviews , discount , brand , country , installments)
                self.array_list.append(obj)
                self.array_all_data_list.append(obj)

        self.load_data_InFile(array_list)


    def runner(self):
        self.featurePhonescrap()  
        self.landLinePhonescrap()
        self.laptopscrap()            
        self.desktopscrap()     
        self.smartWatchscrap()        
        self.gamingConsolescrap()        
        self.cameracrap()
        self.mobileAssessrycrap()        
        self.phoneCamerascrap()
        self.mobileCoverscrap()       
        self.carChargerscrap()
        self.otherComputerAssessryscrap()         
        self.pcAudioscrap()
        self.ledTvscrap()         
        self.tvAssessryscrap()         
        self.ironAppliancescrap()
        self.vacumCleanerscrap()
        self.washerDryerscrap() 
        self.mensWatchscrap()      
        self.womensWatchscrap()               
        self.securityCamerascrap()
        self.freezerscrap()
        self.refregratorscrap()
        self.ovenscrap()
        self.airConditionerscrap()
        self.aircoolerscrap()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timeUse = QtWidgets.QMainWindow()
    ui = Ui_timeUse()
    ui.setupUi(timeUse)
    timeUse.show()
    sys.exit(app.exec_())
