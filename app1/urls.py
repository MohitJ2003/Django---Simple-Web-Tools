from django.urls import path
from . import views

urlpatterns = [

    path('project1/login/', views.login, name="login"),
    path('project1/signup/', views.signup, name='signup'),

    path('project1/app1/', views.textmsg, name='app1'),
    path('project1/monthlybillform/', views.monthlybillform, name="hello"),
    path('project1/', views.home, name='myapphome'),
    path('project1/monthlybillform/add_record', views.add_record, name='hello'),
    
    path('project1/audiototext/', views.audiototext, name='audiototext'),
    path('project1/addtwonum/', views.addtwonum, name='addTwonumbers'),
    path('project1/addtwonum/add', views.add, name='add'),
    path('project1/audiototext/GetTextfromlink', views.getTextfromlink, name='GetTextfrom_link'),
    path('project1/audiototext/Downlvid_extrAud', views.downlvid_extrud_fun, name="Downloadvideo_extractAudio"),
    path('project1/audiototext/GetTextfromlinklist', views.getTextfromlink_listwise, name="Downloadvideo_extractAudio"),
    

    path('project1/lion_image/', views.load_image, name='loadimage'),
    
    path('project1/my_function/', views.my_function, name='my_function'),
    
    path('project1/loadajaxhtml/', views.loadajaxhtml, name='loadajaxhtmlpage'),
    
    path('project1/my-form/', views.my_view, name='my_form'),
    
    path('project1/get_commodity_details/', views.get_commodity_details, name='get_commodity_details'),
    path('project1/search_files/', views.search_files, name='search_files'),
    path('project1/monthlybillform/delete_record', views.delete_record, name='delete_record'),
    path('project1/monthlybillform/save_edited_record', views.save_edited_record, name='save_edited_record'),
    path('project1/delete_row/', views.delete_row, name='delete_row'),

    path('project1/monthlybillform2',views.monthlybillform2,name="hello2"),
    
    path('project1/audvidtxt',views.audvidtxt,name="audvidtxt"),

    path('project1/car',views.car,name="car"),
    path('project1/test_django',views.test_django,name = "test_django"),
    path('fetch-countries/', views.fetch_countries, name='fetch_countries'),
    path('project1/joker',views.joker,name='joker'),

    
]
