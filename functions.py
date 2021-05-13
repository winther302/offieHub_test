import re

def size_func(data:str) -> str:
    matches = re.findall("([0-9]+\.*[0-9]+)( )*(m2|km2|ft2|kvadratmeter)*",data)
    value = str(matches[0][0])
    unit= str(matches[0][2])
    if(unit == 'kvadratmeter'):
        unit = "m2"
    output = "{\n  value: " + str(value) + ",\n  unit: '" + unit + "'\n}"
    return output

def price_func(data:str) -> str:
    value = re.findall(r'\d?[^\s?m]\d+(?:\.\d+)?', data)[0]
    term = re.findall(r'(((M|m)ånedlig)|(M|m)åned|(Å|å)r)',data)
    unit = re.findall(r'(m2|km2|ft2)',data)
    currency = re.findall(r'(kr|eur)',data)
    service = re.findall(r'(((eksl\.)|(inkl\.))\sdrift)',data)

    unit = check_for_empty(unit)
    currency = check_for_empty(currency)

    if(len(term) == 0):
        term = 'undefined'
    elif (term[0][0] == 'Månedlig' or term[0][0] == 'måned'):
        term = 'month'
    elif (term[0][0] == 'år' or term[0][0] == 'År'):
        term = 'year'

    if(currency == 'kr'):
        currency = 'DKK'

    if(len(service) == 0):
        service = 'undefined'
    elif(service[0][0] == 'inkl. drift'):
        service = 'true'
    elif(service[0][0] == 'eksl. drift'):
        service = 'false'

    value = value.replace(".","")
    output = "{\n\tvalue: " + str(value) + ",\n\tterm: '" + term+ "',\n\tunit: '"+str(unit)+"',\n\tcurrency: '" + str(currency) + "',\n\twithService: " + str(service) + "\n}"

    #print(service)
    return output

def check_for_empty(input_lst:list) -> str:
    result = ''
    if(len(input_lst) == 0):
        result = 'undefined'
    else:
        result = input_lst[0]
    return result


def contact_func(data:str) -> str:
    name = re.findall(r'([A-Z]+[a-z]+\s([A-Z][a-z]*(å|æ|ø)*[a-z]*\s*)*)',data)[0][0]
    email = re.findall(r'([a-zA-Z]+@[a-zA-Z]*\.[a-zA-Z]+)',data)
    print(email)
    number = re.findall(r'(\+*(\d+\s*)+)',data)
    role = 'undefined'
    if(len(email) == 0):
        email = 'undefined'
    else:
        email = email[0]

    if(len(number) == 0):
        number = 'undefinded'
    else:
        number = number[0][0].strip('\n')

    output = "{\n  name: '" + str(name) + "',\n  role: '" + role+ "',\n  phone: '"+str(number)+"'\n  email: '" + str(email) + "'\n}"
    return output

def make_output(input_file:str,output_file:str, func):
    with open(input_file,'r') as f:
        input = f.readlines()
    with open(output_file,'w')as f:
        for i,line in enumerate(input):
            f.write('Case ' + str(i)+': ' + line)
            out = func(line)
            f.write(out+'\n')

def main():
    make_output("size_test_out/size_function_test","size_test_out/size_func_out", size_func)
    make_output("price_test_out/price_func_test","price_test_out/price_func_out", price_func)
    make_output("contact_test_out/contact_func_test","contact_test_out/contact_func_out", contact_func)

if __name__ == "__main__":
    main()
