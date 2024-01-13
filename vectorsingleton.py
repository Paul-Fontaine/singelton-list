class VectorSingleton(list):
    # static attribute
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if VectorSingleton.__instance is not None:
            raise Exception("This class is a singleton!")  # you can't have two instances of a singleton
        else:
            list.__init__(self)
            VectorSingleton.__instance = self

    @staticmethod
    def get_instance():
        if VectorSingleton.__instance is None:
            VectorSingleton()
        return VectorSingleton.__instance


def test_singleton():
    sglt_list1 = VectorSingleton.get_instance()
    sglt_list2 = VectorSingleton()

    assert sglt_list1 is sglt_list2


if __name__ == "__main__":
    test_singleton()
