from locust import task
from LoadTests import settings
from LoadTests.authentication.session import SessionAuthUser


class WebsiteUser(SessionAuthUser):

    def __init__(self, environment):
        super().__init__(
            username=settings.USERNAME,
            password=settings.PASSWORD,
            environment=environment,
        )
    
    @task
    def index_page(self):
        self.client.get("/")
