import os 
import logging as lg

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns # Pimp my Matplotlib

lg.basicConfig(level=lg.DEBUG)


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
    	return "SetOfParliamentMembers total : {}".format(len(self.dataframe))

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
    	self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        #proportions = counts / nb_mps
        lg.debug("counts :{}".format(counts))

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                counts,
                labels=labels,
                autopct="%1.1f%%"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()


    def split_by_political_party(self):
		result = {}
		data = self.dataframe
			# These 2 syntaxes are equivalent: data.parti_ratt_financier and data['parti_ratt_financier']
	        all_parties = data["parti_ratt_financier"].dropna().unique()
	        for party in all_parties:
	        	data_subset = data[data.parti_ratt_financier == party]
	        	subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
	        	subset.data_from_dataframe(data_subset)
	        	result[party] = subset

	        	return result


def launch_analysis(data_file, by_party = False, info = False):
	sopm = SetOfParliamentMembers("All MPs")
	sopm.data_from_csv(os.path.join("data",data_file))
	#sopm.display_chart()

	if by_party:
		for party, s in sopm.split_by_political_party().items():
			lg.debug("by party")
			s.display_chart() 

	elif info:
		print(sopm)

	else:
		sopm.display_chart()
	
    

if __name__ == '__main__':
	launch_analysis(data_file)