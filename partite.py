#! /usr/bin/env python3
# coding: utf-8

import argparse

import analysis.csv as c_an
import analysis.xml as x_an 


def parse_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e","--extension",help="""XML or CSV ?""")
	return parser.parse_args()
	pass


def main():
	args = parse_argument()
	if args.extension == 'csv':
		c_an.launch_analysis("current_mps.csv")
	elif args.extension == 'xml':
		x_an.launch_analysis("syseronBrut.xml")
	

if __name__ == '__main__':
	main()

