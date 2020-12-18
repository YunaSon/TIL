import numpy as np
import wave, math

pentatonic_scale = {"C4":261.6, 
                    "flat E": 311.1,
                    "F": 349.2,
                    "G": 392.0,
                    "flat B": 466.2}


#CD의 샘플 레이트 44.1kHz (음질과 상관 있다)
sRate = 44100 

#10초 짜리 오디오 생성.
nSamples = sRate * 3 

# i/R ([샘플]/rate)
x = np.arange(nSamples)/float(sRate) 

# 각 음계의 주파수 별로 정현파 만들어 보기. 
# A=sin(2pift), A:진폭, f:주파수, t:시간
Val = {}
for i, j in pentatonic_scale.items():
    Val[i] = np.sin(2.0*math.pi*j*x) 

#16비트로 바꾸고 파일에 기록될 수 있도록 문자열로 형변환해준다.
datas = {}
for i,j in Val.items():
    datas[i] = np.array(j*32767, 'int16').tostring()


#wave파일로 저장
for i,j in datas.items():
    name = '{}_basic.wav'.format(i)
    files = wave.open(name, 'wb') 
    files.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed')) 
    files.writeframes(j)
    files.close()
#wave파일 생성에 필요한 매개변수 설정: 단일채널(모노), 2바이트(16비트), 비압축 포맷으로 설정


import matplotlib.pyplot as plt

Figure = plt.figure()
plt.ylabel("amplitude")
plt.xlabel("sample index")
plt.xlim(0,500)
plt.title("Waveforms")

plt.plot(Val["C4"], label='C4, 261.6')
plt.plot(Val["flat E"], label='flat E, 311.1')
plt.plot(Val["F"], label='F, 349.2')
plt.plot(Val["G"], label='G, 392.0')
plt.plot(Val["flat B"], label='flat B, 466.2')
plt.legend()
plt.grid()
#plt.show()





from collections import deque
import random

freq = 392
nSamples = 44100
sampleRate = 44100
N = int(sampleRate/freq)
    # initialize ring buffer
buf = deque([random.random() - 0.5 for i in range(N)])
    # plot of flag set 
samples = np.array(n*)
sample = np.array([0]*nSamples, 'float32')
print(sample)