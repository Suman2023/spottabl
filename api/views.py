import csv
from django.http import HttpResponse
from api.models import Registration,ClientUserInvite

# Create your views here.

def index(request):
    number_of_users_flexmoney = Registration.objects.filter(email__endswith='@flexmoney.in').count()
    number_of_users_spottabl = Registration.objects.filter(email__endswith='@spottabl.com').count()

    invited_from_spottabl_spottable = ClientUserInvite.objects.filter(inviter__endswith='@spottabl.com',client_code='spottabl').count()
    invited_from_spottabl_flexmoney = ClientUserInvite.objects.filter(inviter__endswith='@spottabl.com',client_code='flexmoney').count()

    accepted_spottable = ClientUserInvite.objects.filter(accepted=True,client_code='spottabl').count()
    accepted_flexmoney = ClientUserInvite.objects.filter(accepted=True,client_code='flexmoney').count()

    invited_from_spottable_user_spottable = len(ClientUserInvite.objects.raw("SELECT * from api_registration, api_clientuserinvite WHERE api_clientuserinvite.inviter = api_registration.email AND api_registration.email LIKE '%@spottabl.com'"))
    invited_from_spottable_user_flexmoney = len(ClientUserInvite.objects.raw("SELECT * from api_registration, api_clientuserinvite WHERE api_clientuserinvite.inviter = api_registration.email AND api_registration.email LIKE '%flexmoney.in'"))

    # return Response({
    #     "number_of_users_flexmoney":flexmoney_count,"number_of_users_spottablt":spottabl_count,
    #     "invited_from_spottabl_spottable":invited_from_spottabl_spottable,"invited_from_spottabl_flexmoney":invited_from_spottabl_flexmoney,
    #     "accepted_spottable":accepted_spottable,"accepted_flexmoney":accepted_flexmoney,
    #     "invited_from_spottable_user_spottable":invited_from_spottable_user_spottable,"invited_from_spottable_user_flexmoney":invited_from_spottable_user_flexmoney,
    #     })
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="response.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Client Code',
                    'Number of users on spottabl',
                    'Number of users invited from spottabl',
                    'Number of users who have accepted invite',
                    'Number of users invited from spottabl user',
                    ])
    writer.writerow(['Spottabl',number_of_users_spottabl,invited_from_spottabl_spottable,accepted_spottable,invited_from_spottable_user_spottable])
    writer.writerow(['flexmoney',number_of_users_flexmoney,invited_from_spottabl_flexmoney,accepted_flexmoney,invited_from_spottable_user_flexmoney])

    return response



def init(request):
    try:
        init_registration(request)
        init_client_user(request)
    except Exception as e:
        return HttpResponse("Unsucessful")
    return HttpResponse("Successful")


def init_registration(request):
    with open('./api/files/registrations.csv',newline='') as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        data.__next__()
        # print(data)
        for row in data:
            if row[1] == 'true':
                row[1] = True
            else:
                row[1] = False
            try:
                Registration.objects.create(email=row[0],enabled=row[1],registration_type=row[2],user_type=row[3])
            except Exception as e:
                pass

def init_client_user(request):
    with open('./api/files/clientuserinvites.csv',newline='') as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        data.__next__()
        # print(data)
        for row in data:
            if row[3] == 'true':
                row[3] = True
            else:
                row[3] = False
            try:
                ClientUserInvite.objects.create(email=row[0],client_code=row[1],user_type=row[2],accepted=row[3],role=row[4],inviter=row[5])
            except Exception as e:
                pass

