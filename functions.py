
def size_func(data:str) -> str:
    value = 0
    unit = "unkown"
    output = "{\n  value: " + str(value) + ",\n  unit: '" + unit + "'\n}"
    return output

def price_func(data:str) -> str:
    pass

def contact_info_func(data:str) -> str:
    pass

def test_func(output:str, target:str):
    with open(target, 'r') as f:
        target_data = f.read()
    with open(output, 'r') as f:
        output_data = f.read()
    if(target_data == output_data):
        return True
    return False

def make_output(input_file:str,output_file:str, func):
    with open(input_file,'r') as f:
        input = f.readlines()
    with open(output_file,'w')as f:
        for line in input:
            out = func(line)
            f.write(out+"\n")



def main():
    make_output("size_function_test","size_func_out", size_func)

    print("Test of size function:")
    print("\tInput from size_function_test file,\n\tTarget in size_targe,\n\tOutput in size_func_out. \n\tResult: " + str(test_func("size_func_out", "size_target")))


if __name__ == "__main__":
    main()
