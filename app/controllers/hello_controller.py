from app.models.hello_model import HelloModel


class HelloController:
    def read_hello() -> HelloModel:
        return HelloModel(message="asds")
