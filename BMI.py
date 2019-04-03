while True:
	gender = input('請輸入性別: ')
	if gender == '男' or gender == '女':
		weight = float (input ('輸入您的體重(公斤) '))
		height = float (input ('請輸入您的身高(公分): '))
		waistline = float (input ('請輸入您的腰圍(公分): '))
		BMI = int (weight / (height/100 * height/100))
		print ('Your BMI: ', BMI)
		if gender == '男' and waistline >= 90 or gender == '女' and waistline >=80:
			print('腰圍過大')
		if BMI < 18.5:
			print('體重過輕')
		elif BMI >= 18.5 and BMI <24:
			print('體重正常')
		elif BMI >= 24 and BMI < 27:
				print('體重過重')
		elif BMI >= 27 and BMI < 30:
				print('輕度肥胖')
		elif BMI >= 30 and BMI < 35:
				print('中度肥胖')
		elif BMI >=35:
				print('重度肥胖')	
		break
	else:
		print('請輸入男或是女')