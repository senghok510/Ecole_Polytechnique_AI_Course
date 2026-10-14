select distinct m.title, p.name
from movie m, cast_info c, person p, role_type r
where p.id = c.person_id
and c.movie_id = m.id
and c.role_id = r.id
and (r.role='actor' or r.role = 'actress'); 


select m.title, p.name 
from movie m, cast_info c, person p, role_type r
where p.id=c.person_id and c.movie_id=m.id and c.role_id=r.id and
r.role='actor' and m.title like 'King%' and m.production_year=2015; 
