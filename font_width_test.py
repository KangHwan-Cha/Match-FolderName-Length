import tkinter as tk
from tkinter import font

# Create a dummy tkinter window
root = tk.Tk()

# Create a font object for measuring
font_obj = font.Font(family="맑은 고딕", size=12)  # Replace with your desired font and size

# Measure the width of a string
width = font_obj.measure("abc한글123!!!")
print(f"Width: {width}")

width = font_obj.measure("abc한글123!!!abc한글123!!!")
print(f"Width: {width}")

width = font_obj.measure("a")
print(f"a: {width}")

width = font_obj.measure("1")
print(f"1: {width}")

width = font_obj.measure("ㅇ")
print(f"ㅇ: {width}")

width = font_obj.measure("가")
print(f"가: {width}")

width = font_obj.measure("^")
print(f"^: {width}")

width = font_obj.measure("○")
print(f"○(특): {width}")

width = font_obj.measure("_")
print(f"_(특): {width}")
# Destroy the tkinter window
root.destroy()