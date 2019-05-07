#coding:utf8
import re

#!/usr/bin/python
template = "我要<歌手名>的<歌曲名>"

def subString1(template):
    copy = False
    finished = False
    slotList = []
    str = ""
    for s in template:
        if s=='<':
            copy = True
        elif s=='>':
            copy = False
            finished = True
        elif copy:
            str = str+s
        if finished:
            slotList.append(str)
            str = ""
            finished = False
    return slotList

def subString2(template):
    rule = r'<(.*?)>'
    slotList = re.findall(rule, template)
    return slotList


slotList = subString1(template)
for slot in slotList:
    print(slot)

slotList = subString2(template)
for slot in slotList:
    print(slot)
