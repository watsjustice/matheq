import sympy as sp
import numpy as np
import matplotlib.pyplot as mp
import os

class Math():

	derivative_x , derivative_y , newequation_x , newequation_y , flag = 0 , 0 ,str(), 0 ,False 
	x ,y= sp.symbols('x,y')


	def __init__(self , *kwargs):
		globals().update({item : object for item , object in zip(['value' + str(x) for x in range(100)] , kwargs)})
		self.theequation_x = value0
		try:
			self.theequation_y = value1
			Math.flag = True
		except:
			pass
		self.diff()

	def diff(self):
		Math.derivative_x = self.theequation_x.diff(Math.x)
		try:
			Math.derivative_x = Math.derivative_x / self.theequation_x.diff(Math.y)
		except:
			pass
		if Math.flag:
			Math.derivative_y = self.theequation_y.diff(Math.x)



	@property
	def xf(self):
		fig = mp.subplots()
		y = np.linspace(-10 , 10,1000)
		x = np.linspace(-10 , 10,1000)
		mp.plot(y , Math.newequation_x(x,y))

		if Math.flag:
			mp.plot(y , Math.newequation_y(y))
			
		mp.show()


	@xf.setter
	def xf(self , *kwargs):
		globals().update({item : object for item , object in zip(['val' + str(x) for x in range(10)] , kwargs)})
		Math.newequation_x = val0

		if Math.flag:
			Math.newequation_y = val1

	def __str__(self):
		if Math.flag:
			Math.flag = False

			return f'The derivative of the {self.theequation_x} and {self.theequation_y} is :' + '\n'*3 + f'{Math.derivative_x/Math.derivative_y}' + '\n'*3 
		return f'The derivative of the {self.theequation_x} is :' + '\n'*3 + f'{Math.derivative_x}' + '\n'*3

x,y = sp.symbols('x,y')
ss = Math(y*sp.sin(x)-sp.cos(x-y))
print(ss)


# ИНСТРУКЦИЯ ПО ПОСТРОЙКЕ ГРАФИКА.

# ЕСЛИ В ПРОИВЗОДНОЙ ОТСУТСТВУЮТ SIN , COS , TAN , CTG , ASIN (ARCSINUS) , ACOS (ARCCOS) , ТО
# ПРОСТО КОПИРУЕМ ПОЯВИВШИЕСЯ В КОНСОЛИ УРАВНЕНИЕ - ПРОИЗВОДНУЮ ВВЕДЕННОГО РАНЕЕ УРАВНЕНИЯ
# ВО ВСЕХ СЛУЧАЯХ БЕЗ ИСКЛЮЧЕНИЯ ТРЕБУЕТСЯ ЗАМЕНА SQRT НА ( ВЫРАЖЕНИЕ , КОТОРОЕ БЫЛО В МЕТОДЕ SQRT) ** 0.5

# В СЛУЧАЕ ЕСЛИ ЕСТЬ SIN , COS , TAN , CTG , ASIN (ARCSINUS) , ACOS (ARCCOS) , ТО
# ПЕРЕД ТРИГОНОМЕТРИЧЕСКИМ МЕТОДОВ СТАВИМ NP.
# ПРИМЕР : SIN(X) ДОЛЖНО БЫТЬ ПЕРЕПИСАНО В NP.SIN(X)
#



ss.xf = lambda x,y: (y*np.cos(x) + np.sin(x - y))/(np.sin(x) - np.sin(x - y))   #ПОЛЕ ДЛЯ ВВОДА УРАВНЕНИЯ ДЛЯ ПОСТРОЙКИ ГРАФИКА
ss.xf


