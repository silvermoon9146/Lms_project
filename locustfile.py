from locust import HttpUser, task, between

class BookApiUser(HttpUser):
    wait_time = between(1,3)

    @task
    def list_books(self):
        self.client.get('/blog/api/books/')

    @task
    def viewset_book_list(self):
        self.client.get('/blog/api/viewset/books/')

    @task
    def create_book(self):
        payload = {
            'title' : 'world war II',
            'author' : 1
        }

        headers = {
            'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkzNjIxOTgyLCJpYXQiOjE3OTM1MzU1ODIsImp0aSI6IjI2ZjgwYzA3NGU3MjQxYWJiODI5YmI2NmJhMDJmOWMyIiwidXNlcl9pZCI6IjE1IiwiaWQiOjE1LCJmaXJzdF9uYW1lIjoiXHUwNjM5XHUwNjQ0XHUwNmNjIiwibGFzdF9uYW1lIjoiXHUwNjI3XHUwNjQ0XHUwNjQ3IFx1MDY0OFx1MDYzMVx1MDYyZlx1MDZjYyBcdTA2MmVcdTA2MjdcdTA2NDZcdTA2Y2MiLCJpc19zdGFmZiI6ZmFsc2UsInBob25lIjoiMDkxMjM0NTY3ODkifQ.XaAMYVCTvkN7hvRiC1GrEVLUqefHcrzz0Gk9OIBTpEU'
        }

        self.client.post('/blog/api/viewset/books/', json=payload, headers=headers)