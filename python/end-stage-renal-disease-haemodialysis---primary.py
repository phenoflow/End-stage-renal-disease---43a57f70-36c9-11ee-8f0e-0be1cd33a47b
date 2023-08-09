# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14V2.00","system":"readv2"},{"code":"14V2.11","system":"readv2"},{"code":"4I29.00","system":"readv2"},{"code":"7L1A000","system":"readv2"},{"code":"7L1A100","system":"readv2"},{"code":"7L1A200","system":"readv2"},{"code":"7L1A400","system":"readv2"},{"code":"7L1A600","system":"readv2"},{"code":"8882.00","system":"readv2"},{"code":"Gy41.00","system":"readv2"},{"code":"SP0F.00","system":"readv2"},{"code":"SP0G.00","system":"readv2"},{"code":"TA02000","system":"readv2"},{"code":"Z919100","system":"readv2"},{"code":"Z919200","system":"readv2"},{"code":"Z919300","system":"readv2"},{"code":"Z91A.00","system":"readv2"},{"code":"ZV45100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('end-stage-renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["end-stage-renal-disease-haemodialysis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["end-stage-renal-disease-haemodialysis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["end-stage-renal-disease-haemodialysis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
