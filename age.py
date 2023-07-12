#判斷使用者是否開過車，以及詢問年齡，
#如果年齡符合，顯示通過，不符合的話顯示為何開過車

driving = input('是否有開過車: ')
if driving != '有' and driving != '沒有':
	print('只能輸入有or沒有')
	raise SystemExit

age = input('請輸入年齡: ')
age = int(age)

if driving == '有':
	if age >= 18:
		print('考到駕照了')
	elif age < 18:
		print('這樣是無照駕駛')
elif driving == '沒有':
	if age >= 18:
		print('怎麼不去考駕照')
	elif age < 18:
		print('再過幾年就可以去考了')						
