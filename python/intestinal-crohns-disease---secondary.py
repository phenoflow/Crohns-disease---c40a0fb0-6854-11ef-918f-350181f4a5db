# phekb, 2024.

import sys, csv, re

codes = [{"code":"1569611","system":"ICD10CM"},{"code":"1569613","system":"ICD10CM"},{"code":"1569615","system":"ICD10CM"},{"code":"45533598","system":"ICD10CM"},{"code":"45533601","system":"ICD10CM"},{"code":"45557653","system":"ICD10CM"},{"code":"45567306","system":"ICD10CM"},{"code":"45576986","system":"ICD10CM"},{"code":"45596325","system":"ICD10CM"},{"code":"45596326","system":"ICD10CM"},{"code":"45596327","system":"ICD10CM"},{"code":"45601172","system":"ICD10CM"},{"code":"45601174","system":"ICD10CM"},{"code":"1569611","system":"ICD10CM"},{"code":"45533598","system":"ICD10CM"},{"code":"45601172","system":"ICD10CM"},{"code":"45557653","system":"ICD10CM"},{"code":"1569613","system":"ICD10CM"},{"code":"45576986","system":"ICD10CM"},{"code":"45596325","system":"ICD10CM"},{"code":"45596326","system":"ICD10CM"},{"code":"1569615","system":"ICD10CM"},{"code":"45596327","system":"ICD10CM"},{"code":"45567306","system":"ICD10CM"},{"code":"45601174","system":"ICD10CM"},{"code":"45533601","system":"ICD10CM"},{"code":"44820945","system":"ICD10CM"},{"code":"44825522","system":"ICD10CM"},{"code":"44827872","system":"ICD10CM"},{"code":"44827872","system":"ICD10CM"},{"code":"44820945","system":"ICD10CM"},{"code":"44825522","system":"ICD10CM"},{"code":"195575","system":"ICD10CM"},{"code":"195585","system":"ICD10CM"},{"code":"4212991","system":"ICD10CM"},{"code":"4212992","system":"ICD10CM"},{"code":"4246693","system":"ICD10CM"},{"code":"4264850","system":"ICD10CM"},{"code":"46269878","system":"ICD10CM"},{"code":"46269883","system":"ICD10CM"},{"code":"46269888","system":"ICD10CM"},{"code":"46274073","system":"ICD10CM"},{"code":"195585","system":"ICD10CM"},{"code":"195575","system":"ICD10CM"},{"code":"4264850","system":"ICD10CM"},{"code":"4246693","system":"ICD10CM"},{"code":"4212991","system":"ICD10CM"},{"code":"4212992","system":"ICD10CM"},{"code":"46274073","system":"ICD10CM"},{"code":"46269878","system":"ICD10CM"},{"code":"46269883","system":"ICD10CM"},{"code":"46269888","system":"ICD10CM"},{"code":"1569611","system":"ICD10CM"},{"code":"1569613","system":"ICD10CM"},{"code":"1569615","system":"ICD10CM"},{"code":"45533598","system":"ICD10CM"},{"code":"45533601","system":"ICD10CM"},{"code":"45557653","system":"ICD10CM"},{"code":"45567306","system":"ICD10CM"},{"code":"45576986","system":"ICD10CM"},{"code":"45596325","system":"ICD10CM"},{"code":"45596326","system":"ICD10CM"},{"code":"45596327","system":"ICD10CM"},{"code":"45601172","system":"ICD10CM"},{"code":"45601174","system":"ICD10CM"},{"code":"1569611","system":"ICD10CM"},{"code":"45533598","system":"ICD10CM"},{"code":"45601172","system":"ICD10CM"},{"code":"45557653","system":"ICD10CM"},{"code":"1569613","system":"ICD10CM"},{"code":"45576986","system":"ICD10CM"},{"code":"45596325","system":"ICD10CM"},{"code":"45596326","system":"ICD10CM"},{"code":"1569615","system":"ICD10CM"},{"code":"45596327","system":"ICD10CM"},{"code":"45567306","system":"ICD10CM"},{"code":"45601174","system":"ICD10CM"},{"code":"45533601","system":"ICD10CM"},{"code":"44820945","system":"ICD10CM"},{"code":"44825522","system":"ICD10CM"},{"code":"44827872","system":"ICD10CM"},{"code":"44827872","system":"ICD10CM"},{"code":"44820945","system":"ICD10CM"},{"code":"44825522","system":"ICD10CM"},{"code":"195575","system":"ICD10CM"},{"code":"195585","system":"ICD10CM"},{"code":"4212991","system":"ICD10CM"},{"code":"4212992","system":"ICD10CM"},{"code":"4246693","system":"ICD10CM"},{"code":"4264850","system":"ICD10CM"},{"code":"46269878","system":"ICD10CM"},{"code":"46269883","system":"ICD10CM"},{"code":"46269888","system":"ICD10CM"},{"code":"46274073","system":"ICD10CM"},{"code":"195585","system":"ICD10CM"},{"code":"195575","system":"ICD10CM"},{"code":"4264850","system":"ICD10CM"},{"code":"4246693","system":"ICD10CM"},{"code":"4212991","system":"ICD10CM"},{"code":"4212992","system":"ICD10CM"},{"code":"46274073","system":"ICD10CM"},{"code":"46269878","system":"ICD10CM"},{"code":"46269883","system":"ICD10CM"},{"code":"46269888","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('crohns-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["intestinal-crohns-disease---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["intestinal-crohns-disease---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["intestinal-crohns-disease---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
