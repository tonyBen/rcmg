revoke all on database rcmg from rcmg_user;
select pg_terminate_backend(pg_stat_activity.pid) from pg_stat_activity where datname='rcmg' and pid<>pg_backend_pid();
drop user if exists rcmg_user;
drop database if exists rcmg;
create database rcmg;
create user rcmg_user with password 'rcmg_pass';
alter user rcmg_user with SUPERUSER;
CREATE EXTENSION pgcrypto;