"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 80%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

schools = json.load(infile)

conference_schools = [372, 108, 107, 130]

# How many schools are in this file?
# print(len(schools))

# Print name of school, grad rate > 80% for women in the four conferences
print('Schools with women graduation rates greater than 80%\n')
for i in schools:
    # if school['NCAA'][''NAIA conference number football (IC2020)'] in conference_schools:
    for j in conference_schools:
        if j == int(i["NCAA"]['NAIA conference number football (IC2020)']):
            if i['Graduation rate  women (DRVGR2020)'] >= 80:
                print(i['instnm'])
                print('Women Grad Rate: ' +
                      str(i['Graduation rate  women (DRVGR2020)'])+'\n')

print('In-state students living off campusis greater than $50,000:\n')
for i in schools:
    for j in conference_schools:
        if j == int(i["NCAA"]['NAIA conference number football (IC2020)']):
            if i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] != None:
                if int(i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']) >= int(50000):
                    print(i['instnm'])
                    print('In-state cost to live off campus: $' +
                          str(i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']) + '\n')
