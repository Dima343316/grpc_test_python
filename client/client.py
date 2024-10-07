import json
import time
from grpc_client import GrpcClient
import os
# Load configuration from client_config.json


current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, 'cleint_config.json')

# Load configuration from cleint_config.json
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    total_packets = config.get('TotalPackets')
    records_in_packet = config.get('RecordsInPacket')
    time_interval = config.get('TimeInterval')
    grpc_server_addr = config.get('gRPCServerAddr')
    grpc_server_port = config.get('gRPCServerPort')


def main():
    # Создаем gRPC клиента
    client = GrpcClient(grpc_server_addr, grpc_server_port)

    # Отправляем пакеты данных
    for packet_num in range(total_packets):
        packet_data = client.create_packet(records_in_packet, packet_num)

        client.send_packet(packet_data)
        print(f"Sent packet {packet_num}")
        time.sleep(time_interval)


if __name__ == '__main__':
    main()
