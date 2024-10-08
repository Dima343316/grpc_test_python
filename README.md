# GRPC Python Server and Client Project

## Описание

Этот проект демонстрирует использование gRPC для взаимодействия между клиентом и сервером на Python. Сервер предоставляет gRPC сервис, а клиент обращается к этому сервису для выполнения удаленных вызовов. В проекте используются файлы протокола `.proto` для описания сервисов и сообщений, которые сгенерированы с использованием `grpcio-tools`.


## Требования

Для запуска проекта локально, убедитесь, что у вас установлены следующие инструменты:

- Python 3.9 или новее
- `pip` для установки зависимостей
- Docker и Docker Compose (для контейнеризированного запуска)
- `grpcio-tools` для генерации Python-файлов из `.proto`

## Установка и запуск

### 1. Клонирование репозитория

```bash
 git clone https://github.com/Dima343316/grpc_test_python.git
cd grpc_test_python


### Установите зависимости для сервера и клиента из файла requirements.txt:

pip install --no-cache-dir -r requirements.txt

 ## Если файлы grpc_service_pb2.py и grpc_service_pb2_grpc.py отсутствуют, сгенерируйте их с помощью grpcio-tools. Для этого выполните следующую команду:

python -m grpc_tools.protoc -I./proto --python_out=./server --grpc_python_out=./server ./proto/grpc_service.proto

##Запуск сервера 
python server/grpc_server.py

## Запуск клиента 
python client/client.py



###Запуск с помощью Docker

1) открываем  проект командой - cd grpc_test_python;

2) вводим команду - docker-compose up --build 

3) Для того чтобы проверить данные в базе данных PostgreSQL, которая работает в Docker:

1) Подключитесь к контейнеру PostgreSQL с помощью команды - docker exec -it <container_name_or_id> psql -U <username> -d <database_name>

2) Выполните запрос в бд - SELECT * FROM <table_name>;

3) Должны получить информацию типа:

 id | PacketSeqNum | RecordSeqNum | PacketTimestamp |     Decimal1      |     Decimal2      |     Decimal3      |     Decimal4      | RecordTimestamp 
----+--------------+--------------+-----------------+-------------------+-------------------+-------------------+-------------------+-----------------
  1 |            0 |            0 |   1728306544857 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306544857
  2 |            0 |            1 |   1728306544857 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306544857
  3 |            0 |            2 |   1728306544857 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306544857
  4 |            0 |            3 |   1728306544857 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306544857
  5 |            0 |            4 |   1728306544857 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306544857
  6 |            1 |            0 |   1728306548872 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306548872
  7 |            1 |            1 |   1728306548872 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306548872
  8 |            1 |            2 |   1728306548872 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306548872
  9 |            1 |            3 |   1728306548872 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306548872
 10 |            1 |            4 |   1728306548872 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306548872
 11 |            2 |            0 |   1728306552892 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306552892
 12 |            2 |            1 |   1728306552892 | 1.100000023841858 | 2.200000047683716 | 3.299999952316284 | 4.400000095367432 |   1728306552892


Файлы конфигурации
server/config.json — используется для конфигурации gRPC сервера (порт и другие параметры).
client/client_config.json — содержит параметры для подключения gRPC клиента к серверу.



