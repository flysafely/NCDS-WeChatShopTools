import platform
import tkinter
import WPicAdjust
import PublicFunctions as pf
import GlobalValues as gv
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
from PIL import Image as im
from PIL import ImageTk as imt

Version = '1.0'

def Check_System_Info(screen_width, screen_height):
    system_info = platform.platform()
    if "Windows-7" in system_info or "Windows-10" in system_info:

        return {"geometry": '352x400+' + '%s+%s' % (screen_width, screen_height),
                "maxsize-x": 352,
                "maxsize-y": 400,
                "textwidth": 35,
                "buttonwidth": 43,
                "height": 1,
                }
    else:
        return {"geometry": '363x400+' + '%s+%s' % (screen_width, screen_height),
                "maxsize-x": 363,
                "maxsize-y": 400,
                "textwidth": 35,
                "buttonwidth": 45,
                "height": 1,
                }


def SelectFilePath(target,StringValue):
    if target =='dir':
        StringValue.set(tkinter.filedialog.askdirectory(initialdir=pf.GetDesktopPath()))
    else:
        StringValue.set(tkinter.filedialog.askopenfilename(initialdir=pf.GetDesktopPath()))

def LoadView():
    root = tkinter.Tk()
    root.title('微商城工具-v%s' % Version)
    ico = os.getcwd() + r'\wsc.ico'
    root.iconbitmap(ico)
    #root.attributes("-alpha", 0.1)
    screen_width = root.winfo_screenwidth() // 2 - 187
    screen_height = root.winfo_screenheight() // 2 - 260

    windows_params = Check_System_Info(
        root.winfo_screenwidth() // 2 - 187, root.winfo_screenheight() // 2 - 260)
    root.geometry(windows_params["geometry"])
    root.maxsize(windows_params["maxsize-x"], windows_params["maxsize-y"])
    root.minsize(windows_params["maxsize-x"], windows_params["maxsize-y"])
    textwidth = windows_params["textwidth"]
    buttonwidth = windows_params["buttonwidth"]
    height = windows_params["height"]
    # *********************************图像自动处理*****************************************
    # 功能区域-标题
    ImageAdjustForm = Frame(width=windows_params["maxsize-x"], height=windows_params["maxsize-y"]/3,bg='#87CEEB')
    ImageAdjustForm.grid(row=0, column=0,padx=0,pady=0)
    ToolTitle = Label(ImageAdjustForm, text='图片自动处理' ,font='微软雅黑 -15 bold',bg='#87CEEB').grid(
        column=2, row=1, columnspan=2, sticky=E + W)
    # 功能区域-图像处理-文件位置选择
    ImageAdjustLabel = Label(ImageAdjustForm, text='图片路径 ：',bg='#87CEEB').grid(
        column=1, row=2, columnspan=1, sticky=W)
    ImageAdjustPathTextValue = StringVar()
    ImageAdjustPathText = Entry(ImageAdjustForm, font='微软雅黑 -11', bg='#87CEEB', width=textwidth, state='readonly', textvariable=ImageAdjustPathTextValue, justify=LEFT).grid(
        column=2, row=2, sticky=N + S + E + W, columnspan=2)
    ImageAdjustPathButton = Button(ImageAdjustForm, text="✚", width=9, bg='#F0FFFF',height=height, command=lambda:SelectFilePath('dir',ImageAdjustPathTextValue)).grid(column=4, row=2, sticky=W+E, rowspan=1)
    # 功能区域-图像处理-文件保存位置选择    
    ImageAdjustLabel = Label(ImageAdjustForm, text='保存路径 ：',bg='#87CEEB').grid(
        column=1, row=3, columnspan=1, sticky=W)
    ImageSavePathTextValue = StringVar()
    ImageSavePathTextValue.set(pf.GetDesktopPath()+'/'+'微商城图片')
    ImageSavePathText = Entry(ImageAdjustForm, font='微软雅黑 -11',bg='#87CEEB', width=textwidth, state='readonly', textvariable=ImageSavePathTextValue, justify=LEFT).grid(
        column=2, row=3, sticky=N + S + E + W, columnspan=2)
    ImageSavePathButton = Button(ImageAdjustForm, text="✚", width=9, bg='#F0FFFF',height=height, command=lambda:SelectFilePath('dir',ImageSavePathTextValue)).grid(column=4, row=3, sticky=W+E, rowspan=1)    
    # 功能区域-图像处理-宽度
    ImageWidthLabel = Label(ImageAdjustForm, text='默认宽度 ：',bg='#87CEEB').grid(
        column=1, row=4, columnspan=1, sticky=W)
    ImageWidthTextValue = StringVar()
    ImageWidthTextValue.set(640)
    ImageWidthText = Entry(ImageAdjustForm, font='微软雅黑 -18', width=4,bg='#87CEEB', textvariable=ImageWidthTextValue, justify=CENTER).grid(
        column=2, row=4, sticky=N + S + E + W, columnspan=1)    
    # 功能区域-图像处理-执行情况打印
    ImageAdjustProcessTextValue = StringVar()
    gv._global_label = ImageAdjustProcessTextValue
    ImageAdjustProcessTextValue.set('准备开始')
    ImageAdjustProcessLabel= Label(ImageAdjustForm, font='微软雅黑 -9',justify=LEFT, textvariable=ImageAdjustProcessTextValue).grid(column=1, row=5, sticky=N + S + E + W, columnspan=4)    

    # 功能区域-图像处理-执行
    ImageAdjustStartButton =Button(ImageAdjustForm, text="开始处理", font='微软雅黑 -15 bold',width=9, bg='#F0FFFF',height=height, command=lambda:pf.Add_Thread(lambda:WPicAdjust.MultiStart(ImageAdjustPathTextValue.get(),ImageSavePathTextValue.get()),'setDaemon')).grid(column=3, row=4, sticky=W+E, columnspan=4) 

    # *********************************商品信息上传*****************************************
    # 功能区域-信息上传-标题
    ProductInfoUploadForm = Frame(width=windows_params["maxsize-x"], height=windows_params["maxsize-y"]/3,bg='#98FB98')
    ProductInfoUploadForm.grid(row=1, column=0,padx=0,pady=3)

    # 窗口主循环
    root.mainloop()


if __name__ == '__main__':
    #gv._init()
    LoadView()
