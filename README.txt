knn dir:
	'_test' muszy byc katalogi z monetami testowymi,
		ktorych nie bierzemy do knn['_train']

	'_train' tam sa foldery z monetami z ktorych buduje sie knn

	'_test/labelgen.py' tworzy plik 'test.pickle',
		ktory nalezy wgrac do '_train'[potrzebny do 'acc.py']

	'_train/picklegen.py' tworzy 5 plikow '*.pickle'
		[potrzebne do 'acc'.py' i 'pred.py']

	'_train/pred.py' nie istotny

	'_train/acc.py' najwazniejsze, liczy dokladnosc

	'_train/imglib.py' znajduje sie tam funkcja 'imgfun',
		ktora tworzy vektor dla kazdego osobnika,
		[najwazniejsza funckja w knn]
		(jest zaznaczona w 'imglib.py':
			'>>>' 
			'imgfun()'
			'<<<'	)
imggen dir:
	muszy byc katalogi z monetami 
	tworzy w nich nowy katalog z nowymi monetami 
	


		***!foldery monet w 'knn/_train' i 'knn/_test' i 'imggen' musza miec te same nazwy!***