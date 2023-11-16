import os
import time
import sys
from tkinter import filedialog
import tkinter as tk
from tkinter import font


def match_length(param: str, length: int) -> str:
	if length == 0:
		return param
	elif param.find("__") == -1:
		return param

	rep_int = int(((length - font_width(param)) / 7))

	if rep_int <= 0:
		return param

	inst = "_" * rep_int
	param = param[:param.find("__")] + inst + param[param.find("__"):]
	return param


def font_width(strings: str) -> int:
	"""글꼴(맑은고딕)의 문자 하나의 너비를 리턴

	Args:
		s (str): 문자 하나

	Returns:
		int: width a:8 / 1:9 / 한:16
	"""

	str_list = list(strings)
	# Create a dummy tkinter window
	root = tk.Tk()

	# Create a font object for measuring
	font_obj = font.Font(family="맑은 고딕", size=12)  # Replace with your desired font and size

	width = 0
	# Measure the width of a string
	for s in str_list:
		width += font_obj.measure(s)

	# Destroy the tkinter window
	root.destroy()

	return width


def main():
	# 루트 폴더 선택
	root_path = filedialog.askdirectory()
	# 선택된 폴더가 없으면 종료
	if root_path == '':
		print('선택된 폴더가 없으므로 종료합니다.')
		time.sleep(3)
		sys.exit()
	print(root_path)

	# 폴더만 리스트에 저장 후 length_MAX 계산
	folders_list = []
	length_MAX = 0
	for i in os.listdir(root_path):  # i: folder name or file name
		full_path = os.path.join(root_path, i)
		if os.path.isdir(full_path):
			folders_list.append(i)
			i_len = font_width(i)
			if length_MAX <= i_len:
				length_MAX = i_len

	print(length_MAX)
	for f in folders_list:
		src = f
		des = match_length(f, length_MAX)
		os.rename(os.path.join(root_path, src), os.path.join(root_path, des))
		print(des)

if __name__ == '__main__':
	main()

