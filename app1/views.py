import os

import pandas as pd
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from openpyxl.reader.excel import load_workbook

from .mypythonpackage import audiototext as a2t_copy
from .mypythonpackage import myexcelclass as myexlcls
from .forms import MyForm, CreateNewBillFile


def home(request):
    template = loader.get_template('homfortools.html')
    return HttpResponse(template.render())


# Create your views here.

def login(request):
    template = loader.get_template('login.html')

    return HttpResponse(template.render())


"""def monthlybillform(request):
    template = loader.get_template('monthlyexpenisive.html')

    return HttpResponse(template.render(), {'getlistofexlfiles': os.listdir(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/Excelfiles"
    )})"""


def monthlybillform(request):
    return render(request, 'monthlyexpenisive.html', {'getlistofexlfiles': myexlcls.getlistofexlfiles(),
                                                      'months': myexlcls.listofmonths,
                                                      'yearslist': myexlcls.year_list,
                                                      'current_month': myexlcls.month_,
                                                      'current_year': myexlcls.year,
                                                      })


def add_record(request):
    commodity_name = request.GET['commnm']
    price = request.GET['price']
    date = request.GET['dateofpymnt']
    place = request.GET['plcoftranopt']
    category = request.GET['category']
    commodity = {'commodity_1': [commodity_name, price, date, place, category]}

    # myexcelclass.get_value_from_web(commodity)  # calling function to set values in Excel file
    myexlcls.get_value_from_web(commodity)

    return render(request, 'result.html', {'result': commodity['commodity_1']})


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form = UserCreationForm()
        if request.method == 'POST':
            Form = UserCreationForm(request.POST)
            if Form.is_valid():
                currUser = Form.save()
                # Users.objects.create(user=currUser, name=currUser.username)
                return redirect('login')
        context = {
            'form': Form
        }
        return render(request, 'register.html', context)


def textmsg(request):
    msg = input("Write something here..")
    print("Check the page again")
    return HttpResponse("Your message is here  " + msg)


def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 + num2
    return render(request, 'result.html',
                  context={'result': res,
                           'num1': num1,
                           'num2': num2,
                           })


def audiototext(request):
    # a2t.print_something()
    a2t_copy.extractepname()
    a2t_copy.get_list_ofavalbland_notavalbl_2and_writing_and_savinghtml()
    template = loader.get_template('gettextfromaudio.html')

    characters = ['Bhakshanar', 'yug', 'yamini', 'shalini', 'abhimanyu', 'dayna', 'anurag', 'chitra', 'yakhsini',
                  'kayar', 'bindu', 'kachua', 'rajan', 'dileep', 'janki', 'vandana', 'virat', 'sudesh', 'rajani',
                  'amodita', 'balukaka', 'varchusani', 'Devika', 'Ravindra', 'tara', 'charlie', 'chatergee', 'prashant',
                  'phalguni', 'RatanPali', 'mohit', 'Dhaniya', 'Hariya', 'Jagdish', 'aghori', 'mayadhari', 'kanchan',
                  'plak', 'vedant', 'kartik pujari', 'Dayantika', 'Nishach', 'Darmika']

    return HttpResponse(template.render({
        'characterslist': characters,
    },
        request))


def getTextfromlink(request):
     new_link = request.GET['link_ytYak']
     try:
        # num = int(input("Enter the episode num - "))
        # a2t_copy.youtubehindi_link2text(new_link, num)
        a2t_copy.youtubehindi_link2text(new_link)
        return HttpResponse("audio from link is transcribed !!")
     except Exception as e:
        return HttpResponse(f"check the Url {e}")


def getTextfromlink_listwise(request):
    new_linklist = request.GET['linklist_ytYak']
    new_linklist = new_linklist.split(',')
    try:
        a2t_copy.youtubehindi_link2text_listwise(new_linklist)
        return HttpResponse("audio from link is transcribed !!")
    except Exception as e:
        return HttpResponse(f"check the Url {e}")


def downlvid_extrud_fun(request):
    new_link = request.GET['link_ytYak_fordwnldvdad']
    try:
        # num = int(input("Enter the episode num - "))
        # a2t_copy.dowload_video_andextractaudio(new_link,num)
        a2t_copy.dowload_video_andextractaudio(new_link)
        return HttpResponse("audio & video from link is download !!")


    except Exception as e:
        return HttpResponse(f"check the Url {e}")


def addtwonum(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())


def load_image(request):
    template = loader.get_template('lionimageloader.html')
    # print(a2t_copy.load_immagelinkhtml())
    a2t_copy.imageLoaderHtml()
    return HttpResponse(template.render({
        'images_linklist': a2t_copy.load_immagelinkhtml(),
    }))


def loadajaxhtml(request):
    template = loader.get_template('ajaxform.html')
    return HttpResponse(template.render())


def getitem(request):
    pass


def my_function(request):
    # https://docs.djangoproject.com/en/5.0/topics/forms/
    # print(request.GET['billpriceTOT'])

    billprice = request.GET['totbillprice2']
    month = request.GET['billmonth2']
    year = request.GET['year2']
    customname = request.GET['custname_var']

    if billprice != "":
        new_bill_filename = month + year + "_" + billprice
        result = myexlcls.crtnewbillfile(new_bill_filename)
    else:
        result = myexlcls.crtnewbillfile(customname)

    return JsonResponse({'result': result})


def get_commodity_details(request):
    # https://docs.djangoproject.com/en/5.0/topics/forms/
    file = request.GET['file']
    commodity_name = request.GET['commnm']
    price = request.GET['comdprice']
    date = request.GET['dateofpymnt']
    place = request.GET['plcoftranopt']
    category = request.GET['category']

    commodity = {'commodity_1': [commodity_name, price, date, place, category]}
    result = myexlcls.get_value_from_web(commodity, file)
    filedata = []
    if file != "":
        filedata = myexlcls.load_filedata_to_templeate(file)

    return JsonResponse({'result_1': result, 'filedata2': filedata})


def my_view(request):
    print(request)
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'], form.cleaned_data['email'])
            # form.save()  # Save the form data to the database
            success_message = f'Data {form.cleaned_data["name"]}  {form.cleaned_data["email"]} saved successfully!'
            return render(request, 'my_template.html', {'form': form, 'success_message': success_message})
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})


def search_files(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text', '')

        directory = "C:/Users/dell pc/PycharmProjects/djangoProjects/project1/app1/Excelfiles/"
        files = [f for f in os.listdir(directory) if
                 os.path.isfile(os.path.join(directory, f)) and search_text.lower() in f.lower()]
        return JsonResponse({'files': files})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_row(request):
    if request.method == 'POST':
        row_index = int(request.POST['row_index'])
        # Load data from Excel file
        df = pd.read_excel('data.xlsx')

        # Delete row
        df.drop(row_index, inplace=True)
        df.to_excel('data.xlsx', index=False)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def delete_record(request):
    
    if request.method == 'GET':
        file = request.GET['filename']
        unique_id = request.GET['hiddenData']
        print(file + " and " + unique_id)
        result = myexlcls.delete_record(file, unique_id)
        return JsonResponse({'status': 'success', 'result3': result})

    return JsonResponse({'status': 'error'})


def save_edited_record(request):

    file = request.GET['filenamefor_ser']
    unique_id = request.GET['uniqueId']
    edited_values = request.GET['editedvalues']
    
    edited_values = edited_values.split(',')
    print(file + " and " + unique_id + ' and  ', edited_values[:5])

    result = myexlcls.edit_record(file, unique_id, edited_values[:5])

    return JsonResponse({'status': 'success', 'result4': result})

    # return JsonResponse({'status': 'error'})
