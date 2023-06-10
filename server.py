from http.server import BaseHTTPRequestHandler
import os
import datetime
import json
# from socketserver import _RequestType, BaseServer
import time




def GetParam(requestParam):
    post_body_split = requestParam.split('&')

    param_dict = {}
    for param in post_body_split:
        param_split = param.split('=')
        param_dict[param_split[0]] = param_split[1]

    return param_dict


class Server(BaseHTTPRequestHandler):
    q1_di = 1



    def do_GET(self):
            if self.path == '/':
                # self.path = '/index.html'
                self.path = '/login.html'
            elif self.path == '/index.html':
                self.path = '/login.html'

            path, params = self.path.split(
                '?') if '?' in self.path else self.path, None

        # try:
            if path.startswith('/api'):
                if path == '/api/stt':
                    self.send_response(200)
                    self.end_headers()

                    # time.sleep(1)
                    # for i in range(5):
                    ct = datetime.datetime.now()
                    __class__.q1_di = (__class__.q1_di << 1) & 0xFF
                    if (__class__.q1_di == 0):
                        __class__.q1_di = 1

                    api_reponse = {
                        "ts": f"{ct}", 
                        "q1": {
                                'di': self.q1_di
                            }
                        }
                    self.wfile.write(json.dumps(api_reponse).encode())

                    return
                
                if path == '/api/log':
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'this is sample log')

                    return

            split_path = os.path.splitext(path)
            request_extension = split_path[1]
            if request_extension != ".py":
                # f = open(path[1:]).read()

                f = open(path[1:], 'rb').read()
                self.send_response(200)
                self.end_headers()

                # self.wfile.write(bytes(f, 'utf-8'))
                self.wfile.write(f)
            else:
                f = "File not found"
                self.send_error(404, f)
        # except:
        #     f = "File not found"
        #     self.send_error(404, f)

    def do_POST(self):
        # try:
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]
        if request_extension == ".py":
            f = "File not found"
            self.send_error(404, f)

            return

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len).decode()

        param_dict = GetParam(post_body)

        # if self.path == '/api/set/led':
        # param_dict = GetParam(params)
        # param_dict['']

        if self.path == '/index.html':
            if (param_dict['uname'] == '0') and (param_dict['psw'] == '1'):
                f = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.end_headers()

                # self.wfile.write(bytes(f, 'utf-8'))
                self.wfile.write(f)
            else:
                self.send_error(404, "Thong tin dang nhap khong chinh xac")

            return

        # except:
        #     f = "File not found"
        #     self.send_error(404,f)
