# 16170 오늘의 날짜는?
from datetime import date

print("\n".join(list(map(str, (str(date.today())).split("-")))))