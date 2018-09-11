import threading
import multiprocessing
from multiprocessing import cpu_count, Process
from win32com.shell import shell, shellcon


class myThread (threading.Thread):

    def __init__(self, functions):
        threading.Thread.__init__(self)
        self.functions = functions
        self.result = object

    def run(self):
        self.functions()

    def get_result(self):
        return self.result


def Add_Thread(function, Method):
    thread = myThread(function)
    if Method == 'setDaemon':
        thread.setDaemon(True)
        thread.start()
    else:
        thread.start()
        thread.join()

    return thread


class myProcess(multiprocessing.Process):
    def __init__(self, functions):
        multiprocessing.Process.__init__(self)


def Add_Process(functions, Method):
    process = myProcess(functions)
    if Method == 'setDaemon':
        # process.setDaemon(True)
        process.start()
    else:
        process.start()
        process.join()
    return process


def ProgressDisplay(object, info):
    object.set(info)


def GetDesktopPath():
    ilist = shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_DESKTOP)
    return shell.SHGetPathFromIDList(ilist).decode().replace('\\', '/')
