import sys
import pickle
# def do_work1(positive, negative):
# 	text = len(positive) + len(negative)
# 	with open('checking.pickle', 'wb') as f:
# 		pickle.dump(text,f)

def do_work2():
	text = '123'
	with open('checking2.pickle', 'wb') as f:
		pickle.dump(text,f)


do_work2()
