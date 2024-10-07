import grpc
import time
from proto import grpc_service_pb2
from proto.grpc_service_pb2_grpc import DataServiceStub
import random


class GrpcClient:
    def __init__(self, grpc_server_addr, grpc_server_port):
        # Устанавливаем канал для соединения с gRPC сервером
        self.channel = grpc.insecure_channel(f'{grpc_server_addr}:{grpc_server_port}')
        self.stub = DataServiceStub(self.channel)

    def generate_unique_packet_seq_num(self):
        """Генерирует уникальный номер пакета на основе временной метки и случайного числа."""
        return int(time.time() * 1000) + random.randint(0, 99999)

    def create_packet(self, records_in_packet, packet_seq_num):
        packet_timestamp = int(time.time() * 1000)  # Время в миллисекундах
        packet_data = []

        for i in range(records_in_packet):
            record_timestamp = int(time.time() * 1000)
            record_seq_num = packet_seq_num * 1000 + i    # Уникальный RecordSeqNum для каждой записи
            data_record = grpc_service_pb2.Data(
                RecordSeqNum=record_seq_num,
                Decimal1=1.1,
                Decimal2=2.2,
                Decimal3=3.3,
                Decimal4=4.4,
                RecordTimestamp=record_timestamp
            )
            packet_data.append(data_record)

        # Создаем пакет данных
        packet = grpc_service_pb2.Packet(
            PacketSeqNum=packet_seq_num,  # Уникальный номер пакета
            PacketTimestamp=packet_timestamp,
            NRecords=records_in_packet,
            PacketData=packet_data
        )

        return packet

    def send_packet(self, packet):
        """Отправляем пакет через gRPC сервис."""
        self.stub.SendPacket(packet)
        print(f"Sent packet {packet.PacketSeqNum} with {len(packet.PacketData)} records.")
