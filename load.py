from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        response=self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['title']

        print('Post title is ' + request_id)

    @task
    def index(self):
        self.client.get("/")
