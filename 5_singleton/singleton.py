class Singleton:
    unique_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.unique_instance:
            cls.unique_instance = super().__new__(cls, *args, **kwargs)
        return cls.unique_instance

    # Other methods
