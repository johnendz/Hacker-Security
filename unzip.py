import zipfile
import os

filename = 'file.zip'
count = 0

while count < 900:
	zip = zipfile.ZipFile(filename)
	lst = zip.namelist()
	for file in lst:
		proxextract = file
		password = file.split('.', 1)[0]
	zip.extract(proxextract, pwd=password)
	if filename.endswith('.zip'):
		os.remove(filename)
	filename = proxextract
	print 'Quantidade de arquivos extraidos:', count
	count = count + 1