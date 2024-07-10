from LoadTests.authentication.interface import IAuthUser

class SessionAuthUser(IAuthUser):

    def login(self):
        self.client.post("/auth/login", json={"username": f"{self.username}", "password": f"{self.password}"})