# -*- coding:utf-8 -*-

import os
from xlrd import open_workbook
import cx_Oracle
from xlutils.copy import copy
import requests
import json
import random
from datetime import date
import string
from xml.etree import ElementTree as ElementTree


database = {}
proDir = os.path.split(os.getcwd())[0]
dataPath = os.path.join(proDir, "Data", "interface.xls")
sql_path = os.path.join(proDir, "Data", "SQL.xml")

#从SQL.xml中读取SQL数据
def set_xml():
	if len(database) == 0:
		tree = ElementTree.parse(sql_path)
		for db in tree.findall("database"):
			db_name = db.get("name")
			table = {}
			for tb in db.getchildren():
				table_name = tb.get("name")
				#print(table_name)
				sql = {}
				for data in tb.getchildren():
					sql_id = data.get("id")
					#print(sql_id)
					sql[sql_id] = data.text.strip()
				table[table_name] = sql
			database[db_name] = table

def get_xml_dict(database_name, table_name):
	set_xml()
	database_dict = database.get(database_name).get(table_name)
	return database_dict

def get_sql(database_name, table_name, sql_id):
	db = get_xml_dict(database_name, table_name)
	sql = db.get(sql_id)
	return sql


#从excel中取值
def get_excel(cellname, pid, sheetname):
	cellname = str(cellname)
	pid = str(pid)
	sheetname = str(sheetname)
	fd = open_workbook(dataPath, formatting_info=True)
	sh = fd.sheet_by_name(sheetname)
	for row_index in range(sh.nrows):
		colvalue = sh.cell(int(row_index), 0).value
		if pid == colvalue:
			break
	for col_index in range(sh.ncols):
		rowvalue = sh.cell(0,int(col_index)).value
		if cellname == rowvalue:
			break
	cellvalue = sh.cell(row_index, col_index).value
	return cellvalue
#写入EXCEL
def set_excel(cellvalue, cellname, pid, sheetname):
	cellvalue = str(cellvalue)
	if cellname == "请求报文" or cellname == "返回报文":
		cellvalue = cellvalue.replace(" ", "\n")
	cellname = str(cellname)
	pid = str(pid)
	sheetname = str(sheetname)
	fd = open_workbook(dataPath, formatting_info=True)
	sh = fd.sheet_by_name(sheetname)
	for row_index in range(sh.nrows):
		colValue = sh.cell(int(row_index), 0).value
		if pid == colValue:
			break
	for col_index in range(sh.ncols):
		rowvalue = sh.cell(0, int(col_index)).value
		if cellname == rowvalue:
			break
	sheetIndex = fd._sheet_names.index(sheetname)
	wb = copy(fd)
	sheet = wb.get_sheet(sheetIndex)
	sheet.write(row_index, col_index, cellvalue)
	wb.save(dataPath)
#获取sheet页行数
def get_excelnrows(sheetname):
	sheetname = str(sheetname)
	fd = open_workbook(dataPath, formatting_info=True)
	sh = fd.sheet_by_name(sheetname)
	return sh.nrows

#获取身份证号
def get_idcard(maxage=60, minage=20):
	#获取生日
	now = date.today()
	birth = now.year - int(minage)
	mon = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12']
	mon_days = ['31', '28', '31', '30', '31', '30', '31', '31','30', '31', '30', '31']
	age = int(maxage) - int(minage)
	y = str(birth - random.randint(1, age))
	index1 = random.randint(0, 11)
	m = str(mon[index1])
	m = m.zfill(2)
	maxDay = int(mon_days[index1])
	d = str(random.randint(1, maxDay))
	d = d.zfill(2)
	s = y + m + d
	area = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41", "42", "43", "44","45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65", "71", "81", "82", "91"]
	id = random.choice(area)+''.join(random.choice(string.digits) for i in range(4))+s+''.join(random.choice(string.digits) for i in range(3))
	id = id[0:17]
	lid = list(id)
	temp = 0
	for nn in range(2, 19):
		a = int(lid[18 - nn])     # 17到1的数
		w = (2 ** (nn - 1)) % 11  # 17到1的系数
		temp += a * w             # temp = temp+a*w 17位数字和系数相乘的结果相加
	temp = (12 - temp % 11) % 11
	if temp >= 0 and temp <= 9:
		id += str(temp)
	elif temp == 10:
		id += 'X'
	return id
#获取汉字
def get_gbk2312(number):
	str1 = ""
	for i in range(number):
		head = random.randint(0xb0, 0xf7)
		body = random.randint(0xa1, 0xf9)
		val = f'{head:x}{body:x}'
		str = bytes.fromhex(val).decode('gb2312')
		str1 += str
	return str1
#获取手机号
def get_phonenumber():
	prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
	return random.choice(prelist)+''.join(random.choice(string.digits) for i in range(8))

def get_xls(xls_name, sheet_name):
	cls = []
	xlsPath = os.path.join(proDir, "Data", xls_name)
	file = open_workbook(xlsPath)
	sheet = file.sheet_by_name(sheet_name)
	nrows = sheet.nrows
	for i in range(1, nrows):
		if True:
			cls.append(sheet.row_values(i))
	return cls

#生成随机数字
def get_number(number):
	s = ''.join(random.choice(string.digits) for i in range(number))
	return s

