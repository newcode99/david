from math import pi

def sphere_area(diameter: float, material: str, thickness: float = 1.0) -> tuple[float, float]: #<< 함수 자체는 '문제'에 기재되어 있음.
    '''
    #상수 선언 및 인자값 유효성 확인
    1. 0이거나 음수일 경우
    2. material(재질 입력값)이 상수와 다를 경우 
    -> ValueError
    '''
    MATERIALS = {'유리': 2.4, '알루미늄': 2.7, '탄소강': 7.85}
    if diameter <= 0 or thickness <= 0 or material not in MATERIALS:
        raise ValueError

    try: #try-except 필수 1
        density_g_cm3 = MATERIALS[material] #<< 설정 필요 

        # == 하기 계산식은 문제에 기재되어 있음 ===
        area_m2 = pi * (diameter ** 2)
        area_cm2 = area_m2 * 10000
        volume_cm3 = area_cm2 * thickness
        mass_kg = (density_g_cm3 * volume_cm3) / 1000
        mars_weight_kg = mass_kg * 0.38
        return (area_m2, mars_weight_kg)
    except Exception:
        raise

def main():
    try:
        d_str = input('지름(m)을 입력하세요: ').strip()
        diameter_input = float(d_str)
        if diameter_input <= 0:
            raise ValueError

        m_raw = input('재질(유리/알루미늄/탄소강)을 입력하세요: ').strip()
        if m_raw not in ['유리', '알루미늄', '탄소강']:
            raise ValueError
        
        t_str = input('두께(cm)를 입력하세요(기본값:1): ').strip()
        thickness_input = 1.0 if t_str == '' else float(t_str)
        if thickness_input <= 0:
            raise ValueError
        
        ''' 예외 방법 2: thickness(두께) 예외처리
        if t_raw == '':
            thickness_input = 1.0
        else:
            thickness_input = float(t_raw)
        
        if thickness_input <= 0:
            raise ValueError
        '''
        
        area, weight = sphere_area(diameter_input, m_raw, thickness_input)
        print(f"재질: {m_raw}, 지름: {diameter_input:g}, 두께: {int(thickness_input):d}, 면적: {area:.3f}, 무게: {weight:.3f} kg")

    except ValueError:
        print('Invalid input.')
        return
    except Exception:
        print('Processing error.')
        return

if __name__ == '__main__':
    main()
