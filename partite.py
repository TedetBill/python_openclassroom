#! /usr/bin/env python3
# coding: utf-8

import argparse

import analysis.csv as c_an
import analysis.xml as x_an 
import logging as lg

def parse_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e","--extension",help="""XML or CSV ?""")
	parser.add_argument("-d","--datafile",help="""You have to load a datafile""")
	parser.add_argument("-p","--byparty",action='store_true', help="""Do you want to split by political party ?""")
	parser.add_argument("-i","--info",action='store_true', help="""Information about the file""")
	return parser.parse_args()
	pass


def main():
	args = parse_argument()
	try:
		datafile = args.datafile
		if datafile == None:
			raise Warning("You must indicate a datafile")

	except Warning as e:
		lg.warning(e)
	
	else:
		if args.extension == 'csv':
			c_an.launch_analysis(args.datafile, args.byparty, args.info)
		elif args.extension == 'xml':
			x_an.launch_analysis(args.datafile, args.party, args.info)
	
	finally:
		lg.info("Analysis if over!!")

if __name__ == '__main__':
	main()

