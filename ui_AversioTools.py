# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AversioToolsLTwtXw.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_AversioTools(object):
    def setupUi(self, AversioTools):
        if not AversioTools.objectName():
            AversioTools.setObjectName(u"AversioTools")
        AversioTools.resize(662, 581)
        icon = QIcon()
        icon.addFile(u"Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AversioTools.setWindowIcon(icon)
        self.centralwidget = QWidget(AversioTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 120, 631, 381))
        self.IDS = QWidget()
        self.IDS.setObjectName(u"IDS")
        self.gridLayoutWidget = QWidget(self.IDS)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 100, 611, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.IDS_Path = QPushButton(self.gridLayoutWidget)
        self.IDS_Path.setObjectName(u"IDS_Path")

        self.gridLayout_2.addWidget(self.IDS_Path, 0, 1, 1, 1)

        self.IDSFile = QLabel(self.gridLayoutWidget)
        self.IDSFile.setObjectName(u"IDSFile")

        self.gridLayout_2.addWidget(self.IDSFile, 0, 0, 1, 1)

        self.ReportTemplate = QLabel(self.gridLayoutWidget)
        self.ReportTemplate.setObjectName(u"ReportTemplate")

        self.gridLayout_2.addWidget(self.ReportTemplate, 1, 0, 1, 1)

        self.ReportTemplate_Path = QPushButton(self.gridLayoutWidget)
        self.ReportTemplate_Path.setObjectName(u"ReportTemplate_Path")

        self.gridLayout_2.addWidget(self.ReportTemplate_Path, 1, 1, 1, 1)

        self.Report = QLabel(self.gridLayoutWidget)
        self.Report.setObjectName(u"Report")

        self.gridLayout_2.addWidget(self.Report, 2, 0, 1, 1)

        self.Report_path = QPushButton(self.gridLayoutWidget)
        self.Report_path.setObjectName(u"Report_path")

        self.gridLayout_2.addWidget(self.Report_path, 2, 1, 1, 1)

        self.IDSDescription = QLabel(self.IDS)
        self.IDSDescription.setObjectName(u"IDSDescription")
        self.IDSDescription.setGeometry(QRect(0, 10, 611, 51))
        self.IDSDescription.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.IDSDescription.setWordWrap(True)
        self.IDSCheck = QPushButton(self.IDS)
        self.IDSCheck.setObjectName(u"IDSCheck")
        self.IDSCheck.setGeometry(QRect(20, 280, 225, 60))
        self.ShowIDSReport = QPushButton(self.IDS)
        self.ShowIDSReport.setObjectName(u"ShowIDSReport")
        self.ShowIDSReport.setGeometry(QRect(340, 280, 225, 60))
        self.tabWidget.addTab(self.IDS, "")
        self.ON = QWidget()
        self.ON.setObjectName(u"ON")
        self.ONDescription = QLabel(self.ON)
        self.ONDescription.setObjectName(u"ONDescription")
        self.ONDescription.setGeometry(QRect(0, 10, 611, 51))
        self.ONDescription.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.ONDescription.setWordWrap(True)
        self.gridLayoutWidget_3 = QWidget(self.ON)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 70, 581, 191))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CSVFile = QLabel(self.gridLayoutWidget_3)
        self.CSVFile.setObjectName(u"CSVFile")

        self.gridLayout_3.addWidget(self.CSVFile, 0, 0, 1, 1)

        self.CSVPath = QPushButton(self.gridLayoutWidget_3)
        self.CSVPath.setObjectName(u"CSVPath")

        self.gridLayout_3.addWidget(self.CSVPath, 0, 1, 1, 1)

        self.ONTemplatePath = QPushButton(self.gridLayoutWidget_3)
        self.ONTemplatePath.setObjectName(u"ONTemplatePath")

        self.gridLayout_3.addWidget(self.ONTemplatePath, 2, 1, 1, 1)

        self.ONTemplate = QLabel(self.gridLayoutWidget_3)
        self.ONTemplate.setObjectName(u"ONTemplate")

        self.gridLayout_3.addWidget(self.ONTemplate, 2, 0, 1, 1)

        self.ONReport = QLabel(self.gridLayoutWidget_3)
        self.ONReport.setObjectName(u"ONReport")

        self.gridLayout_3.addWidget(self.ONReport, 3, 0, 1, 1)

        self.ONReportPath = QPushButton(self.gridLayoutWidget_3)
        self.ONReportPath.setObjectName(u"ONReportPath")

        self.gridLayout_3.addWidget(self.ONReportPath, 3, 1, 1, 1)

        self.ONParamsPath = QPushButton(self.gridLayoutWidget_3)
        self.ONParamsPath.setObjectName(u"ONParamsPath")

        self.gridLayout_3.addWidget(self.ONParamsPath, 1, 1, 1, 1)

        self.ONParams = QLabel(self.gridLayoutWidget_3)
        self.ONParams.setObjectName(u"ONParams")

        self.gridLayout_3.addWidget(self.ONParams, 1, 0, 1, 1)

        self.ONCheck = QPushButton(self.ON)
        self.ONCheck.setObjectName(u"ONCheck")
        self.ONCheck.setGeometry(QRect(20, 280, 225, 60))
        self.ShowONReport = QPushButton(self.ON)
        self.ShowONReport.setObjectName(u"ShowONReport")
        self.ShowONReport.setGeometry(QRect(340, 280, 225, 60))
        self.tabWidget.addTab(self.ON, "")
        self.Log = QWidget()
        self.Log.setObjectName(u"Log")
        self.AversioToolLog = QListView(self.Log)
        self.AversioToolLog.setObjectName(u"AversioToolLog")
        self.AversioToolLog.setGeometry(QRect(0, 30, 600, 241))
        self.LogDescription = QLabel(self.Log)
        self.LogDescription.setObjectName(u"LogDescription")
        self.LogDescription.setGeometry(QRect(0, 0, 611, 51))
        self.LogDescription.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.LogDescription.setWordWrap(True)
        self.SaveLog = QPushButton(self.Log)
        self.SaveLog.setObjectName(u"SaveLog")
        self.SaveLog.setGeometry(QRect(375, 280, 225, 60))
        self.tabWidget.addTab(self.Log, "")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 481, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.IFCFile = QLabel(self.gridLayoutWidget_2)
        self.IFCFile.setObjectName(u"IFCFile")

        self.gridLayout.addWidget(self.IFCFile, 0, 0, 1, 1)

        self.IfcPath = QPushButton(self.gridLayoutWidget_2)
        self.IfcPath.setObjectName(u"IfcPath")

        self.gridLayout.addWidget(self.IfcPath, 0, 1, 1, 1)

        self.Github = QPushButton(self.centralwidget)
        self.Github.setObjectName(u"Github")
        self.Github.setGeometry(QRect(30, 510, 225, 24))
        icon1 = QIcon(QIcon.fromTheme(u"go-home"))
        self.Github.setIcon(icon1)
        self.Kofi = QPushButton(self.centralwidget)
        self.Kofi.setObjectName(u"Kofi")
        self.Kofi.setGeometry(QRect(350, 510, 225, 24))
        self.Kofi.setIcon(icon1)
        AversioTools.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AversioTools)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QRect(0, 0, 662, 22))
        AversioTools.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AversioTools)
        self.statusbar.setObjectName(u"statusbar")
        AversioTools.setStatusBar(self.statusbar)

        self.retranslateUi(AversioTools)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AversioTools)
    # setupUi

    def retranslateUi(self, AversioTools):
        AversioTools.setWindowTitle(QCoreApplication.translate("AversioTools", u"Aversio Tools", None))
        self.IDS_Path.setText(QCoreApplication.translate("AversioTools", u"Set IDS File", None))
        self.IDS_Path.setProperty(u"Path", "")
        self.IDSFile.setText(QCoreApplication.translate("AversioTools", u"IDS File", None))
        self.ReportTemplate.setText(QCoreApplication.translate("AversioTools", u"Report template", None))
        self.ReportTemplate_Path.setText(QCoreApplication.translate("AversioTools", u"Set template", None))
        self.ReportTemplate_Path.setProperty(u"Path", "")
        self.Report.setText(QCoreApplication.translate("AversioTools", u"Report", None))
        self.Report_path.setText(QCoreApplication.translate("AversioTools", u"Set report file", None))
        self.Report_path.setProperty(u"Path", "")
        self.IDSDescription.setText(QCoreApplication.translate("AversioTools", u"IDS Check checks an IFC file against selected IDS file. The result is sorted (unfind items are at the end of file) and is written into .html file based on selected templates. Aversio Tools have templates in 4 languages, I encourage you to copy the one in your language and modify it to your needs.", None))
        self.IDSCheck.setText(QCoreApplication.translate("AversioTools", u"Run Check", None))
        self.ShowIDSReport.setText(QCoreApplication.translate("AversioTools", u"Show Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IDS), QCoreApplication.translate("AversioTools", u"IDS Check", None))
        self.ONDescription.setText(QCoreApplication.translate("AversioTools", u"ON Check checks an IFC file for manufacturer / model names. It is based on EN 2014/24/EU resp. (Czech law - \u00a7 89 odst. 5 z\u00e1kona \u010d. 134/2016 Sb., o zad\u00e1v\u00e1n\u00ed ve\u0159ejn\u00fdch zak\u00e1zek). Result of the check is a .html report file. The IFC is checked based on CSV file with manufacturer names and CSV file wih parameters to search in - based on your IDS.", None))
        self.CSVFile.setText(QCoreApplication.translate("AversioTools", u"CSV with manufacturer / model names", None))
        self.CSVPath.setText(QCoreApplication.translate("AversioTools", u"Set CSV", None))
        self.CSVPath.setProperty(u"Path", "")
        self.ONTemplatePath.setText(QCoreApplication.translate("AversioTools", u"Set template", None))
        self.ONTemplatePath.setProperty(u"Path", "")
        self.ONTemplate.setText(QCoreApplication.translate("AversioTools", u"Report template", None))
        self.ONReport.setText(QCoreApplication.translate("AversioTools", u"Report", None))
        self.ONReportPath.setText(QCoreApplication.translate("AversioTools", u"Set report file", None))
        self.ONReportPath.setProperty(u"Path", "")
        self.ONParamsPath.setText(QCoreApplication.translate("AversioTools", u"Set checked parameters", None))
        self.ONParamsPath.setProperty(u"Path", "")
        self.ONParams.setText(QCoreApplication.translate("AversioTools", u"Checked parameters", None))
        self.ONCheck.setText(QCoreApplication.translate("AversioTools", u"Run check", None))
        self.ShowONReport.setText(QCoreApplication.translate("AversioTools", u"Show report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ON), QCoreApplication.translate("AversioTools", u"ON Check", None))
        self.LogDescription.setText(QCoreApplication.translate("AversioTools", u"Log for cases where something is wrong", None))
        self.SaveLog.setText(QCoreApplication.translate("AversioTools", u"Save log file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log), QCoreApplication.translate("AversioTools", u"Log", None))
        self.IFCFile.setText(QCoreApplication.translate("AversioTools", u"IFC File", None))
        self.IfcPath.setText(QCoreApplication.translate("AversioTools", u"Set IFC File", None))
        self.IfcPath.setProperty(u"Path", "")
        self.Github.setText(QCoreApplication.translate("AversioTools", u"Github", None))
        self.Kofi.setText(QCoreApplication.translate("AversioTools", u"Kofi", None))
    # retranslateUi

