from zipfile import ZipFile
import os
POWERLIST= []

for file in os.listdir():
	if file.endswith('.ppt'):
		file=file.replace('.ppt','')
		os.rename(file+'.ppt',file+'.zip')
		POWERLIST.append(file+'.zip')
	if file.endswith('.pptx'):
		file=file.replace('.pptx','')
		os.rename(file+'.pptx',file+'.zip')
		POWERLIST.append(file+'.zip')
for file in os.listdir():
	if file.endswith('.zip'):
		POWERLIST.append(file)

for power in POWERLIST:
	with ZipFile(power,'r') as zipObj:
		for content in zipObj.namelist():
			if content.endswith('.wma'):
				zipObj.extract(content,'voice')

	segments_path= os.path.join('voice','ppt','media')
	voice_path = os.path.join('voice',power.replace('.zip','.mp3'))
	with open(voice_path,'wb') as voice:
		datas=bytes()
		for segment in os.listdir(segments_path):
			data = open(f'{segments_path}//{segment}','rb')
			datas= datas + data.read()
			print(data==datas)
		voice.write(datas)
	voice.close()

		
