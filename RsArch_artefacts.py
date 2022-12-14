#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the materials tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Create the artefact layout given the list of images for a faction
def create_artefact_frame(images):
	frame = [[]]
	for i in range(0, len(images), 6):
		frame.append([])
		frame.append([])
		for j in range(0, min(6, len(images[i:i+6]))):
			frame[int(2*i/6)].append(sg.Image(images[i+j]))
			frame[int(2*i/6+1)].append(sg.Input(default_text = "0", enable_events = True, justification = "right", size = (4, 1))) # key = "{}Artefacts_{}".format(i+j)
	return frame

# Creating arrays of images
armadyl_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Armadylean"]))):
	armadyl_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Armadylean",i,"name"])+" (damaged).png"), (31, 31), True))

bandos_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Bandosian"]))):
	bandos_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Bandosian",i,"name"])+" (damaged).png"), (31, 31), True))

dragonkin_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Dragonkin"]))):
	dragonkin_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Dragonkin",i,"name"])+" (damaged).png"), (31, 31), True))

saradomin_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Saradominist"]))):
	saradomin_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Saradominist",i,"name"])+" (damaged).png"), (31, 31), True))

zamorak_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Zamorakian"]))):
	zamorak_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Zamorakian",i,"name"])+" (damaged).png"), (31, 31), True))

zaros_images = []
for i in range(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Zarosian"]))):
	zaros_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.read_value(RsA_f.arch_dict,["Artefacts","Zarosian",i,"name"])+" (damaged).png"), (31, 31), True))

# Creating layouts for each faction's artefacts
armadyl_frame = create_artefact_frame(armadyl_images)
bandos_frame = create_artefact_frame(bandos_images)
dragonkin_frame = create_artefact_frame(dragonkin_images)
saradomin_frame = create_artefact_frame(saradomin_images)
zamorak_frame = create_artefact_frame(zamorak_images)
zaros_frame = create_artefact_frame(zaros_images)

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