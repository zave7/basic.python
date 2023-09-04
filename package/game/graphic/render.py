# from package.game.sound.echo import echo_test # 절대 경로 임포트
from ..sound.echo import echo_test # 상대경로 import

def render_test():
    print("render")
    echo_test()

# 1. 상대 경로를 이용하여 import 하게되면 '__name__' 변수의 값으로 해동 모듈의 위치를 파악한다.
# 2. 만약 '__main__' 으로 설정 될 경우 패키지의 구조가 실제 파일 시스템에 있는 위치에 관계없이 최상위 모듈인 것 처럼 된다.
# 참고 자료: 
#   https://velog.io/@anjaekk/python%EC%A0%88%EB%8C%80%EA%B2%BD%EB%A1%9C%EC%83%81%EB%8C%80%EA%B2%BD%EB%A1%9C-%EC%83%81%EB%8C%80%EA%B2%BD%EB%A1%9C-import-%EC%97%90%EB%9F%AC%EC%9D%B4%EC%9C%A0%EC%99%80-%ED%95%B4%EA%B2%B0
#   https://docs.python.org/3/tutorial/modules.html#intra-package-references
#   https://peps.python.org/pep-0328/