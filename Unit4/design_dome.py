import csv
from math import pi
import numpy as np

wsl_path  = '/mnt/c/Users/c0108/Documents/mars_base/Mars_Base_Inventory_List.csv'

def main():
    """ 파일 포멧팅: 호출 & 파싱 및 리스트 전환 / 내림차순 정렬"""
try:
    with open(wsl_path, 'r', encoding = 'UTF-8') as mars:
        reader = csv.reader(mars) #reader의 기본 기능으로 포멧팅 (리스트 형태로 변환 및 콤마 구분)

        header = next(reader)                    # for i in reader: #출력 시도
        body = list(reader) # 2차원 리스트         # print(i) 
    
    print (body)

    body = sorted(body, key=lambda x: x[4], reverse=True) #내림차순 정렬

    abc = [ i for i in body if float(i[4]) >= 0.7]
    print(abc)


    with open('Mars_Base_Inventory_danger2.csv', 'w', encoding='UTF-8') as w:
        inventory = csv.writer(w)
        inventory.writerows(abc) #짜잔 완성


except FileNotFoundError: # 파일 오류
    print('File not found')

except LookupError:  #알 수 없는 값. 
    print('?뭐함')

except Exception: #UnicodeDecode & Other / 디코딩 외 
    print ('Error..')

if __name__ == "__main__":
    main()


   # 필터링 시스템(구조/조건) : 인덱싱을 통해 항목(칼럼)구분 후 / 조건부 인덱싱 값 산출 


def sphere_area(diameter, material, thickness):
# ========== 지름 입력 처리 ========= #
    try:
        diameter_input = float(input('구축할 돔의 지름을 설정해주세요(단위: m):').strip())
        
        if diameter_input <= 0:
            print('VlaueError: 지름의 값은 0 이하로 설정할 수 없습니다.')
            exit() #<< fo (sys.exit)
            # exit()

    except ValueError:
        print('ㄴㄴ이거 숫자아님')
        exit()

    # ========== 파라미터 정의 ========= #
    cm = 1
    m = cm * 100

    diameter = diameter_input*m
    thickness = cm


    # # ========== 재질/밀도 게산식 (g/cm3) ========= #
    g = 1

    glass = 2.4 * g / (cm**3)
    aluminium = 2.7 * g / (cm**3)
    carbon_steel = 7.85 * g / (cm**3)
    material = {'유리':glass, '알루미늄':aluminium, '탄소강':carbon_steel}


    try:
        material_input = input('돔의 재질을 선택해주세요(유리, 알루미늄, 탄소강 중 1택): ')
    #입력값 -> 각 str과 %data 계산 식으로 전달 (ex. 유리가 입력될 경우 ->  2.4(g/cm3) 데이터를 수식에서 호출 input == material[0] -> material = 2.4 인자 호출)

        if material_input not in material: # 입력값과 리스트 값을 순회 비교
            print('3중 1택이라고라')
            print(f'리스트 값 {material}, i값 {material_input}')
            exit()

        material_p = material[material_input]

    except ValueError:
        print('ㄴㄴ이거 숫자아님')

    except Exception:
        print('실행할 수 없는 코드입니다.')
        exit()  # print(material_input, material_p)


    #==== 결과 출력식 : 표면적 / 부피 / 무게
    try:  # or pi = 3.141592653589793

        r = diameter / 2
        R = r + thickness
        sa = 2 * pi * (r**2)

        v = (2/3) * pi * pow(R, 3) - pow(r, 3)  #(1/2) × (4/3)πr³ = (2/3)πr³
        m = v * material_p * 0.38
        print(f'재질 ⇒ {material_input}, 지름 ⇒ {diameter_input},두께 ⇒ {int(thickness)} 표면적 ⇒ {sa:.3f}, 부피 ⇒ {v:.3f}, 무게 ⇒ {m:.3f} Kg')

    except ValueError:
        ('수식 오류')

# np.sqrt # == 기존 반복문 지점 ==

# #=================

