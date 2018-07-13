import sys

input_file = sys.argv[1] #supplier_data.csv
output_file = sys.argv[2] #output_files/1output.csv

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(', '.join(map(str, header_list)) + '\n')
                        #','.join(header_list)
        for row in filereader:
            row_list = row.split(',')
            print(row_list)
            filewriter.write(', '.join(map(str, row_list)))
