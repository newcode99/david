# Local change fore merge test

from flask import Flask, render_template

app=Flask(__name__) #관습적 변수 이름
 
@app.route('/') # 기본 주소(/)로 접속 시 되기에 /menu와 연동 (같은 페이지 출력)
@app.route('/menu') # "/menu" 라는 경로 설정


def menu():
    return render_template('menu.html') # templates/menu.html 파일 출력

@app.route("/test2")
def test1():
    return render_template('test2.html')

# @app.route("/test3")
# def test3():
#     return render_template('test3.html')

if __name__ == "__main__":
    app.run(debug=True)


# 경로에 접근하면 menu.html 파일을 보여줘야 한다. 즉, 연동할 html 파일이 필요함.
# (다음 단계에서 menu.html을 만드므로, 이 둘은 반드시 연결되어야 함)


