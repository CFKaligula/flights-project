{{ config(materialized='table', unique_key=['flightName']) }}

with

source as (

    select * from {{ source('default','raw_flights') }}

),

renamed as (

    select
        flightName
        , prefixIATA as iataAirline
        , aircraftType.iataMain as iataAircraftTypeMain
        , aircraftType.iataSub as iataAircraftTypeSub
        , route.destinations[-1] as iataDestination

    from source

)

select * from renamed