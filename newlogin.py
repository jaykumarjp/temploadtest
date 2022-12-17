from locust import HttpUser, between, task

class Test_1(1,2):

    @task(1)
    def users(self):
        response = self.client.post("/user/auth/v2/send-otp", {
            "mobile": "9999642347"
        })
        json_var = response.json()
        request_id = json_var['title']

        print('Post title is ' + request_id)
