with at_stats as (
    select
    at.longDescription as aircrafttypeName,
    count() as n_flights

    from {{ source('default', 'flights') }} as f

    join {{ source('default','aircrafttypes') }} as at
    on f.aircraftTypeMain = at.iataMain and f.aircraftTypeSub = at.iataSub

    group by at.longDescription

)

select *
from at_stats
