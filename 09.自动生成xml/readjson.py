import json
'''
with open('../dataconfig/login.json') as fp:
	data = json.load(fp)
print(data['login'])
'''

class ReadJson:
	'''
	读取json文件
	'''
	def __init__(self,file_path='./config/data.json'):
		self.file_path = file_path
		self.data = self.read_data()

	def read_data(self):
		'''
		读取json文件
		'''
		with open(self.file_path, encoding='UTF-8') as fp:
			data = json.load(fp)
		return data

	def get_data(self,id):
		'''
		获取json中某个id的值
		'''
		if id:
			return self.data[id]
		else:
			return None

	# def write_data(self,data):
	# 	with open('../config/data.json','w') as fp:
	# 		fp.write(json.dumps(data))


if __name__ == '__main__':
	print(ReadJson().get_data('Agency'))
