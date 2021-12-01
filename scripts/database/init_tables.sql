drop sequence if exists org_seq ;
CREATE SEQUENCE org_seq
    START WITH 100
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


-----------------------------------------
- Table: 	org_info
-----------------------------------------
drop table if exists org_info cascade;
create table org_info(
    org_id bigint DEFAULT nextval('org_seq'::regclass) NOT NULL,
    org_name varchar(100) not null,
    create_time timestamp default now(),
	primary key (org_id)
);

-----------------------------------------
- Table: 	org_user_info
-----------------------------------------
drop table if exists org_user_info cascade;
create table org_user_info(
	user_id uuid DEFAULT gen_random_uuid() NOT NULL,
    org_id int not null,
    user_name varchar(100) not null,
    user_pass varchar(100) not null,
	user_full_name varchar(100),
	user_short_name varchar(100),
	email varchar(100),
	phone varchar(20),
	primary key (org_id,user_name)
);
alter table ONLY org_user_info ADD CONSTRAINT org_user_info_orgid_fkey FOREIGN KEY (org_id) REFERENCES org_info(org_id) ON DELETE CASCADE;


