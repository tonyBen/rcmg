#!/bin/bash
export RED='\033[0;31m'
export BLUE='\033[1;32m'
export GREEN='\033[1;34m'
export NC='\033[0m' # No Color

BASEDIR=$(cd $(dirname $0) && pwd)
cd $BASEDIR>/dev/null
op=$1
args=$2
usage()
{
	cat <<EOF
USAGE: $0 OPTIONS
OPTIONS:
	build		string 		only build the images & tag 
	start		string		build & restart service
	init		string		build & init database & start service
EOF
}

build_image()
{
	echo "----------------------------------"
	echo -e "${BLUE}Begin Build Image Args ${NC}${RED}$1 ${NC}"
        echo "----------------------------------"
	if  [ $(docker images|grep rcmg_base|wc -l) -eq 0 ] || [ "$1" = "all" ] ;then
		echo -e "${GREEN}Begin Build Base Image${NC}"
		echo "docker build -t rcmg_base:latest -f rcmg_docker_file.base ."
		cd backend >/dev/null
		docker build -t rcmg_base:latest -f rcmg_backend_dockerbase .
		cd - >/dev/null
	fi
	echo "docker build -t rcmg_backend:latest ."
	cd backend>/dev/null
	docker build -t rcmg_backend:latest .
	cd ->/dev/null
	echo "docker build -t rcmg_ui:latest ."
	cd ui>/dev/null
	docker build -t rcmg_ui:latest . 
	cd ->/dev/null
	echo "----------------------------------"
	docker images 
	echo "----------------------------------"
}

start_service()
{
	docker-compose up -d 
	echo "----------------------------------"
        docker ps -a 
	echo "----------------------------------"
}

stop_service()
{
	docker-compose down
}

recreate_db()
{	
	echo "---------------------------------"
	echo -e "${BLUE}Begin ReCreate DataBase & User${NC}"
	echo "---------------------------------"
	db_host=$(sed -n '/host/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
	read -p "admin username of db:" db_username
	read -p "admin password of db:" db_password
	read -p "admin database of db:" db_database
	echo "psql -h ${db_host} -d ${db_database} -U ${db_username} -f scripts/database/create_database.sql"
	export PGPASSWORD=$db_password
	psql -h ${db_host} -d ${db_database} -U ${db_username} -f scripts/database/create_database.sql
	

}
recreate_tables()
{
	echo "---------------------------------"
	echo -e "${BLUE}Begin ReCreate All TABLES${NC}"
	echo "---------------------------------"
	db_host=$(sed -n '/host/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
	db_database=$(sed -n '/dbname/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
	db_username=$(sed -n '/username/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
	db_password=$(sed -n '/password/p' config_server.yaml |head -1|awk '{print $2}'|awk '{gsub(/^\s+|\s+$/, "");print}')
	export PGPASSWORD=$db_password
	echo "psql -h ${db_host} -d ${db_database} -U ${db_username} -f scripts/database/init_tables.sql"
	psql -h ${db_host} -d ${db_database} -U ${db_username} -f scripts/database/init_tables.sql
}

init_service()
{
	recreate_tables
}

reset_service()
{
	recreate_db
}

main()
{
	if [ -z $op ];then
	  usage
	  exit -1
	fi
	if [ "$op" == "build" ];then
		build_image $args
	elif [ "$op" == "start" ];then
		build_image $args
		start_service
	elif [ "$op" == "reset" ];then
		reset_service
	elif [ "$op" == "init" ];then
		init_service
        else
		usage
		exit -1
	fi
}
main

