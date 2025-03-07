with full_flights as (
    select
    flightName,
    al.publicName as airlineName, 
    d.englishName as destinationName,
    at.longDescription as aircrafttypeName

    from {{ source('default', 'flights') }} as f

    left join {{ source('default','airlines') }} as al
    on f.prefixIATA = al.iata

    left join {{ source('default','destinations') }} as d
    on f.destination = d.iata

    left join {{ source('default','aircrafttypes') }} as at
    on f.aircraftTypeMain = at.iataMain and f.aircraftTypeSub = at.iataSub

)

select *
from full_flights
