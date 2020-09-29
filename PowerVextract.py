from zipfile import ZipFile
import os
from moviepy.editor import *

POWERLIST= []


def sort(path):
	for file in os.listdir(path):
		if file[6] == '.':
			new_file = file[:5]+'0'+file[5:]
			os.rename(path+'\\'+file,path+'\\'+new_file)




for file in os.listdir():          #convert All files to zip
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
				zipObj.extract(content,f'{power}-voice')

	segments_path= os.path.join(f'{power}-voice','ppt','media')
	voice_name = power.replace('.zip','.mp3')
	segments = []
	sort(segments_path)
	for segment in os.listdir(segments_path) :
		if segment.endswith('.wma'):
			segments.append(AudioFileClip(os.path.join(segments_path ,segment)))
	audioClips = concatenate_audioclips([segment for segment in segments])
	audioClips.write_audiofile(voice_name)
	os.rmdir(f'{power}-voice')
	os.rename(power ,power.replace('.zip', '.pptx'))
