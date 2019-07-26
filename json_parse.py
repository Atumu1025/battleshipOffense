# To read the data in each json request ->
# Score = data[linenumber]['TeamB'/'TeamA']['score']
# Shots = data[linenumber]['TeamB'/'TeamA']['shots']
# Layout = data[linenumber]['TeamB'/'TeamA']['layout']


import json
import time 

def read_json(filename):
    data = []
    with open(filename) as f:
        for line in f:
            line=line.split('\n')
            data.append(json.loads(line[0]))
    return data

def create_dataset(data):
    dataset=list()
    for line in data:

        # for teamB
        i=0
        double_check=list()
        while i < len(line['TeamB']['shots']):
            if line['TeamA']['layout'][line['TeamB']['shots'][i]['x']][line['TeamB']['shots'][i]['y']]==1:
                if [line['TeamB']['shots'][i]['x'],line['TeamB']['shots'][i]['y']] not in double_check:
                    data_str_x =str()
                    data_str_y =str()
                    for coordinate in range(10):
                        if(coordinate == line['TeamB']['shots'][i]['x']):
                            data_str_x= data_str_x+'1,'
                        else:
                            data_str_x= data_str_x+'0,'
                        if(coordinate == line['TeamB']['shots'][i]['y']):
                            data_str_y= data_str_y+'1,'
                        else:
                            data_str_y= data_str_y+'0,'
                    data_str=data_str_x+data_str_y+'1'
                    dataset.append(data_str)
                    double_check.append([line['TeamB']['shots'][i]['x'],line['TeamB']['shots'][i]['y']])
            
            else:
                data_str_x =str()
                data_str_y =str()
                for coordinate in range(10):
                    if(coordinate == line['TeamB']['shots'][i]['x']):
                        data_str_x= data_str_x+'1,'
                    else:
                        data_str_x= data_str_x+'0,'
                    if(coordinate == line['TeamB']['shots'][i]['y']):
                        data_str_y= data_str_y+'1,'
                    else:
                        data_str_y= data_str_y+'0,'
                data_str=data_str_x+data_str_y+'0'
                dataset.append(data_str)

    
            i+=1
        
        # for teamA
        i=0
        double_check=list()
        while i < len(line['TeamA']['shots']):
            if line['TeamB']['layout'][line['TeamA']['shots'][i]['x']][line['TeamA']['shots'][i]['y']]==1:
                if [line['TeamA']['shots'][i]['x'],line['TeamA']['shots'][i]['y']] not in double_check:
                    data_str_x =str()
                    data_str_y =str()
                    for coordinate in range(10):
                        if(coordinate == line['TeamA']['shots'][i]['x']):
                            data_str_x= data_str_x+'1,'
                        else:
                            data_str_x= data_str_x+'0,'
                        if(coordinate == line['TeamA']['shots'][i]['y']):
                            data_str_y= data_str_y+'1,'
                        else:
                            data_str_y= data_str_y+'0,'
                    data_str=data_str_x+data_str_y+'1'
                    dataset.append(data_str)
                    double_check.append([line['TeamA']['shots'][i]['x'],line['TeamA']['shots'][i]['y']])
            else:
                data_str_x =str()
                data_str_y =str()
                for coordinate in range(10):
                    if(coordinate == line['TeamB']['shots'][i]['x']):
                        data_str_x= data_str_x+'1,'
                    else:
                        data_str_x= data_str_x+'0,'
                    if(coordinate == line['TeamB']['shots'][i]['y']):
                        data_str_y= data_str_y+'1,'
                    else:
                        data_str_y= data_str_y+'0,'
                data_str=data_str_x+data_str_y+'0'
                dataset.append(data_str)
            
            i+=1

    return dataset
        # pass

def write_data_into_csv(dataset):
    f = open('data_set.csv','w')
    f.write("x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,hit\n")
    for line in dataset:
        f.write(line)
        f.write('\n')
    f.close() 

if __name__ =='__main__':
    data = read_json("sample.json")
    processed_data = create_dataset(data)
    write_data_into_csv(processed_data)




        