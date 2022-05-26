class OrderManager:

    def get_brand(self, data):
        return [dic.keys() for dic in data]

    def response_depth_type(self, type, order_data_type):
        if type == "foodtype":
            return self.get_brand(order_data_type[type])

