
import sys

def check_known_genes(known_genes, ad_file):
	known_snps = []
	for line in ad_file:
		tmp  = line.split('\t')
		print tmp[10]
		if tmp[10] in known_genes == True:
			print 'Found %s in VCF'%tmp[10]
			if int(tmp[23].find('rs')) == -1:
                        	known_snps.append(line)


	return known_snps

if __name__ == "__main__":

	argvs = sys.argv
	#[1]=AR file
	#[2]=AD file
	#[3]=Known Genes

        #AR_file for one patient
	f_ar = open(argvs[1])
	text_ar = f_ar.read()
	f_ar.close

        lines_ar = text_ar.split('\r')

        #AD_file for one patient
	f_ad = open(argvs[2])
	text_ad = f_ad.read()
	f_ad.close

        #Export file
        list_name = argvs[1].split('/')[-1]
	f1 = open('build/candidate_list_%s'%list_name, 'w')
        f1.write(lines_ar[2])
        f1.write('\n')


	for line in lines_ar:
		tmp = line.split('\t')
		#maf < 0.05
		try:
			if float(tmp[41]) < 0.05:
				#rs ?
				if int(tmp[23].find('rs')) == -1:
					f1.write(line)
		except:
			pass

	#Known Genes
	f_known=open(argvs[3])
	text_known=f_known.read()
        f_known.close()

	known_genes=text_known.strip('\n').split(',')
	print known_genes
	known_snps = check_known_genes(known_genes, lines_ad)
        f1.write('known genes \n')
	for k_snp in known_snps:
        	f1.write(k_snp)
	
        f1.close()
