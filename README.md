# FingerVein-Spoofing

## Flow
**1. 지정맥 영상 촬영**\
    - 총 20명의 피험자\
    - 피험자 당 4개의 손가락을 촬영\
    - 동영상 기기는 30 sampling rate를 가짐\
**2. 영상에서 frame 받아오기**\
**3. 받아온 frame의 평균픽셀값을 저장.**\
**4. frame들의 평균 픽셀값은 시계열 신호, 이를 주파수로 변환**\
**5. 피클파일로 저장하기.**\
**6. 모델링**\
**7. 모델 학습 및 평가**

- 시계열 신호 예시\
![image](https://user-images.githubusercontent.com/70633080/112020894-1897c980-8b74-11eb-9caa-618bc2f4c2eb.png)\
![-np.mean](https://user-images.githubusercontent.com/70633080/112023476-a1b00000-8b76-11eb-91d4-af991d20e258.png)

- 주파수 변환 예
