# Local change fore merge test

from flask import Flask, render_template
import socket #설정 정보 접근  -> 호스트명 불러옴

app=Flask(__name__) #관습적 변수 이름
 
@app.route('/') # 기본 주소(/) 미설정 시 접속 시 에러 "/menu"를 추가해 / 실행 시 /menu로 넘어가도록 연동했었음. (같은 페이지 출력)
def home(): #home() 함수는 필수적으로 정의해줘야 함. /  # 함수 정의 (반드시 데코레이터 바로 아래)
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = '' #else일땐 empty srt 상태여야 함.
   
    return render_template('index.html', computername=hostname)  #computername: flask가 전달한 데이터만 사용이 가능함 / 화면 출력을 위해선 html 필요 -> html에 접근해야 함. -> 접근할 수 있는 언어로 데이터를 전송해야 함. -> html도 인식할 수 있는 [computername]으로 host변수를 담고 이 내용을 html로 전송 -> html이 이 함수에 담긴 내용을 기반으로 출력
 #데코레이터와 함수는 같은 레벨 / #Python 문법: 함수는 반드시 return으로 끝남.


@app.route('/menu') # "/menu" 라는 경로 설정
def menu():
    return render_template ('menu.html') # templates/menu.html 파일 출력
    

#index.html = web default pg

if __name__ == "__main__":
    if __debug__ == True:
        print("true")
    app.run(debug=True)


# 경로에 접근하면 menu.html 파일을 보여줘야 한다. 즉, 연동할 html 파일이 필요함.
# (다음 단계에서 menu.html을 만드므로, 이 둘은 반드시 연결되어야 함)
