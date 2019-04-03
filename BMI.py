while True:
	gender = input('請輸入性別: ')
	if gender == '男' or gender == '女':
		weight = float (input ('輸入您的體重(公斤) '))
		height = float (input ('請輸入您的身高(公分): '))
		BMI = int (weight / (height/100 * height/100))
		print ('Your BMI: ', BMI)
		break
	else:
		print('請輸入男或是女')