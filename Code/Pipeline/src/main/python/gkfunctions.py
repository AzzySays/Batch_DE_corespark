# All necessary functions
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DoubleType


def read_schema(schema_arg):
    d_types = {
        "StringType()":StringType(),
        "IntegerType()":IntegerType(),
        "TimestampType()":TimestampType(),
        "DoubleType()":DoubleType()
    }

    split_values = schema_arg.split(",")
    sch = StructType()
    for i in split_values:
        x = i.split(" ")
        sch.add(x[0], d_types[x[1]], True)
    return sch
