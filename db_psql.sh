#!/bin/bash
db_host=$(sed -n '/host/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
db_database=$(sed -n '/dbname/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
db_username=$(sed -n '/username/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
db_password=$(sed -n '/password/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
export PGPASSWORD=$db_password
echo "psql -h ${db_host} -d ${db_database} -U ${db_username}"
if [ ! -z $1 ];then
  if [ -f $1 ];then
     cmd=" -f $1"
  else 
     cmd=" -c $1"
  fi
  echo "psql -h ${db_host} -d ${db_database} -U ${db_username} $cmd"
  psql -h ${db_host} -d ${db_database} -U ${db_username} $cmd
  exit
fi
psql -h ${db_host} -d ${db_database} -U ${db_username} 
