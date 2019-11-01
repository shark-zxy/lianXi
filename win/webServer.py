from multiprocessing import Process
import socket
import re

HTML_ROOT_DIR = "./html"


class HTTPServer():
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(5)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s,%s]已经接入" % client_address)
            client_process = Process(target=self.handle, args=(client_socket,))
            client_process.start()
            client_socket.close()
    def start_response(self):
        pass

    @staticmethod
    def handle(self,client_socket):
        global response_start_line, response_header, response_body
        recv_data = client_socket.recv(1024)
        print("recv_data:",recv_data)
        recv_lines = recv_data.splitlines()
        for line in recv_lines:
            print(line)
        recv_start_lines = recv_lines[0]
        print("*" * 10)
        print(recv_start_lines.decode("utf-8"))
        file_name = re.match(r"\w+ +(/[^ ]*)", recv_start_lines.decode("utf-8")).group(1)

        if file_name.endswith(".py"):
            try:
                m = __import__(file_name[1:-3])
            except EOFError:
                self.response_header = "HTTP/1.1 404 NOT FOUND \r\n"
                response_body = "This is not found"
            else:
                env = {}
                response_body = m.application(env,self.start_response)
            response = response_header + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/index.html"

            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                response_start_line = "HTTP/1.1  404 NOT FOUND \r\n"
                response_header = "Server: My Server"
                response_body = "This is not found"
            else:
                file_data = file.read()
                file.close()

                response_start_line = "HTTP/1.1 ./ 200 OK \r\n"
                response_header = "Server: My Server\r\n"
                response_body = file_data.decode("utf-8")
            response = response_start_line + response_header + "\r\n" + response_body
            print("response:", response)

        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()


def main():
    http_user = HTTPServer()
    http_user.bind(8080)
    http_user.start()


if __name__ == '__main__':
    main()
