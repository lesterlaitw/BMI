height = input('請輸入身高(單位cm):' )
height = float( height )
weight = input('請輸入體重(單位kg):' )
weight = float( weight )
height2 = height / 100
bmi = weight / ( height2 * height2 )
print('您的BMI值為:' , bmi )
if bmi < 18.5:
	print('BMI＜18.5，體重過輕' )
elif bmi >=18.5 and bmi < 24:
	print('18.5≦BMI＜24，正常範圍' )
elif bmi >=24 and bmi < 27:
	print('24≦BMI＜27，過重' )
elif bmi >=27 and bmi < 30:
	print('27≦BMI＜30，輕度肥胖' )
elif bmi >=30 and bmi < 35:
	print('30≦BMI＜35，中度肥胖' )
else:
	print('BMI＞35，重度肥胖' )

#while True:
#	mode = input('請輸入模式: ')
#	if mode == 'q':
#		break
#	elif mode = '1':
#		print('啟動模式一')
#	elif mode = '2':
#		print('啟動模式二')
#	else:
#		print('只能輸入1/2/q')