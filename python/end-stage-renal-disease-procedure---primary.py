# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100693.0","system":"med"},{"code":"101124.0","system":"med"},{"code":"101736.0","system":"med"},{"code":"101756.0","system":"med"},{"code":"101912.0","system":"med"},{"code":"103429.0","system":"med"},{"code":"104049.0","system":"med"},{"code":"104050.0","system":"med"},{"code":"104201.0","system":"med"},{"code":"104586.0","system":"med"},{"code":"104630.0","system":"med"},{"code":"104719.0","system":"med"},{"code":"104905.0","system":"med"},{"code":"104960.0","system":"med"},{"code":"105328.0","system":"med"},{"code":"105436.0","system":"med"},{"code":"105724.0","system":"med"},{"code":"105742.0","system":"med"},{"code":"105760.0","system":"med"},{"code":"105811.0","system":"med"},{"code":"106301.0","system":"med"},{"code":"106620.0","system":"med"},{"code":"106720.0","system":"med"},{"code":"106866.0","system":"med"},{"code":"106975.0","system":"med"},{"code":"107000.0","system":"med"},{"code":"107082.0","system":"med"},{"code":"107188.0","system":"med"},{"code":"107220.0","system":"med"},{"code":"107260.0","system":"med"},{"code":"107746.0","system":"med"},{"code":"107752.0","system":"med"},{"code":"107900.0","system":"med"},{"code":"108116.0","system":"med"},{"code":"108213.0","system":"med"},{"code":"108423.0","system":"med"},{"code":"108437.0","system":"med"},{"code":"108699.0","system":"med"},{"code":"108759.0","system":"med"},{"code":"108785.0","system":"med"},{"code":"109135.0","system":"med"},{"code":"109455.0","system":"med"},{"code":"109809.0","system":"med"},{"code":"110051.0","system":"med"},{"code":"110072.0","system":"med"},{"code":"110095.0","system":"med"},{"code":"11553.0","system":"med"},{"code":"11745.0","system":"med"},{"code":"11773.0","system":"med"},{"code":"18774.0","system":"med"},{"code":"20073.0","system":"med"},{"code":"20196.0","system":"med"},{"code":"22252.0","system":"med"},{"code":"23773.0","system":"med"},{"code":"24361.0","system":"med"},{"code":"26862.0","system":"med"},{"code":"28158.0","system":"med"},{"code":"2994.0","system":"med"},{"code":"2996.0","system":"med"},{"code":"2997.0","system":"med"},{"code":"30709.0","system":"med"},{"code":"30756.0","system":"med"},{"code":"36442.0","system":"med"},{"code":"44422.0","system":"med"},{"code":"45160.0","system":"med"},{"code":"46145.0","system":"med"},{"code":"46438.0","system":"med"},{"code":"48057.0","system":"med"},{"code":"48639.0","system":"med"},{"code":"49028.0","system":"med"},{"code":"52123.0","system":"med"},{"code":"54990.0","system":"med"},{"code":"5504.0","system":"med"},{"code":"5911.0","system":"med"},{"code":"59315.0","system":"med"},{"code":"60446.0","system":"med"},{"code":"60498.0","system":"med"},{"code":"60743.0","system":"med"},{"code":"63038.0","system":"med"},{"code":"63488.0","system":"med"},{"code":"63502.0","system":"med"},{"code":"64828.0","system":"med"},{"code":"66705.0","system":"med"},{"code":"66714.0","system":"med"},{"code":"69266.0","system":"med"},{"code":"69760.0","system":"med"},{"code":"70874.0","system":"med"},{"code":"72004.0","system":"med"},{"code":"72336.0","system":"med"},{"code":"74905.0","system":"med"},{"code":"8037.0","system":"med"},{"code":"8330.0","system":"med"},{"code":"86419.0","system":"med"},{"code":"88597.0","system":"med"},{"code":"89924.0","system":"med"},{"code":"93366.0","system":"med"},{"code":"96133.0","system":"med"},{"code":"96184.0","system":"med"},{"code":"98364.0","system":"med"},{"code":"98888.0","system":"med"},{"code":"99692.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('end-stage-renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["end-stage-renal-disease-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["end-stage-renal-disease-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["end-stage-renal-disease-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
