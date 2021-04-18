import sys

from PySide2.QtCore import QCoreApplication, QUrl, Qt, QObject, Signal, Slot, Property
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

url = QUrl.fromLocalFile('test.qml')
engine.load(url)
if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
