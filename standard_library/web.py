# --- urllib : URL을 가져오기 위한 파이썬 모듈
import urllib.request

## request.urlopen : http 요청
resource = "https://wikidocs.net/33"
with urllib.request.urlopen(resource) as html:
    with open("wikidocs_33.html", "wb") as file:
        file.write(html.read())

# --- webbrowser : 시스템 브라우져를 호출할 때 사용하는 모듈
import webbrowser

## open_new : 시스템 브라우져 새 창으로 열기
webbrowser.open_new('https://www.naver.com')
