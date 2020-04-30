import os

with open('country_per_continent.csv', 'a') as dataset:
	dataset.write('N,country,continent\n')
	n = 1
	for name in os.listdir('.'):
		if name != 'makedataset.py':
			with open(name, 'r') as file:
				country = file.readline()
				while country:
					dataset.write(str(n)+','+country[:-1]+','+name.split('.')[0]+'\n')
					country = file.readline()
					n += 1

print('dataset is make')