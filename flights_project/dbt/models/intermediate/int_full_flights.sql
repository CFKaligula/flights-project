with full_flights as (
    select
    flightName,
    al.fullName as airlineName, 
    d.fullName as destinationName,
    at.fullName as aircraftTypeName

    from {{ ref('stg_flights') }} as f

    left join {{ ref('stg_airlines') }} as al
    on f.iataAirline = al.iata

    left join {{ ref('stg_destinations') }} as d
    on f.iataDestination = d.iata

    left join {{ ref('stg_aircrafttypes')}} as at
    on f.iataAircraftTypeMain = at.iataMain and f.iataAircraftTypeSub = at.iataSub

)

select *
from full_flights
