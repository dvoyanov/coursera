import asyncio

class WrongCommand(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):

    DB = {}
    ANSWER_OK = "ok\n\n"

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        data_list = [d.strip() for d in data.split(" ")]
        print(data_list)
        try:
            if data_list[0] == "get" and len(data_list) == 2:
                answer = self.get(data_list[1])
            elif data_list[0] == "put" and len(data_list) == 4:
                answer = self.put(data_list[1:])
            else:
                raise WrongCommand
        except WrongCommand:
            answer = "error\nwrong command\n\n"
        return answer

    def get(self, data):
        answer = ""
        if data == "*":
            for key in ClientServerProtocol.DB:
                for value, timestamp in ClientServerProtocol.DB[key]:
                    answer += "{} {} {}\n".format(key, value, timestamp)
        elif data in ClientServerProtocol.DB:
            for value, timestamp in ClientServerProtocol.DB[data]:
                answer += "{} {} {}\n".format(data, value, timestamp)
        return "ok\n" + answer + "\n"

    def put(self, data):
        try:
            key = data[0]
            value = float(data[1])
            timestamp = int(data[2])
            if not key in ClientServerProtocol.DB:
                ClientServerProtocol.DB[key] = []
            for value_db, timestamp_db in ClientServerProtocol.DB[key]:
                if int(timestamp_db) == timestamp:
                    ClientServerProtocol.DB[key].remove((value_db, 
                        timestamp_db))
            ClientServerProtocol.DB[key].append((value, timestamp))
        except ValueError:
            raise WrongCommand
        return ClientServerProtocol.ANSWER_OK


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    
    server = loop.run_until_complete(coro)
    
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    run_server("127.0.0.1", "8181")
