from database.common.models import db, History
from database.core import crud
from site_API.core import headers, site_api, url, params

db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = site_api.get_num_fact()
fact_by_date = site_api.get_date_fact()
response = fact_by_number('GET', url, headers, params, 10, timeout=5)
response = response.json()
data = [{'number': response.get("number"), 'message': response.get("text")}]

db_write(db, History, data)

response = fact_by_date('GET', url, headers, params, '8', '17', timeout=5)
response = response.json()
data = [{'number': response.get("year"), 'message': response.get("text")}]

db_write(db, History, data)

retrieved = db_read(db, History, History.number, History.message)

for element in retrieved:
    print(element.number, element.message)
