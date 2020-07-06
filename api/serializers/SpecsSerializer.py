


class SpecsSerializer():

    data_list = []
    
    def __init__(self, input_list, freq_level):
        self.data_list = []
        for input in input_list:
            data_dict = {}
            if(float(input[3]) >= freq_level):
                data_dict["spec_key"] = input[0]
                data_dict["spec_values"] = input[1].split(",")
                self.data_list.append(data_dict)

    def data(self):
        res = self.data_list
        self.data_list = []
        return res
        


