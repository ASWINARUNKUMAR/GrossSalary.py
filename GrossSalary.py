while(1):
	grade = input("enter the grade: ")

	if grade in ("A", "B", "C"):
		break
	else:
		print("enter valid grade")

basic = {'A': 10000, 'B': 4567, 'C': 3000}
allowance = {'A': 1700, 'B': 1500, 'C': 1300}

bsalary = basic[grade]
allow = allowance[grade]

hra = (bsalary*20)/100
da = (bsalary*50)/100
pf = (bsalary*11)/100

gross = bsalary + hra + da + allow - pf

print("the gross salary is: ", gross)
