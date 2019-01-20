from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {
        'content':['For general inquiries:','St. Robert Catholic High School', '8101 Leslie St., Thornhill L3T 7P4',
                   'Phone: 905-889-4982', 'Attendance: 905-889-6149', 'Email: srh@ycdsb.ca ' ]})

