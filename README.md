# korean restaurants search program
음식점 검색 프로그램은 python django framework + elastics search를 활용하여 수행됩니다.   
또한, 한글 형태소 분석을 위해 nori 형태소 분석기를 사용했습니다.   
관련, 세부적인 설명은 [블로그](https://blog.naver.com/kyy0810/221494376698)에 있습니다.


## 설치

$ pip install -r requirements.txt


## 프로그램 시작

$ ./manage.py runserver


## 참조
이 프로젝트는 sabricot의 [django-elasticserch-dsl](https://github.com/sabricot/django-elasticsearch-dsl) 소스에 기반하여 작성되었습니다.

