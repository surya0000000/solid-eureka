




create table affiliation (id integer primary key,name text not null,location text not null);


insert into affiliation (name ,location) values ("Stark", "Winterfell");

insert into affiliation (name ,location) values ("Lannister","Kings Landing");


insert into affiliation (name ,location) values ("Targeryen","DragonStone");








create table character( id INTEGER primary key,name text NOT NULL, gender varchar(1),nickname text,  affid integer references affiliation(id));

insert into character(name ,gender,affid) values("Eddard Stark","m",1);

insert into character (name,gender,affid) values ("Cersei Lannister","f",2);

insert into character (name,gender,nickname,affid) values ("Danerys Targeryen", "f","Queen",3);

insert into character(name,affid) values("shouldnt be here",536353636);


