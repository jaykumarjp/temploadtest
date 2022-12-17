from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })

    @task
    def about(self):
        self.client.get("/about/")
~                                            
