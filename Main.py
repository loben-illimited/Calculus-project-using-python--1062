from population_api import *
from Malthus_Country import *
import pylab
import math

def main():
    '''
    人口增長推測
    Author: Lo Ben (loben@illimited.cf)
    '''

    info = "人口增長推測 \nAuthor: Lo Ben (loben@illimited.cf) \n"
    print(info)

    feature = "1. 利用Malthus推算國家人口 \n2. 輸出實際人口數量 \n3. 輸出所有地區的人口數量 \n4. 分別輸出Malthus和實際人口數據及圖形 \n5. 結合feature4，將所有數據儲存在html檔案裏面 \n>>> "
    selection = input(feature)

    if int(selection) == 1:
        feature1()
    elif int(selection) == 2:
        feature2()
    elif int(selection) == 3:
        feature3()
    elif int(selection) == 4:
        feature4()
    elif int(selection) == 5:
        pass

def feature5():
    pass

def saveImg(data, country):
    #covert dict to list
    cal_xs, cal_ys = [], []
    real_xs, real_ys = [], []
    for i in data[0]:
        cal_xs.append(i)
        cal_ys.append(data[0][i])
    for j in data[1]:
        real_xs.append(j)
        real_ys.append(data[1][j])
    #save figure
    grap = pylab
    grap.clf()
    grap.title(country)
    grap.plot(cal_xs, cal_ys, "b")
    grap.plot(real_xs, real_ys, "#FFA500")
    grap.savefig("temp/"+str(country))


def standard_deviation_of_compare(data_, real_population):
    sn = 0
    temp = 0

    data_list = []
    real_population_list = []

    #convert dict to list
    for a in data_.values():
        data_list.append(a)
    for b in real_population.values():
        real_population_list.append(b)
    try:
        for a in range(len(data_list)):
            temp += math.pow(real_population_list[a] - data_list[a], 2)
        sn = math.sqrt(temp/len(data_)-1)
    except:
        sn = None
    return sn

def feature1():
    _input = input_country()
    info = "輸入開始年份及結束年份"
    print(info)

    while(True):
        _begin = int(input("開始年份： "))
        _end = int(input("結束年份： "))
        if _begin < _end:
            break
        else:
            print("輸入錯誤，請重新輸入")

    #Malthus Calculate
    print("\n\n使用Malthus計算出的數據：")
    malthus_model = []
    for n in _input:
        malthus_model.append(Malthus_Country(n).get_interval_population(_begin, _end))
    index = 0
    counter = 0
    for i in malthus_model:
        Malthus_xs, Malthus_ys = [], []
        print(_input[index], ":")
        for j in i:
            Malthus_xs += [j]
            Malthus_ys += [i[j]]
            print(j, ": ", i[j], end = "\t\t\t")
            if counter > 2:
                print()#LF
                counter = 0
            counter += 1
        print("\n")
        pylab.title("use malthus model calculate "+_input[index]+" population")
        pylab.plot(Malthus_xs, Malthus_ys)
        pylab.show()
        index += 1

def feature2():
    _input = input_country()
    print(_input)
    info = "輸入開始年份及結束年份"
    print(info)

    while(True):
        _begin = int(input("開始年份： "))
        _end = int(input("結束年份： "))
        if _begin < _end:
            break
        else:
            print("輸入錯誤，請重新輸入")
    #Get data from website
    print("\n\n實際求出的數據：")
    population_api_result = []
    for n in _input:
        population_api_result.append(population_api(n).population_of_year_interval(_begin, _end))
    index = 0
    counter = 0
    for i in population_api_result:
        population_xs, popylation_ys = [], []
        print(_input[index], ":")
        for j in i:
            population_xs += [j]
            popylation_ys += [i[j]]
            print(j, ": ", i[j], end = "\t\t\t")
            if counter > 2:
                print()#LF
                counter = 0
            counter += 1
        print("\n")
        pylab.title("real "+_input[index]+" population")
        pylab.plot(population_xs, popylation_ys)
        pylab.show()
        index += 1

