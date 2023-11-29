import pandas as p

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from main.models import Organization, Sanction


def fill_orgs():
    file, dire = 'finOrgs.xlsx', ''
    fp = os.path.join(dire, file)
    if os.path.exists(fp):
        df = p.read_excel(fp)
        for name in df.iterrows():
            x = name[1].tolist()
            Organization.objects.create(name=x[0], first_owner=x[1], board_of_directors=x[2],
                                        chairman_of_the_board=x[3], members_of_the_board=x[4],
                                        director=x[5], chief_accountant=x[6], BIN=x[7],
                                        address=x[8], number=x[9], mail=x[10], site=x[11], license=x[12],
                                        branches=x[13])
        print('filled orgs')


def fill_sancs():
    print('sssan')
    file, dire = 'Санкции и меры воздействия.xlsx', ''
    fp = os.path.join(dire, file)
    if os.path.exists(fp):
        df = p.read_excel(fp)
        for name in df.iterrows():
            x = name[1].tolist()
            Sanction.objects.create(name=x[0], type=x[1], date=x[2],
                                        decision_number=x[3], type_of_recovery=x[4],
                                        type_of_penalty=x[5], imposed_penalty=x[6],
                                        essence_of_violation=x[7],
                                        period_of_execution=x[8], article=x[9],
                                        note=x[10], type_npa=x[11], department_name=x[12]
                                    )
        print('filled sancs')


if __name__ == "__main__":
    fill_orgs()
    fill_sancs()
