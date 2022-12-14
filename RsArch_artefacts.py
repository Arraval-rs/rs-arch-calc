#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the materials tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

armadyl_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Armadylean"])):
	armadyl_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Armadylean"][i]["name"]+" (damaged).png"), (31, 31), True))

bandos_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Bandosian"])):
	bandos_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Bandosian"][i]["name"]+" (damaged).png"), (31, 31), True))

dragonkin_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Dragonkin"])):
	dragonkin_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Dragonkin"][i]["name"]+" (damaged).png"), (31, 31), True))

saradomin_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Saradominist"])):
	saradomin_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Saradominist"][i]["name"]+" (damaged).png"), (31, 31), True))

zamorak_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Zamorakian"])):
	zamorak_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Zamorakian"][i]["name"]+" (damaged).png"), (31, 31), True))

zaros_images = []
for i in range(len(RsA_f.arch_dict["Artefacts"]["Zarosian"])):
	zaros_images.append(RsA_f.generate_img("images/artefacts/{}".format(RsA_f.arch_dict["Artefacts"]["Zarosian"][i]["name"]+" (damaged).png"), (31, 31), True))

armadyl_frame = [[sg.Image(armadyl_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Armadylean"][j]["name"]) for j in range(i, i + len(armadyl_images[i:i+6]))] for i in range(0, len(armadyl_images), 6)]
bandos_frame = [[sg.Image(bandos_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Bandosian"][j]["name"]) for j in range(i, i + len(bandos_images[i:i+6]))] for i in range(0, len(bandos_images), 6)]
dragonkin_frame = [[sg.Image(dragonkin_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Dragonkin"][j]["name"]) for j in range(i, i + len(dragonkin_images[i:i+6]))] for i in range(0, len(dragonkin_images), 6)]
saradomin_frame = [[sg.Image(saradomin_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Saradominist"][j]["name"]) for j in range(i, i + len(saradomin_images[i:i+6]))] for i in range(0, len(saradomin_images), 6)]
zamorak_frame = [[sg.Image(zamorak_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Zamorakian"][j]["name"]) for j in range(i, i + len(zamorak_images[i:i+6]))] for i in range(0, len(zamorak_images), 6)]
zaros_frame = [[sg.Image(zaros_images[j], tooltip = RsA_f.arch_dict["Artefacts"]["Zarosian"][j]["name"]) for j in range(i, i + len(zaros_images[i:i+6]))] for i in range(0, len(zaros_images), 6)]

artefacts_tab = [[
					sg.Column(
						[[sg.Frame("Armadylean", armadyl_frame)],
						[sg.Frame("Bandosian", bandos_frame)],
						[sg.Frame("Dragonkin", dragonkin_frame)],
						[sg.Frame("Saradominist", saradomin_frame)],
						[sg.Frame("Zamorakian", zamorak_frame)],
						[sg.Frame("Zarosian", zaros_frame)]
						], element_justification = "center", size = (300,300), scrollable = True, vertical_scroll_only = True)
				]]