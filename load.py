from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    i=0
    wait_time = between(0.05, 0.1)

    def on_start(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['statusCode']

        print(str(i)+"---"+request_id)
        i=i+1

    @task
    def index(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['statusCode']

        print(str(i)+"---"+request_id)
        i=i+1
