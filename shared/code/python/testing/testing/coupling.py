class Simulator:
    def __init__(self):
        self.api_client = APIClient()
        self.api_key = os.environ("API_KEY")

    def simulate(self):
        ...
