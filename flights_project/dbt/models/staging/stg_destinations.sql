{{ config(materialized='table', unique_key=['iata']) }}

with

source as (

    select * from {{ source('default','raw_destinations') }}

),

renamed as (

    select
        iata
        , city
        , country
        , publicname.english as fullName

    from source

)

select * from renamed