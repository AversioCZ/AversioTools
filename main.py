import sys
from PySide6 import QtWidgets, Qt3DCore
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PySide6.QtCore import QStringListModel

# Import the generated UI file
from ui_AversioTools import Ui_AversioTools # Replace MainWindow with the main window class name.

# Import IDS Checker files
from IDSChecker.checker import AversioHtml
import ifcopenshell
import ifctester as tst
from ifctester import ids, reporter
from ifctester.ids import Specification, Ids
from ifcopenshell.util.file import IfcHeaderExtractor
import webbrowser

# Import ON Checker files
from ONChecker.ON_search import AversioON

class MainWindow(QtWidgets.QMainWindow, Ui_AversioTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Parametry pro Kontrolu IDS
        self.IfcPath.clicked.connect(lambda: self.setfile("IfcPath","", "Ifc files (*.ifc);;All Files (*)"))
        self.IDS_Path.clicked.connect(lambda: self.setfile("IDS_Path", "./IDSChecker/IDS examples","IDS files (*.ids);;All Files (*)"))
        self.ReportTemplate_Path.clicked.connect(lambda: self.setfile("ReportTemplate_Path", "./IDSChecker/Report templates","Html files (*.html)"))
        self.Report_path.clicked.connect(lambda: self.setfile("Report_path", "C:/","Html files (*.html)"))
        self.IDSCheck.clicked.connect(lambda: self.checkids(self.IfcPath_Path,self.IDS_Path_Path,self.Report_path_Path,self.ReportTemplate_Path_Path))
        self.ShowIDSReport.clicked.connect(lambda: webbrowser.open('file://'+self.Report_path_Path))
        
        # Parametry pro Kontrolu ON
        self.CSVPath.clicked.connect(lambda: self.setfile("CSVPath", "./ONChecker/Manufacturer files", "CSV files (*.csv);;All files (*)"))
        self.ONParamsPath.clicked.connect(lambda: self.setfile("ONParamsPath","./ONChecker/Parameter files","CSV files (*.csv);;All files (*)"))
        self.ONReportPath.clicked.connect(lambda: self.setfile("ONReportPath","C:/","Html files (*.html)"))
        self.ONTemplatePath.clicked.connect(lambda: self.setfile("ONTemplatePath","./ONChecker/Report templates","Html files (*.html)"))
        self.ONCheck.clicked.connect(lambda: self.checkon(self.IfcPath_Path,self.CSVPath_Path,self.ONParamsPath_Path,self.ONReportPath_Path,self.ONTemplatePath_Path))
        self.ShowONReport.clicked.connect(lambda: webbrowser.open('file://'+self.ONReportPath_Path))

        # Home redirectos
        self.Github.clicked.connect(lambda: webbrowser.open('https://github.com/AversioCZ'))
        self.Kofi.clicked.connect(lambda: webbrowser.open('https://ko-fi.com/aversiocz'))

    # Kontrola dle IDS

    def setfile(self, btt,defpath, filetypes):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", defpath, filetypes)
        if file_name:
            # Assuming you have a way to access the relevant widget based on btt.
            # You might need a dictionary or a naming convention.
            target_widget = getattr(self, btt) # get the widget using the string of the name.
            target_widget.setText(file_name)
            self.update_path(btt, file_name)  # Call a function that handles the path update

    def update_path(self, btt, path):
        # Update the path in your application logic
        print(f"[Aversio tools attribute set]: Path for {btt}: {path}", file=sys.stderr) # for debug purposes.
        # Here you would typically store the path in a variable or a setting.
        if btt == "IfcPath":
            self.IfcPath_Path = path # example of storing the path.
        if btt == "IDS_Path":
            self.IDS_Path_Path = path
        if btt == "ReportTemplate_Path":
            self.ReportTemplate_Path_Path = path
        if btt == "Report_path":
            self.Report_path_Path = path
        if btt == "CSVPath":
            self.CSVPath_Path = path
        if btt == "ONParamsPath":
            self.ONParamsPath_Path = path
        if btt == "ONReportPath":
            self.ONReportPath_Path = path
        if btt == "ONTemplatePath":
            self.ONTemplatePath_Path = path
        # add more if statements for each button you have.

    def checkids(self,ifc_file,ids_file,report_file,reptemplatepath):
        my_ifc = ifcopenshell.open(ifc_file)
        my_idss = ids.open(ids_file)
        my_idss.validate(my_ifc)
        engine = AversioHtml(my_idss)
        engine.report()
        extractor = IfcHeaderExtractor(ifc_file)
        header_info = extractor.extract()
        engine.results["ifcdescription"]=header_info.get("description")
        engine.results["ifcname"]=header_info.get("name")
        engine.results["ifctimestamp"]=header_info.get("time_stamp")
        engine.results["ifcfilepath"]=ifc_file
        engine.sortby_status()
        engine.to_file(report_file, reptemplatepath)
        # Assign your output to the OUT variable.
        # reporter.Console(my_idss).report()
        return(reporter.Console(my_idss).report())

    # Kontrola obchodních názvů
    def checkon(self,ifc_file,csv_file,paramfile,reportfile,templatefile):
        checker = AversioON()
        extractor = IfcHeaderExtractor(ifc_file)
        header_info = extractor.extract()
        checker.results["ifcdescription"]=header_info.get("description")
        checker.results["ifcname"]=header_info.get("name")
        checker.results["ifctimestamp"]=header_info.get("time_stamp")
        checker.results["ifcfilepath"]=ifc_file
        keywords = checker.load_keywords_from_csv(csv_file)
        attributes = checker.load_attributes_from_csv(paramfile)
        results = checker.search_ifc_for_keywords(ifc_file,keywords,attributes)
        checker.to_file(reportfile,templatefile)
        return results



class ErrorStream:
    def __init__(self, log_view):
        self.log_view = log_view
        self.model = QStringListModel()
        self.log_view.setModel(self.model)

    def write(self, message):
        self.model.setStringList(self.model.stringList() + [message.strip()])
        self.log_view.scrollToBottom()

    def flush(self):
        pass  # Required for file-like objects

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    log_view = window.AversioToolLog

    # Redirect stderr to the log view
    sys.stderr = ErrorStream(log_view)

    sys.exit(app.exec())