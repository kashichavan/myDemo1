from django.shortcuts import render
from .froms import *
# Create your views here.
def create(request):
    if request.method=='POST':
        st=StudentForm(request.POST)
        if st.is_valid():
            st.save()
    st=StudentForm()
    return render(request,'create.html',{'st':st})


def show(request):
    data=Student.objects.all()
    return render(request,'show.html',{'data':data})
