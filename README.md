# KoreanSTT-DeepSpeech2

---

## 1. Introduction

본 프로젝트는 실시간 한국어 음성 인식기능을 제공합니다.  

Speech to Text (STT)와 관련한 모든 전처리, 모델, 학습 등은 [sooftware](https://github.com/sooftware)님께서 공유해주신 [Kospeech](https://github.com/sooftware/kospeech) 오픈소스를 사용했습니다.

본 프로젝트는 Kospeech를 기반으로 한 pre-trained 모델을 제공하며, 실시간으로 마이크를 통해 음성 데이터를 받아들이고 해당 음성에 대한 인식 결과를 텍스트로 제공합니다.

다른 데이터셋과 다른 모델을 이용하여 직접 모델을 학습시켜보고 싶으신 분들께서는 [sooftware님의 Kospeech 오픈소스 링크](https://github.com/sooftware/kospeech)에서 더욱 자세한 정보를 얻으실 수 있습니다 :)

## 2. Pre-trained Model

**Model**: DeepSpeech2  
**Dataset**: KsponSpeech  

**Training**  
GPU : RTX 3080ti  
CPU : intel i9-12900k  
Time cost : About 6.5 hours per an Epoch (Total 13 Epoch)  

**Performance**  
CER : 0.2536  

## 3. How to use?

### Prerequisites
Numpy: ```pip install numpy```  
Torch: You can install from [here](https://pytorch.org/get-started/locally/) to suit your environment.    
Torchaudio: ```pip install torchaudio```  
Matplotlib: ```pip install matplotlib```  
Librosa: ```conda install -c conda-forge librosa```  
Speech_recognition: ```conda install -c conda-forge speechrecognition```  
pyaudio: ```conda install -c conda-forge PyAudio```

이곳에 기재되지 않은 라이브러리 이외에 추가적으로 라이브러리가 필요하다는 경고문이 보인다면 해당 라이브러리를 추가로 설치해주시기 바랍니다.

p.s. 본 프로젝트를 위한 별도의 가상환경을 생성하신 후에 위의 라이브러리들을 설치하시길 권장드립니다.

### Inference with pretrained Model
1. Code > Download Zip 를 통해 본 프로젝트를 다운받아주시기 바랍니다.

2. 가상환경에서 본 프로젝트가 다운로드 된 경로로 이동해주세요.

* Command
```
$ python ./main.py
```

* Output
```
소음 수치 반영하여 음성을 청취합니다. 58.945561915793384
목소리를 들을 준비가 되었습니다. 말씀해주세요 :)
```  
위 문장이 보이면 마이크를 통해 말씀해주시면 됩니다.
음성이 수집된 이후 곧바로 인식된 결과가 제공됩니다.
```
음성인식 결과가 제공됩니다.
```

* Jupyter notebook 사용시

jupyter notebook을 통해 main.ipynb 파일을 실행하시면 입력된 음성 그래프 및 다시듣기 기능도 함께 제공됩니다.

## 4. Troubleshoots and Contributing

본 프로젝트와 관련한 이슈나 문의 사항이 있다면 아래를 통해 연락주시면 감사하겠습니다.

Author: Taehyoung Kim @kthworks  
Author e-mail: kthwork9934@gmail.com