# print(f'재질 입력값: {material_input}, 현재 i 값: {material_input}, 재질 입력수: {len(material_input)}')
# print(f'재질 ⇒ {material_input}, 지름 ⇒ {diameter_input}, 표면적 ⇒ {}, 내면적 ⇒ {}, 무게 ⇒ {}')


Mars_1 = '/mnt/c/Users/c0108/Documents/mars_base/mars_base_main_parts-001.csv'
Mars_2 = '/mnt/c/Users/c0108/Documents/mars_base/mars_base_main_parts-002.csv'
Mars_3 = '/mnt/c/Users/c0108/Documents/mars_base/mars_base_main_parts-003.csv'

def mars_parts():
    try:
        arr1 = np.loadtxt(Mars_1, delimiter=",", encoding="utf-8-sig", dtype = str)
        arr2 = np.loadtxt(Mars_2, delimiter=",", encoding="utf-8-sig", dtype = str)
        arr3 = np.loadtxt(Mars_3, delimiter=",", encoding="utf-8-sig", dtype = str)
        # print(type(arr1))
    except FileNotFoundError as e:
        print(f"파일 없음")
        return
  
    except UnicodeDecodeError:
        print("읽기 실패")
        
    except Exception:
        print("오류")
    


    #헤더/바디 (str열)분리 #슬라이싱 = 좌측(행), 우측(열)
    header = arr1[0] # shape 즉, 2차원 배열(행=가로 줄, 열=세로 칸)
    body1, body2, body3 = arr1[1:], arr2[1:], arr3[1:] #str열 분리 / 행 기준 

    #데이터 분리
    head_all = body1[:,0] #콤마는 다차원 슬라이싱 / 축 구분 / #1열 값들(부품명 목록)만 가져옴
    df_1 = body1[:,1].astype(float) #열 기준
    df_2 = body2[:,1].astype(float)
    df_3 = body3[:,1].astype(float)
    
    merged_values = np.column_stack((df_1, df_2, df_3)) #<< 숫자 먼저 병합
    avg = merged_values.mean(axis=1) #숫자열 행의 데이터 avg / ndarry 평균 계산 매서드
    parts = np.column_stack((head_all, merged_values, avg)) # 평균 (행 기준)
    # print(parts)
    
    mask = avg < 50
    filtered = parts[mask] #True(<50)열만 필터링
    
    # filtered_str = filtered.astype(str)
    # filtered_str[:, 4] = avg_str

# 평균<50 필터링까지 끝난 상태에서
    avg_str = np.char.mod('%.3f', filtered[:, 4].astype(float)) # 문자열 포맷팅을 배열 전체에 적용
    out_str = np.column_stack((filtered[:, 0], filtered[:, 1], filtered[:, 2], filtered[:, 3], avg_str))

    try:
        hdr = ",".join([header[0], header[1], header[1], header[1], "avg"])
        avg_str = np.char.mod('%.3f', filtered[:, 4].astype(float))
        out_str = np.column_stack((filtered[:, 0], filtered[:, 1], filtered[:, 2], filtered[:, 3], avg_str))
        np.savetxt("parts_to_work_on.csv", out_str, delimiter=",", fmt="%s", header=hdr, comments="")

        # avg_str = np.char.mod('%.3f', avg[mask])
        # out = np.column_stack((head_all[mask], avg_str))
        # np.savetxt("parts_to_work_on.csv", out, delimiter=",",
        #    fmt="%s", header="{},avg".format(header[0]), comments="")

    except PermissionError:
        print("[저장 실패: 권한/락 에러")

# # print(type(parts), parts.dtype, parts.shape)


if __name__ == "__main__":
    pass




"""
#무게
gravity = 0.38
Earth = 0
weight = 0.38

total_weight = weight * gravity

"""


'''

# if diameter_input < 1 and type(diameter_input) is not float:
#     print('invaild input')    
#     exit()


# for i in material:
#     if i == material_input:
#         print ('참')
#         print(f'리스트 값 {material}')
# else:
#     print('3중 1택이라고라')
#     print(f'리스트 값 {material}, i값 {i}')
# print(f'입력 {material_input}')



'''
