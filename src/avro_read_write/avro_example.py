import avro
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from common.utils import *

avro_schema="./user.avsc"
avro_data="./user.avro"

def read_and_write_avro_data():
    avsc_string = """{"namespace": "example.avro",
     "type": "record",
     "name": "User",
     "fields": [
         {"name": "name", "type": "string"},
         {"name": "age",  "type": ["int", "null"]},
         {"name": "sal", "type": ["long", "null"]},
         {"name": "xfloat", "type": ["float", "null"]},
         {"name": "xdouble", "type": ["double", "null"]},
         {"name": "xbytes", "type": ["bytes", "null"]},
         {"name": "xbool", "type": ["boolean", "null"]}
     ]
     }
    """

    # generate a avro schema file
    write_to_file(avro_schema,avsc_string)

    schema = avro.schema.Parse(open(avro_schema).read())

    writer = DataFileWriter(open(avro_data, "wb"), DatumWriter(), schema)
    writer.append({"name": "Alyssa", "age": 256,"sal": 30438940839849384, "xfloat": 983494.3434, "xdouble": 983498934.3434, "xbytes": b"52017-", "xbool": True})
    writer.append({"name": "dd5", "age": 6, "sal": 8940839849384, "xfloat": 983494.3434, "xbytes": b"dsd2017-", "xbool": True})
    writer.close()

    # load avro file
    reader = DataFileReader(open(avro_data, "rb"), DatumReader())
    for user in reader:
        print(user)
    reader.close()

    # cleanup
    os.remove(avro_schema); os.remove(avro_data)


if __name__ == "__main__":
    read_and_write_avro_data()
