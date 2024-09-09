class Singleton(type):
    """
    Метакласс для работы с синглтонами
    """

    _intances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._intances:
            cls._intances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._intances[cls]
