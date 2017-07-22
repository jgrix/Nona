import sys

from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl, pyqtSignal
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlApplicationEngine, qmlRegisterSingletonType
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from time import sleep
import _thread

class ThermoStat(QObject):

    currentTempChanged = pyqtSignal()
    windChanged = pyqtSignal()
    targetTempChanged = pyqtSignal()
    modeChanged = pyqtSignal()
    _instance = None

    def __init__(self, parent=None):
        global gWind, gCurrentTemp, gTargetTemp, gMode
        super().__init__(parent)
        self._wind = 'Calm'
        self._currentTemp = 70
        self._targetTemp = 70
        self._mode = 0 #0 = off, 1 = heat, 2 = cool

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(ThermoStat, self).__new__(self, *args, **kwargs)
        return self._instance

    @pyqtProperty('QString', notify=windChanged)
    def wind(self):
        return self._wind
    
    @wind.setter
    def wind(self, wind):
        self._wind = wind
        windChanged.emit()
    

    @pyqtProperty(int, notify=currentTempChanged)
    def currentTemp(self):
        #print("current temp getter: ", self._currentTemp)
        return self._currentTemp

    @currentTemp.setter
    def currentTemp(self, ct):
        self._currentTemp = ct
        print("current temp setter: ", ct, self._currentTemp)
        self.currentTempChanged.emit()


    @pyqtProperty(int, notify=targetTempChanged)
    def targetTemp(self):
        return self._targetTemp

    @targetTemp.setter
    def targetTemp(self, tt):
        self._targetTemp = tt
        #print("target temp setter: ", tt, self._targetTemp)
        print("test2: ", id(self))
        self.targetTempChanged.emit()

    @pyqtProperty(int, notify=modeChanged)
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, m):
        self._mode = m
        print("mode setter: ", m, self._mode)
        self.modeChanged.emit()

    def createThermoStatProxy(engine, script_engine):
        return ThermoStat()

    def test(self, inc):
        print("test1: ", id(self))
        self._targetTemp = inc
        self.targetTempChanged.emit()



def Read_current_Tempature():
        "Reads the current Tempature"
        therm = ThermoStat()
        aTemp = 2

        while True:
            sleep(5)
            aTemp = aTemp + 1
            therm.test(aTemp)


pass

if __name__ == "__main__":
    #qmlRegisterType(ThermoStat, 'ThermoStat', 1, 0, 'Therm')
    qmlRegisterSingletonType(ThermoStat, "ThermoStat", 1, 0, "Therm", ThermoStat.createThermoStatProxy)

    _thread.start_new_thread(Read_current_Tempature, ())


    # Create a QML engine.
    app = QGuiApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl.fromLocalFile("UI.qml"))
    view.show()
    app.exec()

# Create a component factory and load the QML script.
#component = QQmlComponent(engine)
#component.loadUrl(QUrl('UI.qml'))

# Create an instance of th  e component.
#person = component.create()
