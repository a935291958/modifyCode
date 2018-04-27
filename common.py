# -*- coding: utf-8 -*-
import os, re, shutil, time

import chardet

# 创建日志目录
if not os.path.isdir('./log'):
    os.mkdir('./log')


# 写入日志
def msg(str, type):
    if not str or not type:
        print '日志相关异常'
        return False

    msg = ''
    pMsg = ''

    # 打开日志文件
    f = './log/' + time.strftime("%Y-%m-%d", time.localtime()) + '.log'
    fLog = open(f, 'a')

    # 拼接提示信息
    msg = time.strftime("%H:%M:%S", time.localtime()) + '] ' + str

    if (type == 1):
        msg = '[INFO] [' + msg
        pMsg = '\033[0;32;40m ' + msg

    elif type == 2:
        msg = '[WARNING] [' + msg
        pMsg = '\033[0;33;40m ' + msg

    elif type == 3:
        msg = '[ALERT] [' + msg
        pMsg = '\033[0;35;40m ' + msg

    elif type == 4:
        msg = '[ERROR] [' + msg
        pMsg = '\033[0;31;40m ' + msg

    elif type == 5:
        msg = '[SUCCESS] [' + msg
        pMsg = '\033[0;37;40m ' + msg
    else:
        print  'type参数错误!'
        fLog.close()
        return False

    print pMsg

    fLog.write(msg + '\n')
    fLog.close()

    pass


# 判断是不是文件
def isFile(filename):
    return os.path.isfile(filename)


# 判断是不是目录
def isDir(dir):
    return os.path.isdir(dir)


# 递归删除目录，非空的也可以删除
def remove_dir(dir):
    dir = dir.replace('\\', '/')
    if (os.path.isdir(dir)):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir, p))
        if (os.path.exists(dir)):
            os.rmdir(dir)
    else:
        if (os.path.exists(dir)):
            os.remove(dir)
    pass


# 获取文件编码
def getDetect(filename):
    if not isFile(filename):
        return False
    f = open(filename, 'r')
    fileData = f.read()
    f.close()
    return chardet.detect(fileData)


# 设置文本为utf-8
def setUtf8(str):
    return str.decode('gbk').encode('utf-8')


# 设置文本为gbk
def setGbk(str):
    return str.decode('utf-8').encode('gbk')


# 设置文件编码
def setCodes(foContent,old, new):
    return foContent.decode(old).encode(new)




