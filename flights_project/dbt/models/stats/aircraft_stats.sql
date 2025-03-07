with at_stats as (
    select
    aircrafttypeName, 
    count() as n_flights

    from {{ ref('full_flights') }} as f
    group by aircrafttypeName

)

select *
from at_stats
