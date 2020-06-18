


class SpecsSerializer():

    data_list = []
    
    def __init__(self, input_list, freq_level):
        for input in input_list:
            data_dict = {}
            if(float(input[3]) >= freq_level):
                data_dict["spec_key"] = input[0]
                data_dict["spec_values"] = input[1].split(",")
                self.data_list.append(data_dict)

    def data(self):
        return {"filters" : self.data_list}


