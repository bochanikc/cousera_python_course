import socket
import time


class ClientError(Exception):
    def __init__(self, text):
        self.text = text


class Client:
    def __init__(self, host, port, timeout=None):
        self.sock = socket.socket()
        self.sock.settimeout(timeout)
        try:
            self.sock.connect((host, port))
        except socket.timeout:
            raise ClientError("Error")

    def __del__(self):
        self.sock.close()

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        try:
            self.sock.sendall(f"put {key} {value} {timestamp}\n".encode("utf8"))
        except socket.timeout:
            raise ClientError("Error")
        except socket.error as ex:
            raise ClientError("Error")

        data = self.sock.recv(1024)
        data = data.decode("utf8")
        self.parse_put(data)

    def get(self, key):
        try:
            self.sock.sendall(f"get {key}\n".encode("utf8"))
        except socket.timeout:
            raise ClientError("Error")
        except socket.error as ex:
            raise ClientError("Error")

        data = self.sock.recv(1024)
        data = data.decode("utf8")
        if key == "*":
            return self.get_all(data)
        info_dict = self.parse_get(data)
        return info_dict

    def get_all(self, data):
        if data == 'ok\n\n':
            return {}
        elif data == '':
            raise ClientError("Error")
        else:
            data = data.split("\n")
            if data[0] == 'error':
                raise ClientError("Error")
            elif data[0] == 'ok':
                info_dict = dict()
                data = data[1:len(data) - 2]
                count = 0
                check = None
                for i in data:
                    i = i.split()
                    if len(i) != 3:
                        raise ClientError("Error")
                    key = i[0]
                    check = i[0]
                    if count == 0:
                        info_dict[key] = tuple(i[1:len(i) + 1])
                        count += 1
                        continue
                    elif info_dict.get(key) is not None:
                        info_dict[key] += tuple(i[1:len(i) + 1])
                        count += 1
                    else:
                        info_dict[key] = tuple(i[1:len(i) + 1])
                        count += 1
                return info_dict

    def parse_get(self, data):
        if data == 'ok\n\n':
            return {}
        elif data == '':
            raise ClientError("Error")
        else:
            data = data.split("\n")
            if data[0] == 'error':
                raise ClientError("Error")
            elif data[0] == 'ok':
                info_dict = dict()
                data = data[1:len(data) - 2]
                count = 0
                check = None
                for i in data:
                    i = i.split()
                    if len(i) != 3:
                        raise ClientError("Error")
                    elif check != i[0] and check is not None:
                        raise ClientError("Error")
                    key = i[0]
                    check = i[0]
                    if count == 0:
                        info_dict[key] = tuple(i[1:len(i) + 1])
                        count += 1
                        continue
                    elif info_dict.get(key) is not None:
                        info_dict[key] += tuple(i[1:len(i) + 1])
                        count += 1
                    else:
                        info_dict[key] = tuple(i[1:len(i) + 1])
                        count += 1
                return info_dict

    def parse_put(self, data):
        if data == 'ok\n\n':
            pass
        else:
            raise ClientError("Error")
