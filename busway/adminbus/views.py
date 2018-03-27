from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'dashboard.html')


def userprofile(request,menu):
    if menu == 'dashboard':
        return render(request,'dashboard.html')
    elif menu == 'userprofile':
        return render(request,'user.html')
    elif menu == 'bookinghistory':
        return render(request,'table.html')
    elif menu == 'typography':
        return render(request,'typography.html')
    elif menu == 'maps':
        return render(request,'maps.html')
    elif menu == 'notifications':
        return render(request,'notifications.html')
    else:
        return render(request,'upgrade.html')

def login(request):
    return render(request,'login.html')
