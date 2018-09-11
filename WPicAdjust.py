import GlobalValues as gv
import os.path
import base64
import tkinter
import time
import threading
import PublicFunctions as pf
from tkinter.filedialog import *
from multiprocessing import cpu_count, Process, Pool
from PIL import Image as im

threshold = 10


class myThread (threading.Thread):

    def __init__(self, functions):
        threading.Thread.__init__(self)
        self.functions = functions
        self.result = object

    def run(self):
        self.functions()

    def get_result(self):
        return self.result


def Add_Thread(function):
    thread = myThread(function)
    # thread.setDaemon(True)
    thread.start()
    thread.join()
    return thread


def GetPictureSize(picture):
    with im.open(picture) as picHandle:
        return {'width': picHandle.size[0], 'height': picHandle.size[1]}


def ResizeLock(picPath, width, Save_Path):
    saveFilePath = Save_Path + '/' + os.path.split(os.path.dirname(
        os.path.dirname(picPath)))[1] + '/' + os.path.split(os.path.dirname(picPath))[1]
    if os.path.exists(saveFilePath) == False:
        os.makedirs(saveFilePath)
    with im.open(picPath) as picHandle:
        W, H = picHandle.size
        new_img = picHandle.resize(
            (width, int(H / W * width)), im.BILINEAR)
        pf.Add_Thread(lambda: new_img.save(
            saveFilePath + '/' + os.path.split(picPath)[1]), 'setDaemon')
        print('正在处理:' + picPath)


def AddMark():
    pass


def CropPic(picPath, cropParams, Save_Path):

    saveFilePath = Save_Path + '/' + os.path.split(os.path.dirname(
        os.path.dirname(picPath)))[1] + '/' + os.path.split(os.path.dirname(picPath))[1]
    if os.path.exists(saveFilePath) == False:
        os.makedirs(saveFilePath)
    with im.open(picPath) as picHandle:
        W, H = picHandle.size
        if abs(W - H) < threshold:
            new_img = picHandle.resize(
                (cropParams[0], cropParams[1]), im.BILINEAR)

            pf.Add_Thread(lambda: new_img.save(
                saveFilePath + '/' + os.path.split(picPath)[1]), 'setDaemon')
            print('正在处理:' + picPath)
        else:
            if W > H:
                new_img = picHandle.crop(((W - H) / 2, 0, (W + H) / 2, H))

                pf.Add_Thread(lambda: new_img.save(
                    saveFilePath + '/' + os.path.split(picPath)[1]), 'setDaemon')

            else:
                new_img = picHandle.crop((0, (H - W) / 2, W, (H + W) / 2)).resize(
                    (cropParams[0], cropParams[1]), im.BILINEAR)

                pf.Add_Thread(lambda: new_img.save(
                    saveFilePath + '/' + os.path.split(picPath)[1]), 'setDaemon')
                print('正在处理:' + picPath)


def StartAdjust(picPath, Save_Path, cropParams=(640, 640), resizeWidth=640):
    picInfo = GetFileInfo(picPath)
    # print(picInfo)
    if picInfo['picName'][0].upper() == 'T':
        # print('T')
        CropPic(picPath, cropParams, Save_Path)
    elif picInfo['picName'][0].upper() == 'X':
        # print('X')
        ResizeLock(picPath, resizeWidth, Save_Path)
    else:
        print('图片命名有问题！')


def CheckPicInfo(filepath):
    picPathList = []
    for path, files, pics in os.walk(filepath):
        if pics:
            for pic in pics:
                if pic.split('.')[1].upper() in ['JPG', 'PNG']:
                    picPathList.append(
                        '/'.join((path.replace('\\', '/'), pic)))
    # print(picPathList)
    return picPathList


def GetFileInfo(picPath):
    (filepath, tempfilename) = os.path.split(picPath)
    (shotname, extension) = os.path.splitext(tempfilename)

    return {'fileName': os.path.split(os.path.dirname(picPath))[1], 'picName': shotname + extension}


def Start(pathlist, Save_Path, width, ProcessNum):
    for picPath in pathlist:
        StartAdjust(picPath, Save_Path, cropParams=(
            width, width), resizeWidth=width)
    return '第%d核心处理%d张图片结束！' % (ProcessNum, len(pathlist))


def Distribute(AllPathList):
    DistributeDPathList = []
    Path_Count = len(AllPathList)
    CPU_Count = cpu_count()
    m = Path_Count % CPU_Count
    step = (Path_Count - m) / CPU_Count

    for i in range(CPU_Count):
        if i == CPU_Count - 1:
            DistributeDPathList.append(
                AllPathList[int(i * step):])
        else:
            DistributeDPathList.append(
                AllPathList[int(i * step):int((i + 1) * step)])
    return DistributeDPathList


def MultiStart(PicsFilePath, PicsSavePath, object):
    PicWidth = gv.get_value('width')
    AllPathList = CheckPicInfo(PicsFilePath)
    CPU_Count = cpu_count()
    object.ImageAdjustButton.setEnabled(False)
    time.sleep(0.1)
    AllPic_Count = len(AllPathList)
    if CPU_Count < 2 or AllPic_Count <= CPU_Count:
        info = '启用单核心处理%d张图片...请稍后' % AllPic_Count
        object.RefreshStatusbar(info)
        Start(AllPathList, PicsSavePath)
    else:
        info = '启用%d核心处理%d张图片...请稍后' % (CPU_Count, AllPic_Count)
        object.RefreshStatusbar(info)
        Queue = []
        i = 1
        QueuePool = Pool(processes=CPU_Count)
        for EachPathList in Distribute(AllPathList):
            print('启动核心%d' % i)
            i += 1
            QueuePool.apply_async(
                Start, (EachPathList, PicsSavePath, PicWidth, i), callback=object.RefreshStatusbar)
        QueuePool.close()
        QueuePool.join()
    object.RefreshStatusbar('%d张图片处理完成' % AllPic_Count)
    object.ImageAdjustButton.setEnabled(True)


if __name__ == '__main__':

    MultiStart()
