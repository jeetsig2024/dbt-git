{{config(materialized='table')}}

select 
 c.c_custkey,
 c.c_name,
 c.c_nationkey as nation,
 sum(o.o_totalprice) as total_order_price
 from {{source('source_check','customer')}} c left join 
 {{ source('source_check','orders')}} o 
 on c.c_custkey = o.o_custkey

 {{group_by(3)}}