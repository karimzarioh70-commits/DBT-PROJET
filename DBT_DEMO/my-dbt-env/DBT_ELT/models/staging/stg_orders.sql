with source as (
    select * from {{ source('my_dbt_db', 'raw_orders') }}
),
renamed as (
    select
        id as customer_id,
        ordered_at as date_ordres
    from source
)
select * from renamed