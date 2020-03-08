import tornado.web
from tornado.options import options
import pymongo
from pymongo import MongoClient
import random
import setting

import io
import os.path

import json
import subprocess
import math

# from db import DB 
# from dataconfig import DataConfig 

MONGOHOST = '47.103.22.185'
MONGODB = 'lsd_new'

#创建client连接mongodb
client = MongoClient(MONGOHOST,27017) #27017是默认端口
db = client[MONGODB]
MONGOCOLLECTION = 'userstudy'
my_collection = db[MONGOCOLLECTION]
data_transform_flag = 1
datas = []

class NewDataHandler(tornado.web.RequestHandler):
	def post(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		global datas	
		datas = list(my_collection.find())
		global data_transform_flag
		data_transform_flag = 0
		self.write({'status': 'ok'})

class InfoHandler(tornado.web.RequestHandler):
	def post(self):	
		global data_transform_flag
		while(data_transform_flag):
			pass
		self.set_header('Access-Control-Allow-Origin', '*')
		user_id = self.get_argument('id')
		accuracy = self.accuracy_rate(datas, user_id)
		total_test_num = self.test_count(datas, user_id)
		test_type = self.test_type(user_id)
		# self.test_type(user_id)
		self.write({
			'result': 'ok',
			'accuracy':accuracy,
			'total_test_num':total_test_num,
			'test_type':test_type
		})

	def accuracy_rate(self,datas, id_):
		test_num = 0
		correct_num = 0
		for data in datas:
			if 'tests' in list(data.keys()):
				if int(data['id']) == int(id_):
					for test in data['tests']:
						if test['answer'] == 1:
							correct_num += 1
					test_num += len(data['tests'])
					
		return round(correct_num/test_num*100,2)

	def test_count(self,datas,id_):
		test_num = 0
		for data in datas:
			if 'tests' in list(data.keys()):
				if int(data['id']) == int(id_):
					test_num += len(data['tests'])
		return test_num

	def test_type(self,id_):
		int_user = list(my_collection.find({'id':int(id_)}))
		str_user = list(my_collection.find({'id':str(id_)}))
		if len(int_user)>=1:
			return int_user[-1]['type']
		else:
			return str_user[-1]['type']

