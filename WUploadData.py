import requests
import time
import ProductFields
import json
import xlrd
import AppConfig
import threading
import hashlib
import copy
import gc
import base64
import os
import tkinter
import PublicFunctions as pf
from tkinter.filedialog import *

TempXLSXMD5 = "385af58f01fa876fc285b3c1dff1b6f8"

# ***********************公用功能**************************


def GetMD5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    result = m.hexdigest()
    return result


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


def GetSessionID(username, Ekey):
    s = requests.session()
    try:
        r = s.get(AppConfig.LOGIN_URL + 'username=' +
                  username + '&password=' + Ekey)
    except KeyError:
        raise KeyError
        # print(r.cookies.values()[0])
    finally:

        return r.cookies.values()

# ***********************上传商品信息**************************


def FormatSkuModelsData(data, bonusPointsRate, salePrice):

    if not data:

        return []
    else:
        SKUModels = []
        SKUModelList = data.split('&')
        for skumodel in SKUModelList:
            SKUModel = copy.deepcopy(ProductFields.SkuModels)
            SKUModelInfo = skumodel.split('*')
            SKUModel['quantityAvailable'] = skumodel.split('*')[1]
            SKUModel['bonusPointsRate'] = bonusPointsRate
            SKUModel['salePrice'] = salePrice
            SKUModel['optionModels'] = []
            optionList = SKUModelInfo[0].split('#')
            for option in optionList:
                # print('添加前',SKUModel['optionModels'])
                optionNameInfo = option.split('%')
                optionDict = copy.deepcopy(ProductFields.OptionName)
                optionDict['optionNameId'] = optionNameInfo[0]
                optionDict['optionValueNameId'] = optionNameInfo[1]

                SKUModel['optionModels'].append(optionDict)
                # print('添加后',SKUModel['optionModels'])
            SKUModels.append(SKUModel)
        # print(SKUModels)
        return SKUModels


def CheckTempXlSX(fields, rowcount):
    if fields == AppConfig.TempXLSXMD5 and rowcount > 2:
        return True
    else:
        return False


def PostDataProcessing(filePath, username, password, method, object):
    fileHandler = xlrd.open_workbook(filePath)
    Sheet = fileHandler.sheet_by_index(0)
    object.RefreshStatusbar('开始准备上传数据...请稍后')
    #object.PostDataButton.setEnabled(False)
    #time.sleep(0.5)
    URL = AppConfig.METHOD[method]['URL']
    JSESSIONID = GetSessionID(username, GetMD5(password))
    if JSESSIONID:
        cookie = {"JSESSIONID": JSESSIONID[0]}

        FieldsList = Sheet.row_values(1)
        Row_Count = len(Sheet.col_values(7))
        Column_Count = len(FieldsList)
        # print(Column_Count)
        if CheckTempXlSX(GetMD5(''.join(FieldsList)), Row_Count):
            for i in range(2, Row_Count):
                postData = copy.deepcopy(ProductFields.AddData)
                for j in range(Column_Count - 1):
                    if j <= 38:
                        postData["productBasicModel"][Sheet.cell(1, j).value] = str(Sheet.cell(
                            i, j).value).replace('.0', '')
                    else:
                        #print(i,j,Sheet.cell(i, j).value)
                        postData["skuModels"] = FormatSkuModelsData(
                            Sheet.cell(i, j).value, postData["productBasicModel"]["bonusPointsRate"], postData["productBasicModel"]['salePrice'])

                        postData["id"] = postData["productBasicModel"]["productId"]
                postData["productBasicModel"]['mediaModels'] = []
                postData["productBasicModel"]['models'] = []
                # print(postData)
                Datas = json.dumps(postData, ensure_ascii=False).encode()

                object.RefreshStatusbar(
                    "上传%s数据中..." % postData["productBasicModel"]['productName'])
                pf.Add_Thread(lambda: StartOperating(URL, Datas, cookie,
                                                     postData["productBasicModel"]['productName']), 'setDaemon')
            #object.PostDataButton.setEnabled(True)
            object.RefreshStatusbar('上传%s条商品信息数据完成...' % str(Row_Count-2))
        else:
            object.RefreshStatusbar('导入数据或者模板有误！')
            object.PostDataButton.setEnabled(True)
    else:
        object.RefreshStatusbar('账号密码错误！')
        object.PostDataButton.setEnabled(True)
        return False
    object.PostDataButton.setEnabled(True)
    for x in locals().keys():
        del locals()[x]
    gc.collect()


