## MySQL Benchmark

## Quick and dirty

```
docker run --rm -it trnubo/mysql-benchmark
MYSQL_ROOT_PASSWORD= MYSQL_ALLOW_EMPTY_PASSWORD=yes MYSQL_DATABASE=dbtest /docker-entrypoint.sh mysqld &
sysbench --test=oltp --oltp-table-size=1000 --mysql-db=dbtest --mysql-user=root --mysql-host=127.0.0.1 prepare
sysbench --test=oltp --oltp-table-size=1000 --mysql-db=dbtest --mysql-user=root --mysql-host=127.0.0.1 run
```