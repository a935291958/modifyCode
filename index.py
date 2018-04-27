# -*- coding: utf-8 -*-
import os, sys, re, shutil
from common import *

if __name__ != '__main__':
    sys.exit(1)

# 文件目录
fileDir = r'D:\cihuaTemp\yd_66551166_cn\templets\cihua'
# 需要转换的文件后缀名
need = ['.htm', '.html', '.js', '.css']
# 目标编码  例如utf-8,utf-16,ascii，文件内容为空会显示None
setCode = 'utf-8'

# =============================================================================#
# 编码换成小写
setCode = setCode.lower()

if not isDir(fileDir):
    msg('文件根目录错误，程序退出', 4)
    sys.exit(1)


def run(fileDir,setCode):
    if os.path.exists(fileDir):
        dirs = os.listdir(fileDir)
        # 遍历目录
        dirc = ''
        for dirc in dirs:
            # 转换编码，中文会乱码
            dirc = setUtf8(dirc)
            # 拼接成完整的路径
            thisPath = os.path.join(fileDir, dirc)
            if isFile(thisPath):

                # 匹配后缀名
                thisSplitext = os.path.splitext(thisPath)
                suffix = thisSplitext[1]

                if not suffix:
                    msg('未找到后缀名，已跳过:' + thisPath, 2)
                    continue
                if suffix in need:
                    msg('当前文件:' + thisPath, 1)
                    thisDetect = getDetect(thisPath)
                    if thisDetect['encoding'] == None:
                        msg('未匹配到文件编码，已跳过:' + thisPath, 2)
                        continue
                    # 匹配是不是目标编码
                    if thisDetect['encoding'].lower() != setCode:
                        # 读取文件然后转换编码
                        fo = open(thisPath, 'r')
                        foContent = fo.read()
                        fo.close()
                        # 判断是不是空白文件
                        if not foContent:
                            msg('未读取到文件内容，已跳过:' + thisPath, 2)
                            continue
                        # print foContent
                        # print thisDetect['encoding']
                        # print setCode
                        try:
                            setRes = setCodes(foContent, thisDetect['encoding'], setCode)
                            # print setRes
                            # 写入文件
                            fo = open(thisPath, 'w')
                            fo.write(setRes)
                            fo.close()
                            msg('转换成功:' + thisPath, 1)
                        except:
                            msg('文件写入失败:' + thisPath, 2)
            else:
                run(thisPath,setCode)
        pass
    pass



run(fileDir,setCode)