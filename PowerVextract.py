import os
import zipfile
from pydub import AudioSegment
import re


class VoiceExtract:
	def __init__(self, file):
		self.file = file
		self.file_name = os.path.basename(self.file)
		self.file_name_no_ext = os.path.splitext(self.file_name)[0]
		self.file_ext = os.path.splitext(self.file_name)[1]
		self.file_path = os.path.dirname(self.file)
		self.supported_ext = ['.ppt', '.pptx', '.zip']
		self.audio_ext = ['.wav', '.mp3','aiff', '.aif', '.aifc', '.aiff', '.au', '.flac', '.m4a', '.mp4', '.m4b', '.m4p', '.mpc', '.oga', '.ogg', '.opus', '.ra', '.ram', '.wma', '.wv', '.webm']
		self.extract_zip()
		self.merge_audio()
		self.clear()
	
	def extract_zip(self):
		if self.file_ext in self.supported_ext:
			with zipfile.ZipFile(self.file, 'r') as zip_ref:
				zip_ref.extractall('output')
				zip_ref.close()
		else:
			raise Exception('File extension not supported')

	def sortaudiolist(self,audiolist):
		return sorted(audiolist, key=lambda x: int(re.sub('\D','',x)))

	def get_audio_files(self):
		audio_files = []
		for root, _, files in os.walk('output'):
			for file in files:
				if os.path.splitext(file)[1] in self.audio_ext:
					audio_files.append(os.path.join(root, file))
		return audio_files

	def merge_audio(self):
		audio_files = self.get_audio_files()
		audio_files = self.sortaudiolist(audio_files)
		if len(audio_files) > 1:
			print('Merging audio files')
			merged_audio = AudioSegment.from_file(audio_files[0])
			for audio_file in audio_files[1:]:
				merged_audio += AudioSegment.from_file(audio_file)
				merged_audio.export('test.mp3', format='mp3')
				merged_audio = AudioSegment.from_file('test.mp3')
		else:
			raise Exception('No audio files found')

	def clear(self):
		print('Cleaning up')
		os.rmdir('output')

if __name__ == '__main__':
	file = 'file.pptx'
	VoiceExtract(file)