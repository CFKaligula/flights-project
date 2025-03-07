﻿with at_stats as (
    select
    airlineName, 
    count() as n_flights

    from {{ ref('full_flights') }} as f
    group by airlineName

)

select *
from at_stats
