import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog
import requests
import bs4
import pandas as pd
import time
import numpy as np

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('투자 종목코드', self)
        self.btn.move(30,30)
        self.btn.clicked.connect(self.showDialog)

        self.btn1 = QPushButton('투자된 금액(원)', self)
        self.btn1.move(30,60)
        self.btn1.clicked.connect(self.showDialog1)

        self.btn2 = QPushButton('보유할 기간(일)', self)
        self.btn2.move(30,90)
        self.btn2.clicked.connect(self.showDialog2)

        self.btn3 = QPushButton('목표 신뢰수준(%)', self)
        self.btn3.move(30,120)
        self.btn3.clicked.connect(self.showDialog3)

        self.btn4 = QPushButton('VaR Value', self)
        self.btn4.move(30,150)

        self.le = QLineEdit(self)
        self.le.move(160,35)

        self.le1 = QLineEdit(self)
        self.le1.move(160,65)

        self.le2 = QLineEdit(self)
        self.le2.move(160,95)

        self.le3 = QLineEdit(self)
        self.le3.move(160,125)

        self.le4 = QLineEdit(self)
        self.le4.move(160,155)

        self.setWindowTitle('Var Calculator')
        self.setGeometry(300,300,400,400)
        self.show()

    def showDialog(self):
        global StockCode, rate_mean, rate_std
        UrlHead = 'https://fchart.stock.naver.com/sise.nhn?symbol='
        UrlTail = '&timeframe=day&count=246&requestType=0'
        StockCode, ok = QInputDialog.getText(self, 'Input Dialog', '종목 코드를 입력하시오:')
        if ok:
            self.le.setText(StockCode)
        price_url = UrlHead + StockCode + UrlTail
        price_data = requests.get(price_url)
        price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml')
        item_list = price_data_bs.find_all('item')
        temp = item_list[0]['data']
        temp.split('|')
        price_list = []
        return_rate_list = []

        for item in item_list:
            temp_data = item['data']
            datas = temp_data.split('|')
            # print(datas[0],datas[4])
            price_list.append(datas[4])

        for i in range(0, 245):
            return_rate = abs(float(price_list[i + 1]) / float(price_list[i]) - 1)
            return_rate_list.append(return_rate)

        rate_mean = np.mean(return_rate_list)
        rate_std = np.std(return_rate_list)

    def showDialog1(self):
        global InvestMoney
        InvestMoney, ok = QInputDialog.getDouble(self, 'Input Dialog', '투자한 금액을 입력하시오(단위:원):')
        if ok:
            self.le1.setText(str(InvestMoney))

    def showDialog2(self):
        global HoldingDay
        HoldingDay, ok = QInputDialog.getDouble(self, 'Input Dialog', '보유할 기간을 입력하시오(단위:일):')
        if ok:
            self.le2.setText(str(HoldingDay))

    def showDialog3(self):
        global zvalue, vvalue
        zvalue, ok = QInputDialog.getDouble(self, 'Input Dialog', '목표신뢰수준을 입력하시오(%):')
        if zvalue == 99:
            zvalue = 2.33
        elif zvalue == 95:
            zvalue = 1.96
        else :
            zvalue = "오류"
        vvalue = (rate_mean-zvalue*rate_std)*(HoldingDay**(1/2))*InvestMoney
        if ok:
            self.le3.setText(str(zvalue))
            self.le4.setText(str(vvalue))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
