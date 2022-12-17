from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0.05, 0.1)

    def on_start(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['statusCode']

        print(request_id)

    @task
    def index(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['statusCode']

        print(request_id)
