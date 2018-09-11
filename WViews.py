import sys
import PublicFunctions as pf
import WPicAdjust
import WUploadData
import os
import GlobalValues as gv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

SavePathDefualt = pf.GetDesktopPath()

class Ui_WSCWindow(object):
    def setupUi(self, WSCWindow):
        WSCWindow.setObjectName("WSCWindow")
        WSCWindow.resize(397, 343)
        WSCWindow.setMinimumSize(QtCore.QSize(397, 321))
        WSCWindow.setMaximumSize(QtCore.QSize(397, 343))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd()+"/wsc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WSCWindow.setWindowIcon(icon)
        WSCWindow.setIconSize(QtCore.QSize(36, 36))

        # 功能标题字体
        TitleFont = QtGui.QFont()
        TitleFont.setFamily("方正姚体")
        TitleFont.setPointSize(11)
        TitleFont.setBold(True)
        TitleFont.setWeight(50)
        # 按钮字体
        ButtonFont = QtGui.QFont()
        ButtonFont.setFamily("微软雅黑")
        ButtonFont.setBold(True)
        ButtonFont.setWeight(75)
        # 标签字体
        LabelFont = QtGui.QFont()
        LabelFont.setFamily("微软雅黑")
        LabelFont.setPointSize(10)
        LabelFont.setBold(False)
        LabelFont.setWeight(50)
        # 选择项字体
        RadioButton = QtGui.QFont()
        RadioButton.setFamily("微软雅黑")

        self.centralwidget = QtWidgets.QWidget(WSCWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(397, 321))
        self.centralwidget.setMaximumSize(QtCore.QSize(397, 321))
        self.centralwidget.setSizeIncrement(QtCore.QSize(397, 321))
        self.centralwidget.setObjectName("centralwidget")
        # 图片处理功能区
        # *************标题***************
        self.ImageAdjustTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageAdjustTitlelabel.setGeometry(QtCore.QRect(33, -1, 397, 20))
        self.ImageAdjustTitlelabel.setFont(TitleFont)
        self.ImageAdjustTitlelabel.setObjectName("ImageAdjustTitlelabel")
        # *************原图位置标签***************
        self.ImagePathlabel = QtWidgets.QLabel(self.centralwidget)
        self.ImagePathlabel.setGeometry(QtCore.QRect(4, 20, 61, 20))
        self.ImagePathlabel.setFont(LabelFont)
        self.ImagePathlabel.setObjectName("ImagePathlabel")
        # *************原图位置路径显示***************
        self.ImagePathlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ImagePathlineEdit.setGeometry(QtCore.QRect(62, 21, 289, 20))
        self.ImagePathlineEdit.setObjectName("ImagePathlineEdit")
        self.ImagePathlineEdit.setEnabled(False)
        # *************原图位置路径选择按钮***************
        self.ImagePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImagePathButton.setGeometry(QtCore.QRect(354, 19, 41, 23))
        self.ImagePathButton.setObjectName("ImagePathButton")
        self.ImagePathButton.clicked.connect(lambda:self.SelectFilePath('dir',self.ImagePathlineEdit))
        # *************保存位置标签***************
        self.ImageSavePathlabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageSavePathlabel.setGeometry(QtCore.QRect(4, 50, 61, 20))
        self.ImageSavePathlabel.setFont(LabelFont)
        self.ImageSavePathlabel.setObjectName("ImageSavePathlabel")
        # *************保存位置路径显示***************
        self.ImageSavePathlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ImageSavePathlineEdit.setGeometry(QtCore.QRect(62, 51, 289, 20))
        self.ImageSavePathlineEdit.setObjectName("ImageSavePathlineEdit")
        self.ImageSavePathlineEdit.setText(SavePathDefualt)
        self.ImageSavePathlineEdit.setEnabled(False)
        # *************保存位置路径选择按钮***************
        self.SavePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.SavePathButton.setGeometry(QtCore.QRect(354, 49, 41, 23))
        self.SavePathButton.setObjectName("SavePathButton")
        self.SavePathButton.clicked.connect(lambda:self.SelectFilePath('dir',self.ImageSavePathlineEdit))
        # *************宽度标签***************
        self.ImageAdjustWidthlabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageAdjustWidthlabel.setGeometry(QtCore.QRect(4,79,75,23))
        self.ImageAdjustWidthlabel.setFont(LabelFont)
        self.ImageAdjustWidthlabel.setObjectName("ImageAdjustWidthlabel")
        # *************宽度数据显示***************
        self.ImageAdjustWidthlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ImageAdjustWidthlineEdit.setGeometry(QtCore.QRect(85, 82, 50, 20))
        self.ImageAdjustWidthlineEdit.setObjectName("ImageAdjustWidthlineEdit")
        self.ImageAdjustWidthlineEdit.setEnabled(True)
        self.ImageAdjustWidthlineEdit.setText('640')
        #gv.set_value('width',int(self.ImageAdjustWidthlineEdit.text()))
        # *************开始图像处理按钮***************
        self.ImageAdjustButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImageAdjustButton.setGeometry(QtCore.QRect(145, 80, 250, 23))
        self.ImageAdjustButton.setFont(ButtonFont)
        self.ImageAdjustButton.setObjectName("ImageAdjustButton")
        self.ImageAdjustButton.clicked.connect(lambda:self.StartProcess('imageadjust'))


        # *************功能区域分割线***************
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(2, 104, 391, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")


        # 商品信息上传功能
        # *************商品信息上传标题***************
        self.DataPostTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.DataPostTitlelabel.setGeometry(QtCore.QRect(33, 114, 397, 20))
        self.DataPostTitlelabel.setFont(TitleFont)
        self.DataPostTitlelabel.setObjectName("DataPostTitlelabel")
        # *************商品信息文件标签***************
        self.ExcelPathlabel = QtWidgets.QLabel(self.centralwidget)
        self.ExcelPathlabel.setGeometry(QtCore.QRect(4, 139, 61, 20))
        self.ExcelPathlabel.setFont(LabelFont)
        self.ExcelPathlabel.setObjectName("ExcelPathlabel")
        # *************商品信息文件路径显示***************
        self.ExcelPathlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ExcelPathlineEdit.setGeometry(QtCore.QRect(64, 140, 287, 20))
        self.ExcelPathlineEdit.setObjectName("ExcelPathlineEdit")
        self.ExcelPathlineEdit.setEnabled(False)
        # *************商品信息文件选择按钮***************
        self.ExcelPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExcelPathButton.setGeometry(QtCore.QRect(354, 138, 41, 23))
        self.ExcelPathButton.setObjectName("ExcelPathButton")
        self.ExcelPathButton.clicked.connect(lambda:self.SelectFilePath('file',self.ExcelPathlineEdit))
        # *************功能选择按钮组合框***************
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(3, 165, 121, 31))
        self.groupBox_1.setTitle("")
        self.groupBox_1.setObjectName("groupBox_1")
        # *************添加功能选择***************
        self.AddradioButton = QtWidgets.QRadioButton(self.groupBox_1)
        self.AddradioButton.setGeometry(QtCore.QRect(10, 7, 51, 16))
        self.AddradioButton.setFont(RadioButton)
        self.AddradioButton.setChecked(True)
        self.AddradioButton.setObjectName("AddradioButton")
        # *************修改功能选择***************
        self.EditradioButton = QtWidgets.QRadioButton(self.groupBox_1)
        self.EditradioButton.setGeometry(QtCore.QRect(69, 7, 51, 16))
        self.EditradioButton.setFont(RadioButton)
        self.EditradioButton.setObjectName("EditradioButton")
        # *************商品信息上传按钮***************
        self.PostDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.PostDataButton.setGeometry(QtCore.QRect(124, 169, 271, 23))
        self.PostDataButton.setFont(ButtonFont)
        self.PostDataButton.setObjectName("PostDataButton")
        self.PostDataButton.clicked.connect(lambda:self.StartProcess('datapost'))

        # *************功能区域分割线***************
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 194, 391, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        # 上传图片信息功能区域
        # *************上传图片功能标题***************
        self.ImagePostTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.ImagePostTitlelabel.setGeometry(QtCore.QRect(33, 204, 397, 20))
        self.ImagePostTitlelabel.setFont(TitleFont)
        self.ImagePostTitlelabel.setObjectName("ImagePostTitlelabel")
        # *************上传图片标签***************
        self.ImagePostPathlabel = QtWidgets.QLabel(self.centralwidget)
        self.ImagePostPathlabel.setGeometry(QtCore.QRect(4, 229, 61, 20))
        self.ImagePostPathlabel.setFont(LabelFont)
        self.ImagePostPathlabel.setObjectName("ImagePostPathlabel")  
        # *************上传图片文件路径显示***************
        self.ImagePostPathlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ImagePostPathlineEdit.setGeometry(QtCore.QRect(62, 230, 289, 20))
        self.ImagePostPathlineEdit.setObjectName("ImagePostPathlineEdit")
        self.ImagePostPathlineEdit.setEnabled(False)   
        # *************上传图片位置浏览***************
        self.PostImagePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.PostImagePathButton.setGeometry(QtCore.QRect(354, 228, 41, 23))
        self.PostImagePathButton.setObjectName("PostImagePathButton")
        self.PostImagePathButton.clicked.connect(lambda:self.SelectFilePath('dir',self.ImagePostPathlineEdit))

        # *************功能选择按钮组合框***************
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(2, 255, 121, 31))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        # *************只保存选择***************
        self.SaveradioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.SaveradioButton.setGeometry(QtCore.QRect(10, 7, 51, 16))
        self.SaveradioButton.setFont(RadioButton)
        self.SaveradioButton.setChecked(True)
        self.SaveradioButton.setObjectName("SaveradioButton")
        # *************保存审核选择***************
        self.ExamineradioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.ExamineradioButton.setGeometry(QtCore.QRect(69, 7, 51, 16))
        self.ExamineradioButton.setFont(RadioButton)
        self.ExamineradioButton.setObjectName("ExamineradioButton")
        # *************上传图片开始***************
        self.PostImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.PostImageButton.setGeometry(QtCore.QRect(123, 259, 271, 23))
        self.PostImageButton.setFont(ButtonFont)
        self.PostImageButton.setObjectName("PostImageButton")        
        self.PostImageButton.clicked.connect(lambda:self.StartProcess('imagepost'))        

        # *************功能区域分割线***************
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 284, 391, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        # *************用户名标签***************
        self.UserNamelabel = QtWidgets.QLabel(self.centralwidget)
        self.UserNamelabel.setGeometry(QtCore.QRect(5, 299, 61, 20))
        self.UserNamelabel.setFont(LabelFont)
        self.UserNamelabel.setObjectName("UserNamelabel")
        # *************用户名输入***************
        self.UserNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserNamelineEdit.setGeometry(QtCore.QRect(62, 300, 131, 20))
        self.UserNamelineEdit.setObjectName("UserNamelineEdit")
        # *************密码标签***************
        self.PassWordlabel = QtWidgets.QLabel(self.centralwidget)
        self.PassWordlabel.setGeometry(QtCore.QRect(202, 299, 61, 20))
        self.PassWordlabel.setFont(LabelFont)
        self.PassWordlabel.setObjectName("PassWordlabel")
        # *************密码输入***************
        self.PassWordlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PassWordlineEdit.setGeometry(QtCore.QRect(262, 300, 131, 20))
        self.PassWordlineEdit.setObjectName("PassWordlineEdit")


        WSCWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(WSCWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('准备就绪')
        WSCWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WSCWindow)
        QtCore.QMetaObject.connectSlotsByName(WSCWindow)

    def SelectFilePath(self,method,target):
        if method =='dir':
            directory = QFileDialog.getExistingDirectory(None,'文件夹选择',pf.GetDesktopPath())
            target.setText(directory)
        else:
            file = QFileDialog.getOpenFileName(None,'文件选择',pf.GetDesktopPath())
            target.setText(file[0])

    def RefreshStatusbar(self,info):
        self.statusbar.showMessage(info)

    def ButtonEnableControl(self,object,status):
        object.setEnabled(status)

    def StartProcess(self,method):
        gv.set_value('width',640)
        if method == 'imageadjust':
            pf.Add_Thread(lambda:WPicAdjust.MultiStart(self.ImagePathlineEdit.text(),self.ImageSavePathlineEdit.text(),self),'setDaemon')
        elif method == 'datapost':
            pf.Add_Thread(lambda:WUploadData.PostDataProcessing(self.ExcelPathlineEdit.text(),self.UserNamelineEdit.text(),self.PassWordlineEdit.text(),'Add' if self.AddradioButton.isChecked() else 'Update',self),'setDaemon')
        elif method == 'imagepost':
            pf.Add_Thread(lambda:WUploadData.PostImageProcessing(self.ImagePostPathlineEdit.text(),self.UserNamelineEdit.text(),self.PassWordlineEdit.text(),'PicUpload' if self.SaveradioButton.isChecked() else 'PicUploadExamine',self),'setDaemon')

    def retranslateUi(self, WSCWindow):
        _translate = QtCore.QCoreApplication.translate
        WSCWindow.setWindowTitle(_translate("WSCWindow", "微商城工具 Version:1.0.1"))
        self.ImagePathButton.setText(_translate("WSCWindow", "✚"))
        self.SavePathButton.setText(_translate("WSCWindow", "✚"))
        self.ImageAdjustWidthlabel.setText(_translate("WSCWindow", "图片宽度(px)"))
        self.ImageAdjustTitlelabel.setText(_translate("WSCWindow", "▁▁▁▁▁▁▁▁▁自动修图▁▁▁▁▁▁▁▁▁"))
        self.ImageAdjustButton.setText(_translate("WSCWindow", "开始处理"))
        self.ImagePathlabel.setText(_translate("WSCWindow", "原图位置"))
        self.ImageSavePathlabel.setText(_translate("WSCWindow", "保存位置"))
        self.ExcelPathlabel.setText(_translate("WSCWindow", "文件位置"))
        self.ExcelPathButton.setText(_translate("WSCWindow", "✚"))
        self.DataPostTitlelabel.setText(_translate("WSCWindow", "▁▁▁▁▁▁▁▁▁信息添加▁▁▁▁▁▁▁▁▁"))
        self.PostDataButton.setText(_translate("WSCWindow", "开始上传"))
        self.PostImagePathButton.setText(_translate("WSCWindow", "✚"))
        self.ImagePostPathlabel.setText(_translate("WSCWindow", "图片位置"))
        self.PostImageButton.setText(_translate("WSCWindow", "开始上传"))
        self.ImagePostTitlelabel.setText(_translate("WSCWindow", "▁▁▁▁▁▁▁▁▁图片添加▁▁▁▁▁▁▁▁▁"))
        self.UserNamelabel.setText(_translate("WSCWindow", "用户账号"))
        self.PassWordlabel.setText(_translate("WSCWindow", "用户密码"))
        self.AddradioButton.setText(_translate("WSCWindow", "新增"))
        self.EditradioButton.setText(_translate("WSCWindow", "修改"))
        self.SaveradioButton.setText(_translate("WSCWindow", "保存"))
        self.ExamineradioButton.setText(_translate("WSCWindow", "审核"))


if __name__ == "__main__":
    gv._init()
    app = QtWidgets.QApplication(sys.argv)
    WSCWindow = QtWidgets.QMainWindow()
    ui = Ui_WSCWindow()
    ui.setupUi(WSCWindow)
    WSCWindow.show()
    sys.exit(app.exec_())

