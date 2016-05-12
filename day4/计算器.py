import re
def formatEquation(string):
	string = string.replace("--", "+")
	string = string.replace("-+", "-")
	string = string.replace("++", "+")
	string = string.replace("+-", "-")
	string = string.replace("*+", "*")
	string = string.replace("/+", "/")
	string = string.replace(' ', '')
	return string
def findErrorChar(equation):
	'''
	查找非计算的字符
	'''
	re_rule = r"[^ \.\d\+\-\*\/\(\)]+"
	req = re.findall(re_rule,equation)
	return req
def findErrorOperator(equation):
	'''
	查找连续多次出现的运算符号
	'''
	re_rule = r'[+\-/*][+\-/*][+\-/*]*'
	req = re.findall(re_rule,equation)
	while '**' in req:
		req.remove('**')	
	return req
def addSubtract(equation):
	'''
	加减法运算，递归运算
	'''
	re_rule = r'[-]?\d+\.?\d*[+-]\d+\.?\d*'
	if re.search(re_rule,equation):
		req = re.search(re_rule,equation).group()
		if '+' in req:
			x,y = req.split('+')
			string = str(float(x) + float(y)) 
			equation = formatEquation(equation.replace(req,string))
			return addSubtract(equation)
		if '-' in req:
			if req.startswith('-'):
				req1 = req[1:]
				x,y = req1.split('-')
				x = '-'+x
			else:
				x,y = req.split('-')
			string = str(float(x) - float(y)) 
			equation = formatEquation(equation.replace(req,string))
			return addSubtract(equation)
	else:
		return equation

def multiplicationDivision(equation):
	'''
	乘除法及幂运算，递归运算
	'''
	re_rule = r'\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
	print(11)
	if re.search(re_rule,equation):
		req = re.search(re_rule,equation).group()
		print(req)
		if '**' in req:
			x,y = req.split('**')
			string = str(float(x) ** float(y)) 
			equation = formatEquation(equation.replace(req,string))
			return multiplicationDivision(equation)
		if '*' in req:
			x,y = req.split('*')
			string = str(float(x) * float(y)) 
			equation = formatEquation(equation.replace(req,string))
			return multiplicationDivision(equation)
		if '/' in req:
			x,y = req.split('/')
			string = str(float(x) / float(y)) 
			equation = formatEquation(equation.replace(req,string))
			return multiplicationDivision(equation)
	else:
		return equation
def removeBrackets(equation):
	'''
	计算算式中括号里的公式，直到所有括号的计算已完成
	'''
	re_rule =  r'\([^()]*\)'
	equation = formatEquation(equation)
	if re.search(re_rule,equation):
		req = re.search(re_rule,equation).group()
		string = addSubtract(multiplicationDivision(req[1:-1]))
		equation = equation.replace(req,string)
		return removeBrackets(equation)
	else:
		return equation
if __name__ == '__main__':
	while 1:
		#equation = input("请输入需要计算的公式")
		equation = "1 - 2 *  ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
		equation = equation.replace(' ','')
		#判断字符是否合法
		if findErrorChar(equation) :
			errorChar = findErrorChar(equation)
			print("下列字符不合法：",''.join(errorChar))
		elif findErrorOperator(equation):
			errorOperator = findErrorOperator(equation)
			print("下列字符不合法：",''.join(errorOperator))
		else:
			#格式化算式
			formatEquation(equation)
			print("输入的公式为：",equation)
			#去除括号
			equation = removeBrackets(equation)
			#计算结果
			equation = addSubtract(multiplicationDivision(equation))
			print('程序计算结果为：',equation)
			print('eval计算结果为：',eval(equation))
			break



