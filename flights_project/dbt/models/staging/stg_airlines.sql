{{ config(materialized='table', unique_key=['iata']) }}

with

source as (

    select * from {{ source('default','raw_airlines') }}

),

renamed as (

    select
        iata
        , publicName as fullName

    from source

)

select * from renamed