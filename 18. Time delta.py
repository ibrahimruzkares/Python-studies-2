from datetime import datetime
from datetime import timedelta

moment = datetime.now()
tdelta = timedelta(days= 7, hours = 5)
print(moment + tdelta)
print(moment - tdelta)