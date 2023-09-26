def parse_data(data):
    x = data.replace("0"," ")
    data_list = x.split()
    data_dict = {}
    data_dict["first_name"] = data_list[0]
    data_dict["last_name"] = data_list[1]
    data_dict["id"] = data_list[2]
    return data_dict
    
    
data = input("Enter Data : ")
data_dict = parse_data(data)
print(data_dict)
