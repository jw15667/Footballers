use football_db;


select FirstSet.Name
from
(
select Name from table_3
	where Player_ID in (
		select Player_ID from table_1
		where Team_ID in (
			select Team_ID from table_1
			where Player_ID in (
				select Player_ID from table_3
				where Name = 'John Terry')))) as FirstSet
	inner join 
	 (
select Name from table_3
	where Player_ID in (
		select Player_ID from table_1
		where Team_ID in (
			select Team_ID from table_1
			where Player_ID in (
				select Player_ID from table_3
				where Name = 'Mikel Arteta')))) as SecondSet
	on FirstSet.Name = SecondSet.Name
    order by FirstSet.Name;
