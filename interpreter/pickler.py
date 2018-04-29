from pickle import dumps
# from unpickler import Unpickler
# from DB_Local import DBLocal
# from collections import namedtuple


# Wesley
class Pickler:
    # Wesley
    @staticmethod
    def pickle_dictionary_values(dictionary):
        """
        Will take a dictionary containing dictionary values and return a dictionary with pickled values, keys are
        maintained
        :param dictionary:
        :return: dictionary{{key: value(pickled)}}
        >>>Pickler.pickle_dictionary_values({1: {"asdfdsafdsaf"}})
        """
        pickled_dict = dict()
        for key, value in dictionary.items():
            pickled_dict[key] = dumps(value)
        return pickled_dict



