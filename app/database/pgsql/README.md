# PGSQL CONFIG
### Set up to:
    cd ./pgsql/
    cp pg_service.conf ~/
    mv ~/pg_service.conf ~/.pg_service.conf

## pg_service.conf(PATH:~/.pg_service.conf)

    # .pg_service.conf format
    # password : ~/.pg_pass
    # example):
    #    psql connection
    # psql service=mydb

    [mydb]
    host=[host name]
    port=[port number]
    user=[access user]
    dbname=[database]

    [test]
    host=[host name]
    dbname=[database]
    user=[access user]

## pg_pass(PATH:~/.pg_pass)

    #.pg_pass format
    hostname:port:database:username:password

***

## export ENV

    Password is ~/.pg_pass
    Example:

    export PGHOST="localhost"
    export PGHOSTADDR="localhost"
    export PGPORT=5432
    export PGDATABASE="mydb"
    export PGUSER="admin"
