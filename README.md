# FingerVein-Spoofing

## Flow
1. 지정맥 영상 촬영
    - 총 20명의 피험자
    - 피험자 당 4개의 손가락을 촬영
    - 동영상 기기는 30 sampling rate 를 가짐
2. 영상에서 frame 받아오기
3. 받아온 frame의 평균픽셀값을 저장.
4. frame들의 평균 픽셀값은 시계열 신호, 이를 주파수로 변환
5. 피클파일로 저장하기.
6. 모델링
7. 모델 학습 및 평가
## Code
- [SVR]() : 기존연구 SVR을 사용하여 위조지정맥판별
- [DNN]() : 위조지정맥 판별 모델로 DNN사용
- [CNN]() : 위조지정맥 판별 모델로 CNN사용
- [Dataprocessing]() : data 전처리(frame 당 평균 픽셀값 추출 -> 주파수변환 -> 피클파일 저장)
## Data
- Real 지정맥 이미지 예시
- Fake 지정맥 이미지 예시
    - 손가락에 print된 지정맥 image를 감싼 후 
## Model
## Result
## 
