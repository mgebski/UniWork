Maciej Gebski s5111611
create scripts-


create table academic(
academic_id VARCHAR2(4),
academic_name varchar2(20),
academic_mail varchar2(20),
primary key (academic_id)
);
create table institution(
institution_id varchar2(4),
institutionname varchar2(30),
primary key (institution_id)
);

create table  article(
article_id varchar2(4),
numberof_ref varchar2(3),
numof_page varchar2(4),
subbmition_date date,
primary key (article_id)
);
create table authoring(
articleid varchar2(4),
academicid varchar2(4),
primary key (articleid,academicid),
foreign key (articleid) references article(article_id),
foreign key (academicid) references academic(academic_id)
);

create table affiliation(
academicid varchar2(4),
institutionid varchar2(4),
update_date date,
primary key (academicid,institutionid),
foreign key (academicid) references academic(academic_id),
foreign key (institutionid) references institution(institution_id)
);



create table review(
review_id varchar2(4),
articleid varchar2(4),
academic varchar2(4),
review_date date,
primary key (review_id),
foreign key (articleid) references article(article_id),
foreign key (academic) references academic(academic_id)
);
insert scripts-




--ACADEMIC
insert into academic values('1','Ocean Jones','oceanj@gmail.com');
insert into academic values('2','Odysseus Soto','ocdyssj@hotmail.com');
insert into academic values('3','Chaim Hood','chaimho@gmail.com');
insert into academic values('4','Ivor Patrick','ivory2@gmail.com');
insert into academic values('5','Ciaran Burton','ciaraburt@gmail.com');
insert into academic values('6','Stacey Myers','StaceyMy@gmail.com');
insert into academic values('7','Willa Hess','Willahess@gmail.com');
insert into academic values('8','Omar Rojas','Omarroj@gmail.com');
insert into academic values('9','Quamar Maddox','QuamarMad@gmail.com');
insert into academic values('10','Xandra Bennett','Xandraben@gmail.com');

--INSTITUTION
insert into institution values ('0','No institution');
insert into institution values ('1','Bournemouth University');
insert into institution values ('2','Oxford Universtiy');
insert into institution values ('3','University Surrey');
insert into institution values ('4','Kingston University');
insert into institution values ('5','Imperial College');
insert into institution values ('6','Bristol University');
insert into institution values ('7','University of Brighton');

--ARTICLE
insert into article values ('1','24','20','23/May/2013');
insert into article values ('2','32','19','06/Aug/2014');
insert into article values ('3','162','19','04/Apr/2013');
insert into article values ('4','30','8','04/Nov/2011');
insert into article values ('5','68','3','20/Oct/2011');
insert into article values ('6','79','4','25/May/2017');
insert into article values ('7','199','5','25/Sep/2015');
insert into article values ('8','14','12','12/Jun/2016');
insert into article values ('9','152','9','07/Jul/2012');
insert into article values ('10','25','5','30/Jun/2016');
insert into article values ('11','123','21','26/May/2014');
insert into article values ('12','143','13','27/Aug/2014');
insert into article values ('13','67','15','22/Jun/2014');


--AFFILIATION
insert into affiliation  values('1','1','28/Oct/2013');
insert into affiliation  values('1','5','09/Dec/2012');
insert into affiliation  values('3','3','16/Jul/2011');
insert into affiliation  values('4','2','14/Feb/2011');
insert into affiliation  values('4','7','01/Jul/2017');
insert into affiliation  values('8','4','29/Jun/2017');
insert into affiliation  values('8','1','14/Apr/2012');
insert into affiliation  values('8','2','21/Mar/2017');
insert into affiliation  values('9','6','26/May/2011');
insert into affiliation  values('10','0',null);
insert into affiliation  values('2','0',null);
insert into affiliation  values('5','0',null);
insert into affiliation  values('6','0',null);
insert into affiliation  values('7','0',null);
--AUTHORING
insert into authoring values ('1','1');
insert into authoring values ('1','2');
insert into authoring values ('1','3');
insert into authoring values ('2','2');

insert into authoring values ('3','4');
insert into authoring values ('4','3');
insert into authoring values ('4','9');
insert into authoring values ('5','10');
insert into authoring values ('6','8');
insert into authoring values ('6','7');
insert into authoring values ('7','9');
insert into authoring values ('8','9');
insert into authoring values ('9','3');
insert into authoring values ('9','6');
insert into authoring values ('10','6');
insert into authoring values ('11','5');
insert into authoring values ('12','4');
insert into authoring values ('12','5');
insert into authoring values ('13','3');

--REVIEW
insert into review values ('1','1','4','04/Mar/2015');
insert into review values ('2','1','5','15/Mar/2015');
insert into review values ('3','1','9','05/Nov/2015');
insert into review values ('4','2','3','01/Jul/2017');
insert into review values ('5','2','1','05/Nov/2015');
insert into review values ('6','3','1','15/Mar/2015');
insert into review values ('7','3','9','21/Apr/2016');
insert into review values ('8','4','7','02/Mar/2014');
insert into review values ('9','4','6','09/Dec/2011');
insert into review values ('10','5','4','21/Apr/2016');
insert into review values ('11','5','9','09/Dec/2012');
insert into review values ('12','6','4','29/Jun/2017');
insert into review values ('13','6','5','05/Jul/2017');
insert into review values ('14','7','8','06/Aug/2017');
insert into review values ('15','7','7','22/Jun/2017');
insert into review values ('16','8','10','21/Mar/2017');
insert into review values ('17','8','2','22/Jun/2017');
insert into review values ('18','8','1','07/Oct/2017');
insert into review values ('19','9','2','01/Jul/2017');
insert into review values ('20','9','2','25/Feb/2016');
insert into review values ('21','9','7','29/May/2014');
insert into review values ('22','10','2','22/Jun/2017');
insert into review values ('23','10','3','05/Jul/2017');
insert into review values ('24','11','2','30/Mar/2015');
insert into review values ('25','11','4','30/Sep/2015');
insert into review values ('26','12','2','23/Mar/2017');
insert into review values ('27','12','3','29/Jun/2017');
insert into review values ('28','13','10','05/Sep/2016');
insert into review values ('29','13','6','06/Aug/2017');
insert into review values ('30','13','7','05/Nov/2015');


--------DROP SCRIPTS
drop table review;
drop table affiliation;
drop table authoring;
drop table academic;
drop table institution;
drop table article;






-------Select scripts-
1. Select academic_id, academic_name
from academic;

2. Select institutionname , academic_name
from institution, academic, affiliation
where institution_id = 1
and
where academic.academicid=affiliation.academic_id
and
where institution.insstitution_id=affiliation.institutionid;

3. Select  institutionname, count(academicid) as numofaffiliations
from academic, institution, affiliation
where affiliation.institutionid=institution.institution_id
and affiliation.academicid=academic.academic_id
group by institutionname
order by numofaffiliations DESC;
4. 


select distinct academic.academic_name,institution.institutionname,mostreviewed
from academic, institution, affiliation, 
        (
        select academic_id,  count(review_id) as mostreviewed
        from academic, review
        where review.academic=academic.academic_id
        group by academic_id
		
        
        ) reviews,
       (
        
            
        select max(update_date) as currentinsti
        from   affiliation,academic
        where academic_id=academicid
        group by academicid
        
         
        ) currentint
WHERE affiliation.academicid = academic.academic_id
AND affiliation.institutionid = institution.institution_id
and affiliation.update_date=currentint.currentinsti
and reviews.academic_id=academic.academic_id
order by mostreviewed desc
