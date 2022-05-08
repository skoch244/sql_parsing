create procedure asd

select * from 	`table1` ,    table2,
		#table3, table3
--------------------------------------
--------------------------------------
select *
			from 	table4 ,table5  , table6,        table7     join     #table7   on table5.id = table7.id
--------------------------------------
--------------------------------------
select * from dbo.table8 c
                cross apply [db01].[dbo].[table9] ap
          cross apply ( select l 'Letter', sum (cl) 'LetterCount'
                    from
                (select left( ap.City, 1 ) l,
                        len( City ) - len ( replace ( City, left( ap.City, 1 ) ,'' ) )  cl
                   from table10 where CountryID = c.CountryID
                 ) t
              group by l
            ) apLetters
--------------------------------------
--------------------------------------
exec deposql.GEstDepoDB.dbo.abb_CX_EIM_CONTACT_new_period
exec   script2
exec
        [dbo].[script3]
exec     serv1.dbo.script4
--------------------------------------
--------------------------------------
select *
	   FROM
[#table11] ,[serv1].[db1].[dbo].[table11]  ,       dbo.table12,
table13

join
		db1.dbo.table14 on table14.id = table13.id
	left JOIN db1.dbo.table15 on table15.id = table13.id
--------------------------------------
--------------------------------------
SELECT * FROM OPENQUERY (OracleSvr, 'SELECT name FROM table16 join [db1].[dbo].[table17] WHERE name = ''NewTitle''');