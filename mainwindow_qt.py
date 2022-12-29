from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet(u"background-color: #FFFFFF;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_img = QLabel(self.centralwidget)
        self.input_img.setObjectName(u"input_img")
        self.input_img.setGeometry(QRect(0, 0, 500, 500))
        self.output_img = QLabel(self.centralwidget)
        self.output_img.setObjectName(u"output_img")
        self.output_img.setGeometry(QRect(500, 0, 500, 500))
        self.select_image = QPushButton(self.centralwidget)
        self.select_image.setObjectName(u"select_image")
        self.select_image.setGeometry(QRect(175, 540, 150, 50))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        self.select_image.setFont(font)
        self.select_image.setStyleSheet(u"border-width: 2px;\n"
"border-radius: 16px;\n"
"background-color: #4285f4;\n"
"color: #FFFFFF;")
        self.save_image = QPushButton(self.centralwidget)
        self.save_image.setObjectName(u"save_image")
        self.save_image.setGeometry(QRect(675, 540, 150, 50))
        self.save_image.setFont(font)
        self.save_image.setStyleSheet(u"border-width: 2px;\n"
"border-radius: 16px;\n"
"background-color: #4285f4;\n"
"color: #FFFFFF;")
        self.super_resolve = QPushButton(self.centralwidget)
        self.super_resolve.setObjectName(u"super_resolve")
        self.super_resolve.setGeometry(QRect(420, 520, 200, 100))
        self.super_resolve.setFont(font)
        self.super_resolve.setStyleSheet(u"border-width: 2px;\n"
"border-radius: 16px;\n"
"background-color: #FF0000;\n"
"color: #FFFFFF;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_img.setText("")
        self.output_img.setText("")
        self.select_image.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.save_image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.super_resolve.setText(QCoreApplication.translate("MainWindow", u"Super-Resolve!", None))
    # retranslateUi

