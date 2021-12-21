def plot_spec(data,sr,title, fpath):
  '''
  Function for plotting spectrogram along with amplitude wave graph
  '''
  label = str(fpath).split('/')[-1].split('_')[0]
  fig, ax = plt.subplots(1,2,figsize=(15,5))
  ax[0].title.set_text(f'{title} / Label: {label}')
  ax[0].specgram(data,Fs=2)
  ax[1].set_ylabel('Amplitude')
  ax[1].plot(np.linspace(0,1,len(data)), data)
  
#Reading the wav file:
file_path = data_path.ls()[3]
wav, sr = librosa.load(file_path,sr=None)

#Plotting the spectrogram and wave graph
plot_spec(wav,sr,'Original wave file',file_path)
'''
Noise addition using normal distribution with mean = 0 and std =1
Permissible noise factor value = x > 0.004
'''
wav_n = wav + 0.009*np.random.normal(0,1,len(wav))
plot_spec(wav_n,sr,'Noise Added 0.005',file_path)
ipd.Audio(data=wav_n,rate=sr)

'''
Shifting the sound wave

Permissible factor values = sr/10
'''

wav_roll = np.roll(wav,int(sr/10))
plot_spec(data=wav_roll,sr=sr,title=f'Shfiting the wave by Times {sr/10}',fpath=file_path)
ipd.Audio(wav_roll,rate=sr)

#Time-stretching the wave
'''
Permissible factor values = 0 < x < 1.0
'''
factor = 0.4
wav_time_stch = librosa.effects.time_stretch(wav,factor)
plot_spec(data=wav_time_stch,sr=sr,title=f'Stretching the time by {factor}',fpath=file_path)
ipd.Audio(wav_time_stch,rate=sr)

#pitch shifting of wav
'''
Permissible factor values = -5 <= x <= 5
'''
wav_pitch_sf = librosa.effects.pitch_shift(wav,sr,n_steps=-5)
plot_spec(data=wav_pitch_sf,sr=sr,title=f'Pitch shifting by {-5} steps',fpath=file_path)
ipd.Audio(wav_pitch_sf,rate=sr)