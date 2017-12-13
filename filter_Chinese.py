import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-file', default='', type=str)
opt = parser.parse_args()


f = open(opt.file)
fout = open('filtered_'+ opt.file,'w')










for s in f:
	if len(s) >2 :
	    new_s = ''.join(list(filter(lambda c: '\u4e00' <= c <= '\u9fa5' or c in '，。？：',s))) #filter Chinese characters
	    if len(new_s) > 0:
	        fout.write(' '.join(new_s)+'\n')    

f.close()
fout.close()