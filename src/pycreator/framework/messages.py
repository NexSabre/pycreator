class Messages:
    @staticmethod
    def error(message):
        print(f"ERRO :: {message}")

    @staticmethod
    def warn(message):
        print(f"WARN :: {message}")

    @staticmethod
    def info(message):
        print(f"INFO :: {message}")

    @staticmethod
    def ok(message):
        print(f" OK  :: {message}")

    @staticmethod
    def clean(message):
        print(f"     :: {message}")
