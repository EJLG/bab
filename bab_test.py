from decimal import MIN_ETINY
from multiprocessing.pool import MapResult
import requests
import json
# API 엔드포인트 URL
api_url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

# 필요한 파라미터 설정
params = {
    'ATPT_OFCDC_SC_CODE': 'Q10',
    'SD_SCHUL_CODE': '8490058',
    'MMEAL_SC_CODE': '1',
    'MLSV_YMD': '20231208',
}

# API 요청 보내기
response = requests.get(api_url, params=params)

# 응답 데이터
full_text = response.text

# 줄 단위로 나누기
lines = full_text.splitlines()

# 5번째 줄 출력
lunch_menu = lines[19]
# print(lunch_menu)

# 필요없는 것들 제거
remove_numbers = str.maketrans('', '', '1234567890')
remove_special = str.maketrans('', '', '<>!().[]')
clean_things = lunch_menu.translate(remove_numbers)
clean_things = clean_things.translate(remove_special)

clean_things = clean_things.replace('/DDISH_NM','')
clean_things = clean_things.replace('DDISH_NM','')
clean_things = clean_things.replace('CDATA','')
clean_things = clean_things.replace('br/','\n')
clean_things = clean_things.replace('/',' + ')

menu_result = clean_things.translate(remove_special)
menu_result = menu_result[4:]
# 결과 출력
print(menu_result)
