import re

def size_func(data:str) -> str:
    matches = re.findall("([0-9]+\.*[0-9]+)( )*(m2|km2|ft2|kvadratmeter)*",data)

    #Stops if no matches is found
    if(check_for_empty(matches)):
        return 'No matches'

    value = str(matches[0][0])
    unit= str(matches[0][2])

    #More cases could be added, if more exists
    if(unit == 'kvadratmeter'):
        unit = 'm2'
    output = "{\n  value: " + str(value) + ",\n  unit: '" + unit + "'\n}"
    return output

def price_func(data:str) -> str:
    value = re.findall(r'\d?[^\s?m]\d+(?:\.\d+)?', data)[0]
    term = re.findall(r'(((M|m)ånedlig)|(M|m)åned|(Å|å)r)',data)
    unit = re.findall(r'(m2|km2|ft2)',data)
    currency = re.findall(r'(kr|eur)',data)
    service = re.findall(r'(((eksl\.)|(inkl\.))\sdrift)',data)

    if(check_for_empty(unit)):
        unit = unit[0]
    else:
        unit = 'undefined'

    if(check_for_empty(currency)):
        currency = currency[0]
    else:
        currency = currency[0]

    #More cases could be added, for different types of valuta
    if(currency == 'kr'):
        currency = 'DKK'

    if(len(term) == 0):
        term = 'undefined'
    elif (term[0][0] == 'Månedlig' or term[0][0] == 'måned'):
        term = 'month'
    elif (term[0][0] == 'år' or term[0][0] == 'År'):
        term = 'year'

    if(len(service) == 0):
        service = 'undefined'
    elif(service[0][0] == 'inkl. drift'):
        service = 'true'
    elif(service[0][0] == 'eksl. drift'):
        service = 'false'

    #Remove punct so the numbers is consistent
    value = value.replace(".","")

    output = "{\n\tvalue: " + str(value) + ",\n\tterm: '" + term+ "',\n\tunit: '"+str(unit)+"',\n\tcurrency: '" + str(currency) + "',\n\twithService: " + str(service) + "\n}"

    return output

def contact_func(data:str) -> str:
    name = re.findall(r'([A-Z]+[a-z]+\s([A-Z][a-z]*(å|æ|ø)*[a-z]*\s*)*)',data)
    email = re.findall(r'([a-zA-Z]+@[a-zA-Z]*\.[a-zA-Z]+)',data)
    number = re.findall(r'(\+*(\d+\s*)+)',data)
    role = re.findall(r'([A-Z]*[a-z]*æ*å*ø*[a-z]*\-*\s)', data)
    role_combined = ''.join(role)

    if(len(name) ==  0):
        name= "undefined"
    else:
        name = name[0][0]
    print(name)

    if(len(email) == 0):
        email = 'undefined'
    else:
        email = email[0]

    if(len(number) == 0):
        number = 'undefinded'
    else:
        number = number[0][0].strip('\n')

    #Remove founed name from tole tag
    names = name.split(' ')
    for name_ in names:
        role_combined = role_combined.replace(name_, "")
        role_combined = role_combined.replace("dk", "")
        role_combined = role_combined.strip("\n")
    role = role_combined

    output = "{\n  name: '" + str(name) + "',\n  role: '" + role+ "',\n  phone: '"+str(number)+"'\n  email: '" + str(email) + "'\n}"
    return output

def check_for_empty(input_lst:list):
    if(len(input_lst) == 0):
        return False
    return True

# Takes file with testes on different lines in, outputs the results in output file
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
    #To run the functions only on one line uncommentet following and insert line:
    #print(size_func("input string"))
    #print(price_func("input string"))
    #print(contact_func("input string"))


if __name__ == "__main__":
    main()
