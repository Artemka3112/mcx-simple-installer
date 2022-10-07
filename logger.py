import dearpygui.dearpygui as dpg

def addLogData(row):
    dpg.set_value("log","[LOG] - "+str(row)+"\n"+dpg.get_value("log"))

def addLogDataDebug(row):
    dpg.set_value("log","[DEBUG] - "+str(row)+"\n"+dpg.get_value("log"))

def addLogDataSuccess(row):
    dpg.set_value("log","[SUCCESS] - "+str(row)+"\n"+dpg.get_value("log"))
def addLogDataError(row):
    dpg.set_value("log","[ERROR] - "+str(row)+"\n"+dpg.get_value("log"))
