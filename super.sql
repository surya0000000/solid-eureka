
CREATE SEQUENCE user_id_seq;
create table heroes(
id smallint NOT NULL DEFAULT nextval('user_id_seq')
,
name text not null,
gender varchar(1) not null);
ALTER SEQUENCE user_id_seq OWNED BY heroes.id;





