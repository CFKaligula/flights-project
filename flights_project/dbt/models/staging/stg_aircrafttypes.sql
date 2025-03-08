{{ config(materialized='table', unique_key=['iataMain', 'iataSub']) }}

with

source as (

    select * from {{ source('default','raw_aircrafttypes') }}

),

renamed as (

    select
        iataMain
        , iataSub
        , longDescription as fullName

    from source

)

select * from renamed