# FingerVein-Spoofing

## Pickle file
- list나 class 같은 text가 아닌 자료형데이터는 일반적인 파일입출력 방법으로는 데이터를 불러올 수 없다.
- python에서는 이와 같은 자료형의 데이터를 파일로 저장하기 위해 pickle모듈을 사용한다.

- ```import pickle``` 로 모듈임포트가 필요함
- 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드할수있다.
  - (open('text.txt','w')방식으로 데이터를 입력하면 string자료형으로 저장된다.)
- pickle로 데이터를 저장하거나 불러올때는 파일을 BYTE형식으로 읽거나 써야한다.(wb,rb)
- wb로 데이터를 입력하는 경우 .bin확장자를 사용하는 것이 좋다.
- 모든 파이썬데이터객체를 저장하고 읽을 수 있다.
### 입력
- ```pickle.dump(data,file)```
```
import pickle
list = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
  pickle.dump(list, f)
```
### LOAD
- val=pickle.load(file)
- 한줄씩 파일을 읽어오며 더이상 로드할 데이터가 없으면 EOFError가 발생
```
with open('list.txt', 'rb') as f:
  data = pickle.load(f) # 단 한줄씩 읽어옴

data
#['a', 'b', 'c']
```
- pickle.load(file)을 통해 파일을 읽기위해서는 pickle.dump로 입력된 파일이어야 한다.
