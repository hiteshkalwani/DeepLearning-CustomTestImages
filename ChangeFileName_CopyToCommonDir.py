import os
import shutil
from shutil import copyfile
import csv
i=1
with open('imageList.csv', 'wb') as csvfile:
	fieldnames = ['image', 'output']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()		
    	for foldername in os.listdir('.'):
		if (foldername!='ChangeFileName_CopyToCommonDir.py' and foldername!='ChangeFileName_CopyToCommonDir.py~' and foldername!='imageList.csv' and foldername!='CustomTestImages'):
			for subfoldername in os.listdir('./'+foldername):			
				for filename in os.listdir('./'+foldername+'/'+subfoldername):
					print os.path.realpath(foldername)+'/'+subfoldername+'/'+filename
					filename = os.path.realpath(foldername)+'/'+subfoldername+'/'+filename
					filenamenew = os.path.realpath(foldername)+'/'+subfoldername+'/'+subfoldername+str(i)+'.jpg'
					print str(i)+ ' ' + filenamenew		
					os.rename(filename,filenamenew)
					shutil.copy2(filenamenew,'./CustomTestImages')
					if subfoldername=='green':
						output=2
					elif subfoldername=='red':			
						output=1
					else:
						output=0
					writer.writerow({'image': subfoldername+str(i)+'.jpg', 'output': output})
					i+=1

reader = csv.DictReader(open('imageList.csv', 'r'))
result = sorted(reader, key=lambda d: d['image'].split('.')[0])

writer = csv.DictWriter(open('sorted_imageList.csv', 'w'), reader.fieldnames)
writer.writeheader()
writer.writerows(result)
