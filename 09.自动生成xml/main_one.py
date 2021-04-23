 #导入minidom
from xml.dom import minidom
from readini import ReadIni
from readjson import ReadJson

class CreateXml:
	def __init__(self, file_path):
		self.file_path = file_path
		self.readini = ReadIni(file_path)
		self.json_data = ReadJson().get_data("Agency")
		self.dom = minidom.Document()  # 1.创建DOM树对象
		self.voucher_node = self.dom.createElement('Voucher')# 2.创建根节点。每次都要用DOM对象来创建任何节点。
		self.dom.appendChild(self.voucher_node)


	def run_one_main(self):
		#主程序入口
		if self.readini.get_sections_len() != 1: #获得ini文件的第一层节点长度，若index不等于1,有detail;等于1，没有detail
			self.create_voucher_child()
			self.create_detail_child()
			self.write_txt()
		else:
			self.create_voucher_child()
			self.write_txt() 


	def create_voucher_child(self):
		#创建没有detail的报文
		list_data = self.readini.get_list_data('Voucher')
		for data in list_data:			
			voucher_data_node = self.dom.createElement(data[0])
			self.voucher_node.appendChild(voucher_data_node)
			for key,value in self.json_data.items():
				if data[1] != "":   #如果ini里有值，用ini ，无值用json
					voucher_data_text = self.dom.createTextNode(data[1])
					# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
					voucher_data_node.appendChild(voucher_data_text)
					break
				elif data[1] == "" and data[0] == key:
					voucher_data_text = self.dom.createTextNode(value)
					# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
					voucher_data_node.appendChild(voucher_data_text)
					break

	def create_detail_child(self):
	 	#创建有detail的报文,detail会循环
		list_data = self.readini.get_list_data('Detail')
		detail_num = self.detail_num()
		self.detaillist_node = self.dom.createElement('DetailList')
		self.voucher_node.appendChild(self.detaillist_node)
		# self.readini.get_list_data(node_name)[0]
		for i in range(detail_num):
			self.detail_node = self.dom.createElement('Detail')
			self.detaillist_node.appendChild(self.detail_node)
			for data in list_data:			
				detail_data_node = self.dom.createElement(data[0])
				self.detail_node.appendChild(detail_data_node)
				for key,value in self.json_data.items():
					if data[1] != "":
						detail_data_text = self.dom.createTextNode(data[1])
						# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
						detail_data_node.appendChild(detail_data_text)
						break
					elif data[0] == key and data[1] == "":
						detail_data_text = self.dom.createTextNode(value)
						# 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
						detail_data_node.appendChild(detail_data_text)
						break

	def write_txt(self):
		#将组好的报文写入txt文件
		file_name = './file_xml/' + self.file_path[-8:-4] + '.txt'
		try:
			with open(file_name,'w',encoding='UTF-8') as fh:
				# 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
				# 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
				self.dom.writexml(fh,indent='',addindent='\t',newl='\n',encoding='GBK')
				print('OK')
		except Exception as err:
			print('错误：{err}'.format(err=err))

	def detail_num(self):
		#获取detail的笔数
		list_data = self.readini.get_list_data("DetailList")
		return int(list_data[0][1])


if __name__ == "__main__":
	# createxml = CreateXml(1)
	# createxml.create_voucher_child()
	# createxml.create_detail_child()
	# createxml.write_txt()
	CreateXml('./config/5952.ini').run_one_main()





