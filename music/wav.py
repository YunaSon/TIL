# CD음질의 220Hz 정현파 wav파일 만들어 보기. 

import numpy as np
import wave, math

#CD의 샘플 레이트 44.1kHz (음질과 상관 있다)
sRate = 44100 

#10초 짜리 오디오 생성.
nSamples = sRate * 10 

# i/R ([샘플]/rate)
x = np.arange(nSamples)/float(sRate) 
print(x.shape)

# 220Hz의 정현파 만들어 보기. 
# A=sin(2pift), A:진폭, f:주파수, t:시간, 220Hz의 정현파 만들어 보기
vals = np.sin(2.0*math.pi*220.0*x) 

#16비트로 바꾸고 파일에 기록될 수 있도록 문자열로 형변환해준다.
data = np.array(vals*32767, 'int16').tostring()

#wave파일로 저장
files = wave.open('sine220.wav', 'wb') 

#wave파일 생성에 필요한 매개변수 설정: 단일채널(모노), 2바이트(16비트), 비압축 포맷으로 설정
files.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed')) 
files.writeframes(data)
files.close()

import matplotlib.pyplot as plt

plt.figure()
plt.plot(vals)
plt.ylabel("amplitude")
plt.xlabel("sample index")
plt.xlim(0,1000)
plt.title("Waveform of sine220Hz")
plt.show()