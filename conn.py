class DbConn():
    def __init__(self, port, hostname, username, password):
        self.port = port
        self.hostname = hostname
        self.username = username
        self.password = password
    
    def show_conn(self):
        print(f"The connection is succesful: {self.port}, {self.hostname}, {self.username}, {self.password}")

    
dbConn = DbConn(443, "localhost", "admin", "admin123")
dbConn.show_conn()
