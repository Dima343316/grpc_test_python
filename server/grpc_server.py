import grpc
from concurrent import futures
import json
from google.protobuf.empty_pb2 import Empty
from proto.grpc_service_pb2_grpc import DataServiceServicer, add_DataServiceServicer_to_server
from server.database import GRPCData, get_session
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем полный путь к файлу config.json
config_path = os.path.join(current_dir, 'config.json')

# Load configuration from cleint_config.json
with open(config_path, 'r') as config_file:
    config_data = json.load(config_file)  # Используем json.load для загрузки словаря из JSON-файла

    # Получаем нужные параметры из словаря
    grpc_port = config_data.get('gRPCServerPort')
    database_url = config_data.get('database_url')


# Create a new session
session = get_session()

class DataService(DataServiceServicer):
    def SendPacket(self, request, context):
        packet_seq_num = request.PacketSeqNum
        packet_timestamp = request.PacketTimestamp

        for i, record in enumerate(request.PacketData):
            new_data = GRPCData(
                PacketSeqNum=packet_seq_num,
                RecordSeqNum=i,
                PacketTimestamp=packet_timestamp,
                Decimal1=record.Decimal1,
                Decimal2=record.Decimal2,
                Decimal3=record.Decimal3,
                Decimal4=record.Decimal4,
                RecordTimestamp=record.RecordTimestamp
            )
            session.add(new_data)

        # Commit all changes to the database
        session.commit()

        return Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DataServiceServicer_to_server(DataService(), server)
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    print(f'gRPC server is running on port {grpc_port}')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
