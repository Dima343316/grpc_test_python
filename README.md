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
cd grpc_python_server


### Установите зависимости для сервера и клиента из файла requirements.txt:

pip install --no-cache-dir -r requirements.txt

 ## Если файлы grpc_service_pb2.py и grpc_service_pb2_grpc.py отсутствуют, сгенерируйте их с помощью grpcio-tools. Для этого выполните следующую команду:

python -m grpc_tools.protoc -I./proto --python_out=./server --grpc_python_out=./server ./proto/grpc_service.proto

##Запуск сервера 
python server/grpc_server.py

## Запуск клиента 
python client/client.py


##Запуск с помощью Docker

docker-compose up --build
docker-compose run grpc_client

Файлы конфигурации
server/config.json — используется для конфигурации gRPC сервера (порт и другие параметры).
client/client_config.json — содержит параметры для подключения gRPC клиента к серверу.



