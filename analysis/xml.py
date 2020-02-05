import os 
import logging as lg

lg.basicConfig(level=lg.debug)

def launch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_file = os.path.join(directory,"data",data_file)
	
	try:	
		with open(path_to_file, 'r') as file:
				preview = file.readline()
				lg.debug(preview)
	except FileNotFoundError as e :
		lg.critical("File Not Found, Message is : {}".format(e))
	finally:
		lg.debug("#### ANALYSIS IS OVER ####")


def main():
	launch_analysis('syseronBrut.xml')
	pass

if __name__ == '__main__':
	main()
