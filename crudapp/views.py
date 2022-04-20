from django.shortcuts import redirect, render

from crudapp.models import colg
# Create your views here.
#addproduct HTML page
def addstudents(request):
    return render(request,'add.html')

#product details
def addstudentdetails(request):
    if request.method=='POST':
        pname=request.POST['stu_name']
        ad=request.POST['adres']
        ge=request.POST['gen']
        qu=request.POST['qua']
        em=request.POST['email']
        do=request.POST['daofb']
        products=colg(Stud_name=pname,
                            
                               Address=ad,
                               Gender=ge,
                               Qualification=qu,
                               Email=em,
                               DOB=do,)
        products.save()
        print("Hii")
        return redirect('showstudent')

def showstudent(request):
    products=colg.objects.all()
    return render(request, 'show.html', {'products': products})

def editstudent(request,pk):
    products=colg.objects.get(id=pk)
    return render(request,'edit.html',{'products':products})  


def editstu(request,pk):
    if request.method=='POST':
        products=colg.objects.get(id=pk)
        products.Stud_name = request.POST.get('stu_name')
        products.Address = request.POST.get('adres')
        products.Gender= request.POST.get('gen')
        products.Qualification= request.POST.get('qua')
        products.Email= request.POST.get('email')
        products.DOB= request.POST.get('daofb')
        products.save() 
        print("successfully updated")
        return redirect('showstudent')
    return render(request,'edit.html',) 

def deletestudent(request,pk):
    products=colg.objects.get(id=pk)
    return render(request,'delete.html',{'products':products})

def delete(request,pk):
    products=colg.objects.get(id=pk)
    products.delete()
    print("successfully deleted")
    return redirect('showstudent')   

