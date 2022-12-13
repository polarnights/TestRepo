Собираем через докер командами:

docker build -t mtu_finder -f Dockerfile .

docker run mtu_finder HOSTNAME

———————————

Ошибки:

Host is not valid exception for host = HOSTNAME -> имя хоста не валидное

Bad response (returncode) for host = HOSTNAME -> код возврата пинга хоста ненулевой (хост недоступен)

