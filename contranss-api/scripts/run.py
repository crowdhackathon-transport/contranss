from elasticsearch import Elasticsearch
import unicodecsv as csv


es = Elasticsearch(['http://localhost:9200'])

with open('/home/giorgos/Documents/personal/transporty/api/scripts/importer/oasa_routes/stops.txt', 'rb') as in_file:
    data_reader = csv.reader(in_file, delimiter=',', encoding='utf-8')

    # stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,location_type
    for idx, row in enumerate(data_reader):
        stop = {
            'code': row[1],
            'name': row[2],
            'desc': row[3],
            'location': {
                "lat": row[4],
                "lon": row[5]
            },
            'type': row[6]
        }

        print es.index(index="stop", doc_type='stop', id=row[0], body=stop)
