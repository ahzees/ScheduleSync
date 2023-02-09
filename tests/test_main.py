import requests  # type: ignore


class Test:
    def test_module(self):
        import schedulesync

    def test_import(self):
        from schedulesync import core

    def test_server(self):
        url = "http://127.0.0.1:8000"
        response = requests.get(url, timeout=1.50)

        assert response.status_code < 500

    def test_employee_list(self):
        url = "http://127.0.0.1:8000/employee"
        response = requests.get(url, timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_employee(self):
        url = "http://127.0.0.1:8000/employee/1"
        response = requests.get(url, timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_occupation_list(self):
        url = "http://127.0.0.1:8000/occupation"
        response = requests.get(url, timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_occupation(self):
        url = "http://127.0.0.1:8000/occupation/1"
        response = requests.get(url, timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0
