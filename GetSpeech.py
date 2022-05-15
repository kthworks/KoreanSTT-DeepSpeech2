#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr

# 함수 정의부
def get_speech():
    # 마이크에서 음성을 추출하는 객체
    recognizer = sr.Recognizer()

    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("소음 수치 반영하여 음성을 청취합니다. {}".format(recognizer.energy_threshold))

    # 음성 수집
    with microphone as source:
        print("목소리를 들을 준비가 되었습니다. 말씀해주세요 :)")
        result = recognizer.listen(source)
        audio = result.get_raw_data()
    
    return audio

