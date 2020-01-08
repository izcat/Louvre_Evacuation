import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import time
import random

from map import myMap
from people import People

class GUI:
	# GUI
	# 图像比例
	Pic_Ratio = 10
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("疏散模拟")
		self.root.geometry("1000x715")
		self.root.resizable(width=False, height=False)

		width = myMap.Length * GUI.Pic_Ratio
		height = myMap.Width * GUI.Pic_Ratio
		self.canvas = tk.Canvas(self.root, width=width, height=height, bg="grey")
		self.canvas.pack()

		self.label_time = tk.Label(self.root, text="Time = 0.00s", font='Arial -37 bold')
		self.label_evac = tk.Label(self.root, text="Evacution People: 0", font='Arial -37 bold')
		self.label_time.pack()
		self.label_evac.pack()

		self.setBarrier()
		self.setExit()

	
	# 障碍
	def setBarrier(self):
		for (A, B) in myMap.Barrier:
			x1, y1, x2, y2 = A[0], A[1], B[0], B[1]
			[x1, y1, x2, y2] = map(lambda x:x*GUI.Pic_Ratio, [x1, y1, x2, y2])
			self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")
	
	# 出口
	def setExit(self):
		for (x, y) in myMap.Exit:
			sx, sy = x-1, y-1
			ex, ey = x+1, y+1
			[sx, sy, ex, ey] = map(lambda x:x*GUI.Pic_Ratio, [sx, sy, ex, ey])
			self.canvas.create_rectangle(sx, sy, ex, ey, fill="green", outline="green")


	def Update_People(self, People_List):
		for p in People_List:
			# print(p.id)
			self.canvas.delete(p.name())

		self.Show_People(People_List)

	def Show_People(self, People_List):
		for p in People_List:
			if p.savety:
				continue
			ox, oy = p.pos[0], p.pos[1]
			x1, y1 = ox-0.2, oy-0.2
			x2, y2 = ox+0.2, oy+0.2
			[x1, y1, x2, y2] = map(lambda x:x*GUI.Pic_Ratio, [x1, y1, x2, y2])
			self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black", tag=p.name())
			

def Cellular_Automata(Total_People):
	
	UI = GUI()

	# Total_People = 200
	P = People(Total_People, myMap)

	UI.Show_People(P.list)


	Time_Start = time.time()
	Eva_Number = 0
	while Eva_Number<Total_People:
		Eva_Number = P.run()

		UI.Update_People(P.list)	

		time.sleep(random.uniform(0.15, 0.25))

		UI.canvas.update()
		UI.root.update()

		Time_Pass = time.time()-Time_Start
		UI.label_time['text'] = "Time = "+ "%.2f" % Time_Pass + "s"
		UI.label_evac['text'] = "Evacution People: " + str(Eva_Number)
		# print("%.2fs" % (Time_Pass) + " 已疏散人数:" +str(Eva_Number))

	Time_Pass = time.time()-Time_Start
	UI.label_time['text'] = "Time = "+  "%.2f" % Time_Pass + "s"
	UI.label_evac['text'] = "Evacution People: " + str(Eva_Number)

	# 热力图
	sns.heatmap(P.thmap.T, cmap='Reds')
	plt.axis('equal')
	plt.show()


	UI.root.mainloop()

Cellular_Automata(Total_People=1000)

