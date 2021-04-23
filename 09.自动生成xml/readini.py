'''
读取报文节点
'''
from myconfigparser import MyConfigParser
import os


class ReadIni:
	def __init__(self,file_path,index=0):
		self.read_ini = MyConfigParser()
		self.file_path = file_path
		if index == 0:
			self.read_ini.read(file_path, encoding='UTF-8')
		

	def get_list_data(self, node):
		return self.read_ini.items(node) #返回Voucher节点下的数据[('admdivcode', '310000'), ('styear', ''), ('vtcode', ''), ('voudate', ''), ('voucherno', ''), ('paybankcode', ''), ('paybankname', ''), ('allflag', ''), ('xacctdate', ''), ('hold1', ''), ('hold2', '')]

	def get_sections_len(self):
		return len(self.read_ini.sections()) #返回第一层节点['Voucher', 'DetailList', 'Detail']

	def get_file_path(self):   #获得整个config文件夹下的文件名
		files = os.listdir(self.file_path)
		files_list = []
		for file in files:
			if file[-3:] == 'ini':
				files_list.append(os.path.join(self.file_path, file))
		return files_list


if __name__ == "__main__":
	#print(ReadIni('./config/').read_file_all_node("Voucher"))
		#print(file.get_list_data('Voucher'))
	#print(ReadIni().get_sections_len())
	files = ReadIni('./config/').get_file_path()
	for file in files:
		print(file)
		print(ReadIni(file).get_list_data("Voucher"))

