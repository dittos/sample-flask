sample-flask
============

## 이 저장소의 목적

1. 나의 Flask 코딩 컨벤션과 프로젝트 레이아웃을 정리한다. 가급적 상세히 문서화한다.
2. 그것을 여러가지 방향으로 바꾸며 실험하고, 더 나은 방향으로 발전시킨다.
3. 자주 나타나는 패턴과 boilerplate 코드를 발견하고, Flask를 대체할(또는 보강할) 프레임워크를 개발하는데에 참고한다.

## 사용하기

    git clone ...
    cd sample-flask
    virtualenv env
    . env/bin/activate
    pip install -e .
    mkdir instance
    cp config.py.sample instance/config.py
    python manage.py db create_all
    python manage.py runserver

## 바뀐 점

### 2014-03-22

App Factory 사용.

### 2013-12-16

Flask-Script 업데이트로 필요 없어진 hack 제거.
