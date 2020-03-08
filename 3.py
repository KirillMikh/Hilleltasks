class SwitchConnector:

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._password = password
        self._login = login
        self._ip_address = ip_address
        self._mac_address = mac_address
        self._unit_name = unit_name



    @property
    def unit_name(self):
        return self._unit_name


    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


connection1 = SwitchConnector("switch1",66901,192_168_01_01,"admin",12345)
connection1.unit_name = "switchwww1"
print(connection1.password, connection1.mac_address)

print(connection1.__dict__)
connection1.login="user1"

print(connection1.login)





