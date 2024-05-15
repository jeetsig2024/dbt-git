from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(materialized='table')

    df= session.table('SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.TIME_DIM')

    return df

# from snowflake.snowpark import Session 
# from snowflake.snowpark.functions import col


# def model(dbt, session):
#     # Must be either table or incremental (view is not currently supported)
#     dbt.config(materialized = "table",database='DEMO_DB',schema='BRONZE')
#     print("Inside Bronze_customer")

#     # DataFrame representing an upstream model
#     df = session.table("snowflake_sample_data.TPCH_SF1.CUSTOMER")
#     return df