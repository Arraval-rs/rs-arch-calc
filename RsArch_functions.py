#####################################################
# RsArch_functions.py							   #
# Various functions used by the app				 #
# Also includes some variables used across the app  # 
#####################################################

import os
import io
import bisect
import json
from PIL import Image, ImageDraw

# array of XP required to level up skills
level_xp = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333, 111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431, 14391160, 15889109, 17542976, 19368992, 21385073, 23611006, 26068632, 28782069, 31777943, 35085654, 38737661, 42769801, 47221641, 52136869, 57563718, 63555443, 70170840, 77474828, 85539082, 94442737, 104273167]

# array of active collections
active_collections = []

# Dictionary for archaeology data
json_file = open("data/arch_data.json", "rt")
json_text = json_file.read()
arch_dict = json.loads(json_text)

# finds the user's current or target level based on input xp
def find_level(experience):
	return bisect.bisect(level_xp, experience)

# finds the user's current or target xp based on input level. Uses the minimum xp to attain that level
def find_experience(level):
	return level_xp[level - 1]

# generates an image with the given file and size. Optionally generates a background square
def generate_img(f, s, bg): # Generates image using PIL
	if "None" in f:
		f = 'images/Empty Slot.png'
	if not os.path.exists(f):
		print("WARN: Missing image {}".format(f))
		f = 'images/Missing.png'
	img = Image.open(f).resize(s)
	if bg:
		item_bg = Image.open('images/Empty Slot.png').resize(s)
		item_bg.paste(img, (0, 0), img.convert('RGBA'))
		img = item_bg
	img.thumbnail(s)
	bio = io.BytesIO()
	img.save(bio, format = "PNG")
	return bio.getvalue()

# 
def determine_collections(preference, level, target_level):
	return

# Determines which artefacts to build based on input parameters
def determine_artefacts(collections_only, ):
	if collections_only:
		return
	else:
		return

# function to save input values to JSON
def save_json_to_file():
	return