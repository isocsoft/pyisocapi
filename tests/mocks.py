class MockableResponse:
    def __init__(self, json_data: dict, status_code: int) -> None:
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_valid_request(*args, **kwargs) -> MockableResponse:
    return MockableResponse(
        json_data={
            "error": "",
            "message": "Successfully retrieved data",
            "success": True,
            "data": {"mocked": True},
        },
        status_code=200,
    )
