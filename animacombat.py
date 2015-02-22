import random
counter = range(0, 151, 5)

def atMake(number):
	foo = []
	for i in range(0, number+2):
		foo.append(0)
		
	foo.extend(sta(len(foo)))
		
	return foo

def sta(length):
	limit = 410 - (length * 10) + 1
	return range(10, limit, 10)

at0 = [0, 0, 0, 10, 30, 50]
at0.extend(range(60, 401, 10))
at1 = [0, 0, 0, 10, 20, 40]
at1.extend(range(50, 391, 10))

at2 = atMake(2)
at3 = atMake(3)
at4 = atMake(4)
at5 = atMake(5)
at6 = atMake(6)
at7 = atMake(7)
at8 = atMake(8)
at9 = atMake(9)
at10 = atMake(10)

def finalAtk(attack):
	roll = random.randint(1, 100)
	return attack + roll

def finalDef(defence):
	roll = random.randint(1, 100)
	return defence + roll
	
def calc(attack, defence, atype, dmg):
	fA = finalAtk(attack)
	fD = finalDef(defence)
	result = fA - fD
	
	if (result < 0):
		print "Counterattack! Bonus of %d" % counter[result / 10]
	else:
		per = 0
		if atype == 0:
			per = at0[result / 10]
		elif atype == 1:
			per = at1[result / 10]
		elif atype == 2:
			per = at2[result / 10]
		elif atype == 3:
			per = at3[result / 10]
		elif atype == 4:
			per = at4[result / 10]
		elif atype == 5:
			per = at5[result / 10]
		elif atype == 6:
			per = at6[result / 10]
		elif atype == 7:
			per = at7[result / 10]
		elif atype == 8:
			per = at8[result / 10]
		elif atype == 9:
			per = at9[result / 10]
		elif atype == 10:
			per = at10[result / 10]
			
		#print "Damage: %d; Fraction: %d" % (dmg, per / 100.0)
		dam = dmg * (per / 100.0)
		
		if dam == 0:
			print "Swing and a miss! No damage!"
		else:
			print "Hit! %d%% of total damage! Damage is %d!" % (per, dam)
