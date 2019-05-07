# -*- coding:utf-8 -*-

import os
import codecs
import configparser

proDir = os.path.split(os.getcwd())[0]
configPath = os.path.join(proDir, "Data", "config.ini")

class ReadConfig:
	def __init__(self):
		with open(configPath) as fd:
			data = fd.read()
	#BOM对于utf-16和utf-32有用，对于utf-8没啥大用。。所以能去掉就去掉
			#  remove BOM
			if data[:3] == codecs.BOM_UTF8:
				data = data[3:]
				with codecs.open(configPath, "w") as file:
					file.write(data)

		self.cf = configparser.ConfigParser()
		self.cf.read(configPath, encoding="utf-8-sig")


	def get_email(self, name):
		value = self.cf.get("EMAIL", name)
		return value

	def get_http(self, http, name):
		value = self.cf.get(http, name)
		return value

	def get_db(self, db, name):
		value = self.cf.get(db, name)
		return value

