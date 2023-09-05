from http.server import HTTPServer, BaseHTTPRequestHandler

# class Handler(BaseHTTPRequestHandler):
#     def do_GET(self):      
#         self.send_response(200)
#         self.send_header('content-type', 'text/hmtl')
#         self.end_headers()
#         self.wfile.write('Hola Mundo!!!'.encode())

# PORT = 8000
# servidor = HTTPServer(('localhost', PORT), Handler)
# print(f'Servidor conectado al puerto {PORT}')
# servidor.serve_forever()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/landing.html'
        try:
            archivo_abrir = open(self.path[1:]).read()
            self.send_response(200)
        except:
            archivo_abrir = 'Archivo no encontrado'
            self.send_response(404)
            
        self.end_headers()
        self.wfile.write(bytes(archivo_abrir, 'UTF-8'))

PORT = 8000
servidor = HTTPServer(('localhost', PORT), Handler)
print(f'Servidor conectado al puerto {PORT}')
print("Servidor levantado mediante http.server")
servidor.serve_forever()