# ***********************上传商品图片**************************

def PostImageProcessing(filePath, username, password, method, object):
    URL = AppConfig.METHOD[method]['URL']
    #object.ImageAdjustButton.setEnabled(False)
    #time.sleep(0.1)
    JSESSIONID = GetSessionID(username, GetMD5(password))
    if JSESSIONID:
        cookie = {"JSESSIONID": JSESSIONID[0]}
        PicsInfo = GetPicsInfo(filePath)
        for picinfo in PicsInfo:
            postData = json.dumps(FormatImagePostData(
                picinfo), ensure_ascii=False).encode()
            object.RefreshStatusbar("上传'%s'商品信息..." % picinfo[0])
            pf.Add_Thread(lambda: StartOperating(
                URL, postData, cookie, picinfo[0]), 'setDaemon')

    else:
        object.RefreshStatusbar('账号密码错误！')
        return False
    #object.ImageAdjustButton.setEnabled(True)


def FormatImagePostData(picinfo):
    TempData = ProductFields.ImageData
    # print(picinfo)
    TempData[0]['productId'] = int(picinfo[0])
    for item in picinfo[1]:
        Initials = os.path.split(item['picPath'])[1][0].upper()
        if Initials == 'T':
            TempImageStr = 'data:image/%s;base64,%s' % (
                item['picExtension'], GetPicBase64(item['picPath']))
            TempData[0]['mainImgs'].append(TempImageStr)
        elif Initials == 'X':
            TempImageStr = 'data:image/%s;base64,%s' % (
                item['picExtension'], GetPicBase64(item['picPath']))
            TempData[0]['detailImgs'].append(TempImageStr)

    return TempData


def GetPicsInfo(filepath):
    picInfoList = []
    for path, files, pics in os.walk(filepath):
        if pics and not files:
            picID = os.path.split(path)[1]
            picList = (picID, [])
            for pic in pics:
                picpath = '/'.join((path.replace('\\', '/'), pic))
                Extension = pic.split('.')[1].lower()

                if Extension == 'jpg' and picID.isdigit() and len(picID) >= 4:
                    picList[1].append(
                        {'picPath': picpath, 'picExtension': "jpeg"})
                elif Extension == 'png' and picID.isdigit() and len(picID) >= 4:
                    picList[1].append(
                        {'picPath': picpath, 'picExtension': "png"})
            picInfoList.append(picList)
    return picInfoList


def GetPicBase64(PicPath):
    with open(PicPath, "rb") as f:
            # b64encode是编码，b64decode是解码
        return base64.b64encode(f.read()).decode()


def StartOperating(URL, Datas, cookie, Tag):

    print("上传'%s'商品信息..." % Tag)
    try:
        res = requests.post(URL, data=Datas, cookies=cookie,
                            headers=AppConfig.HEADER)
    except KeyError:
        raise KeyError
    #print('Get in StartOperating')
    print(CodeInfo(res.json()))


def CodeInfo(info):
    if str(info['code']) == '200':
        return '添加成功!'
    else:
        return '添加失败!' + repr(info)


def Start(username, password, Method):
    if Method == 'Add':
        filepath = tkinter.filedialog.askopenfilename()
        return PostDataProcessing(filepath, username, GetMD5(password), Method)

    else:
        filepath = tkinter.filedialog.askdirectory()
        return PostImageProcessing(filepath, username, GetMD5(password), Method)


if __name__ == '__main__':
    # print(GetMD5('Xaf19901102'))
    Start('wjkun', '123456', 'Add')
