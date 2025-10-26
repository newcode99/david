import json
# print ("파일 내용", os.listdir(dir))
def main():
    wsl_file_path = '/mnt/c/Users/c0108/Documents/mission_computer_main.log' # os 하드웨어 접근

    try:
        with open(wsl_file_path, 'r', encoding='UTF-8' ) as mars: # encoding=''
            mars_data = mars.read().splitlines()#split(',', '/n')#.replace('\n', '') #문자열 변경
            # mars_data.sort(reverse=True) #list formet으로 만들어야 함으로 'readlines'사용
            # .sort() 함수는 원본을 내림차순으로 정렬 함 / reverse=true는 역정렬 / reverse() 함수는 즉 반
                # ㄴ 해당 사항에서 요구하는 것은 시간 역순 정렬 

            # header  = mars_data[0]
            # body = mars_data[1:]
            body = [] #body 칼럼용
            all_data = [] #딕셔너리 저장용

            # ============== Header / Body 값 지정 ============== # / 헤더 및 바디를 지정하고 ',' 기준으로 스플릿
            for i, j in enumerate(mars_data):

                if i == 0:
                    header = j.split(',') #헤더 칼럼
                    # print(j[0])
                else:
                    abc = j.split(',') #바디 칼럼 / #splitlines로 인해 한 줄 씩 출력된 문자열을 ',' 기준으로 블럭 처리
                    body.append(abc)

            if i in mars_data:
                print

            all_body = list(body)
            all_body.reverse()
            # print(all_body)

    # ============== Header + Body Mapping (idx) ============== #
        # dict_data = header

        for col_body in all_body: #time, event, message를 담음
            dict_data =  {}

            for i, col_head in enumerate(header):
                if i < len(col_body):
                    # dict_data[col_head] = []

                    dict_data[col_head] = col_body[i]
                    # dict_data[col_head].append(col_body[i])
            all_data.append(dict_data)
        
        print (all_data)
        # description(all_data)
        #            # ㄴ 출력 형식: 헤더0: 데이터0 / 헤더1: 데이터1 / 헤더2: 데이터2 
        with open('mission_computer_main.json', 'w', encoding='UTF8') as mars_json:
            json.dump(all_data, mars_json, indent=2) #json 변환 파일 및 작성 파일 호출 / indent = 블럭 스페이싱

# #        # ============== except error ============== #

    except FileNotFoundError: # 파일 오류
        print('File not found')

    except LookupError:  #알 수 없는 값. 
        print('?뭐함')

    except Exception: #UnicodeDecode & Other / 디코딩 외 
        print ('Error..')

# #     # print('\\n 개수:', mars_data.count('\n')) # strip & split test

# #     # #          # ============== except error ============== #


# #     # # =================== #위험 키워드 탐색 및 사고 원인 분석(data formatting)===================== #

# def description(log_data):
    log_data = all_data
    error_event = []
    warning_list = ['powered down', 'oxygen', 'unstable', 'explosion']
    description = {
            'unstable': '사고원인: 산소 탱크 불안정',
            'explosion': '사고원인: 산소 탱크 폭발',
            'powered down': '사고원인: 센터 및 임무 제어 시스템 전원 셧다운',
            'oxygen': '사고원인: 산소 시스템 문제'
        }
    
    #이벤트 발생 계
    for log in log_data:
    
        if log['event'] == 'ERROR': #key 호출 후 해당 열에서 특정 문자열 탐색
            error_event.append(log)

        # if 'ERROR' in log:
        #     error.append('ERROR') << Key 값을 탐색함으로 str 탐색 불가.
        
        message = log['message']


        for i in warning_list:
        
            if i in message:
                error_event.append({'time':log['timestamp'],
                    'message': message,
                    'issue': i,
                    'cause': description[i]})

                break
    
        # pre = {'time':log['timestamp'],
        #  'message': message,
        #  'issue': i}
    print(error_event)

    count_error = len(error_event)
    print(f'위험 상황 발생 횟수: {count_error}')

    total = len(log_data)
    print (f'이벤트 발생 횟수(전체): {total}')

    gen_md(error_event, count_error, total)
    # #=================== .Md 파일 제작===================== #
    # md formetting & generate

def gen_md(error_event, count_error, total):

    data = []
    
    data.append('# 사고 분석 보고서\n') #보고서 구조 설계

    data.append(f'## 요약\n')
    data.append(f'분석 대상: 로그 파일 전체(총 {total}건)\n\n') # << 이부분
    data.append(f'총 발생 로그: {count_error}/n') #보고서 구조 설계 #이 부분

    data.append("## 상세 분석\n") 
    for item in error_event:  # error_event 사용 #<< 이부분
        data.append(f"### {item['time']}\n")
        data.append(f"**메시지**: {item['message']}\n")
        data.append(f"**이슈**: {item['issue']}\n")
        data.append(f"**사고원인**: {item['cause']}\n\n")

    # print(data)
    with open('log_analysis.md', 'w', encoding='UTF8') as mars_md:
        mars_md.write(''.join(data)) #변환 객체 및 파일 핸들러 삽입

       # mars_md.write(data, mars_md)
    
if __name__ == '__main__':
    main()
