#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the materials tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Creating layouts for each faction's artefacts
armadyl_frame = RsA_f.create_item_frame("Armadylean", "Artefact")
bandos_frame = RsA_f.create_item_frame("Bandosian", "Artefact")
dragonkin_frame = RsA_f.create_item_frame("Dragonkin", "Artefact")
saradomin_frame = RsA_f.create_item_frame("Saradominist", "Artefact")
zamorak_frame = RsA_f.create_item_frame("Zamorakian", "Artefact")
zaros_frame = RsA_f.create_item_frame("Zarosian", "Artefact")

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