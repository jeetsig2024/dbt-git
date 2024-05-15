{{config(materialized="table",post_hook= 'grant select on {{this}} to role ANALYST')}}

select * from {{ source('source_check','customer')}}