from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(0.05, 0.1)

    def on_start(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "7014090407",
            "ccode": "+91"
        })

        print(response)
        

    @task
    def index(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "7014090407",
            "ccode": "+91"
        })
        print(response)
        
