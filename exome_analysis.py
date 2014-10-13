
import sys

if __name__ == "__main__":

	argvs = sys.argv

	f = open(argvs[1])
	text = f.read()
	f.close

        lines = text.split('\r')

        list_name = argvs[1].split('/')[-1]
	f1 = open('candidate_list_%s'%list_name, 'w')
	for line in lines:
		tmp = line.split('\t')
		#maf < 0.05
		try:
			if float(tmp[41]) < 0.05:
				#rs ?
				if int(tmp[23].find('rs')) == -1:
					f1.write(line)
		except:
			pass
        f1.close()

	
