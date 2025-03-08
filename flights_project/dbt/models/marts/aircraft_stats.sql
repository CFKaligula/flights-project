with at_stats as (
    select
    aircraftTypeName, 
    count() as n_flights

    from {{ ref('int_full_flights') }} as f
    group by aircraftTypeName

)

select *
from at_stats
