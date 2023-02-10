import os  # type: ignore

import requests  # type: ignore

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8000/")


class Test:
    def test_module(self):
        import schedulesync

    def test_import(self):
        from schedulesync import core

    def test_server(self):
        response = requests.get(BASE_URL, timeout=1.50)

        assert response.status_code < 500

    def test_employee_list(self):
        response = requests.get(os.path.join(BASE_URL, "employee"), timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_employee(self):
        response = requests.get(os.path.join(BASE_URL, "employee/1"), timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_occupation_list(self):
        response = requests.get(os.path.join(BASE_URL, "occupation"), timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0

    def test_occupation(self):
        response = requests.get(os.path.join(BASE_URL, "occupation/1"), timeout=1.50)

        assert response.status_code == 200

        response_dict = response.json()
        assert len(response_dict) != 0
