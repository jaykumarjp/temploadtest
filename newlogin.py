class Test_1(TaskSet):

    @task(1)
    def users(self):
        response = self.client.post("/user/auth/v2/send-otp", json=
        {
        "title": "Silence of the Lambs",
        "body": "Thriller Book",
        "userId": 1
        }
        )
        json_var = response.json()
        request_id = json_var['title']

        print 'Post title is ' + request_id
