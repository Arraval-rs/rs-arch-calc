#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the materials tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Create the artefact layout given a faction
def create_artefact_frame(faction):
	frame = [[]]
	for i in range(0, len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts", faction])), 5):
		frame.append([])
		frame.append([])
		for j in range(0, min(5, len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts",faction])[i:i+5]))):
			frame[int(2*i/5)].append(sg.Image(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts",faction,i+j,"name"])+" (damaged).png"), (31, 31), True)))
			frame[int(2*i/5+1)].append(sg.Input(default_text = "0", enable_events = True, justification = "right", size = (4, 1))) # key = "{}Artefacts_{}".format(i+j)
	return frame
	
# Creating layouts for each faction's artefacts
armadyl_frame = create_artefact_frame("Armadylean")
bandos_frame = create_artefact_frame("Bandosian")
dragonkin_frame = create_artefact_frame("Dragonkin")
saradomin_frame = create_artefact_frame("Saradominist")
zamorak_frame = create_artefact_frame("Zamorakian")
zaros_frame = create_artefact_frame("Zarosian")

artefacts_tab = [[
					sg.Column(
						[
							[sg.Frame("Armadylean", armadyl_frame)],
							[sg.Frame("Bandosian", bandos_frame)],
							[sg.Frame("Dragonkin", dragonkin_frame)],
							[sg.Frame("Saradominist", saradomin_frame)],
							[sg.Frame("Zamorakian", zamorak_frame)],
							[sg.Frame("Zarosian", zaros_frame)]
						], element_justification = "center", size = (300,300), scrollable = True, vertical_scroll_only = True)
				]]

# function for artefact events
def artefact_events(window, event):
	return	