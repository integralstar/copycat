# copycat

OpenGPT2를 이용하여 학습한 모델을 바탕으로 기업의 마케팅 문구를 생성해 준다.

#### 평가
1. 모든 카테고리를 합쳐서 훈련시켰기 때문에 생성되는 문구가 자연스럽지 않음
2. 카피 라이팅 문구에서 브랜드와 광고 모델(연애인들) 이름을 삭제 해 줘야 함
3. 미세조정 전 후를 비교하여 보면 생성되는 문구에 확실한 차이가 발생함
4. 자연스러운 문장 생성을 위한 연구 필요
5. 나중에 기회가 되면 GPT-3에서 파인튜닝 후 결과 비교

#### finetunning 전

'호텔신라가 호텔신라의 지분을 인수하기로 한 것은 이번이 처음이다.'

'호텔 테라스가 내려다 보이는 길을 따라 길게 줄을 서 기다리면 된다.'

#### finetunning 후

'호텔침실만 보면 “여기가 우리집이었음..”하는 부부에 맞춰 롯데마트가 맞춤 세탁을 시작합니다. 오늘의 옥션이었습니다.'

'호텔침대에서 혼자 셀카를 찍다 깜빡했을지도 모를 일이다. 내 모바일에 이런 포샵이 있나? ... 좀 보여주까?'