def feature3():
    
    info = "這個選項可以把所有國家的人口數量及以Malthus推算的人口數量畫出，並儲存在 .\\temp 裏面 \n而圖中藍色線為真實人口數量，而燈色線則為利用Malthus推測的人口數量"
    print(info)

    #檢查開始和結束時間上時是否有logic error
    while(True):
        _begin = int(input("開始年份： "))
        _end = int(input("結束年份： "))
        if _begin < _end:
            break
        else:
            print("輸入錯誤，請重新輸入")
    
    all_countries = population_api(None).all_countries()
    data = {} #store country all data
    for country in all_countries:
        #malthus_model
        malthus_model = Malthus_Country(country).get_interval_population(_begin, _end)
        #real population
        real_population = population_api(country).population_of_year_interval(_begin, _end)
        
        standard_deviation_of_compare(malthus_model, real_population)

        #data
        data = [malthus_model, real_population, standard_deviation_of_compare(malthus_model, real_population)]
        saveImg(data, country)
    
    #for test only
    #print(data)
    

def feature4():
    _input = input_country()
    info = "輸入開始年份及結束年份，並輸出以Malthus計算與實際人口數量的圖形"
    print(info)

    while(True):
        _begin = int(input("開始年份： "))
        _end = int(input("結束年份： "))
        if _begin < _end:
            break
        else:
            print("輸入錯誤，請重新輸入")

    #Malthus Calculate
    print("\n\n使用Malthus計算出的數據：")
    malthus_model = []
    for n in _input:
        malthus_model.append(Malthus_Country(n).get_interval_population(_begin, _end))
    index = 0
    counter = 0
    for i in malthus_model:
        Malthus_xs, Malthus_ys = [], []
        print(_input[index], ":")
        for j in i:
            Malthus_xs += [j]
            Malthus_ys += [i[j]]
            print(j, ": ", i[j], end = "\t\t\t")
            if counter > 2:
                print()#LF
                counter = 0
            counter += 1
        print("\n")
        pylab.title("use malthus model calculate "+_input[index]+" population")
        pylab.plot(Malthus_xs, Malthus_ys)
        pylab.show()
        index += 1


    #Get data from website
    print("\n\n實際求出的數據：")
    population_api_result = []
    for n in _input:
        population_api_result.append(population_api(n).population_of_year_interval(_begin, _end))
    index = 0
    counter = 0
    for i in population_api_result:
        population_xs, popylation_ys = [], []
        print(_input[index], ":")
        for j in i:
            population_xs += [j]
            popylation_ys += [i[j]]
            print(j, ": ", i[j], end = "\t\t\t")
            if counter > 2:
                print()#LF
                counter = 0
            counter += 1
        print("\n")
        pylab.title("real "+_input[index]+" population")
        pylab.plot(population_xs, popylation_ys)
        pylab.show()
        index += 1

def input_country():
    while True:    
        all_countries = list_all_coutries() #list all countries

        country = input("請輸入上表中的國家: （例如： Swaziland, Thailand, Canda 或者 對應國家的數字編號如： 100, 102） \n >>> ")
        input_list = country.split(",")

        if(is_input_valid(all_countries, input_list)):
            break
        else:
            print("輸入錯誤，請重新輸入。 你的輸入是：", input_list)
    
    index = 0
    for n in input_list:
        n = n.strip()
        if n.isnumeric():
            input_list[index] = all_countries[int(n)]
        index += 1
    return input_list


def list_all_coutries():
    all_countries = population_api(None).all_countries()
    index, i = 1, 0 #counter
    for n in all_countries:
        print(index, n, sep = ": ", end="\t\t\t")
        index += 1
        i += 1
        if (i > 1):
            print() #LF
            i = 0
    return all_countries

def is_input_valid(all_countries, input_list):
    for n in input_list:
        n = n.lstrip() #remove left space
        a = n.strip() #remove all space
        if a.isnumeric():
            if int(a) <= len(all_countries) and int(a) > 0: #is input number between index
                pass
            else:
                return False
                break
        elif not n.isnumeric() and n not in all_countries: #is input string in the all countries
            return False
            break
    return True

if __name__ == "__main__":
    main()