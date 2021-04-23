from readini import ReadIni
from main_one import CreateXml

class CreateXml_more:
	def __init__(self, file_paths):
		self.file_lists = ReadIni(file_paths).get_file_path()

	def main(self):
		for file in self.file_lists: 
			CreateXml(file).run_one_main()


if __name__ == "__main__":
	CreateXml_more('./config/').main()