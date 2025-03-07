with at_stats as (
    select
    al.publicName as airlineName, 
    count() as n_flights

    from {{ source('default', 'flights') }} as f

    join {{ source('default','airlines') }} as al
    on f.prefixIATA = al.iata

    group by al.publicName

)

select *
from at_stats
