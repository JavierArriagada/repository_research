from pathlib import Path
from articles.models import User, Article
from django.utils import timezone

from django.core.files import File

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae ultricies leo integer malesuada nunc vel risus commodo viverra. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Augue lacus viverra vitae congue eu consequat ac. Ornare arcu dui vivamus arcu felis bibendum ut. Fermentum iaculis eu non diam phasellus. Massa sed elementum tempus egestas sed sed risus pretium quam. Blandit libero volutpat sed cras ornare arcu dui. Sit amet aliquam id diam maecenas. Risus nullam eget felis eget nunc lobortis mattis aliquam faucibus. Hendrerit dolor magna eget est lorem ipsum dolor. Felis donec et odio pellentesque diam volutpat commodo. Turpis cursus in hac habitasse platea dictumst quisque sagittis purus.'

roberto_asin = User.objects.get(username='roberto_asin')
ruta = 'c:/Users/Javier/Desktop/PDF/roberto_asin/'

for file in Path(ruta).iterdir():    
    doc = Article.objects.create(title=file.name, content=lorem)
    doc.created_by = roberto_asin
    doc.pdf.save(file.name, File(open(file, 'rb')))
    doc.save() 


julio_godoy = User.objects.get(username='julio_godoy')
ruta = 'c:/Users/Javier/Desktop/PDF/julio_godoy/'

for file in Path(ruta).iterdir():    
    doc = Article.objects.create(title=file.name, content=lorem)
    doc.created_by = julio_godoy
    doc.pdf.save(file.name, File(open(file, 'rb')))
    doc.save()  

zheng_li = User.objects.get(username='zheng_li')

ruta = 'c:/Users/Javier/Desktop/PDF/zheng_li/'

for file in Path(ruta).iterdir():    
    doc = Article.objects.create(title=file.name, content=lorem)
    doc.created_by = zheng_li
    doc.pdf.save(file.name, File(open(file, 'rb')))
    doc.save()   

cecilia_hernandez = User.objects.get(username='cecilia_hernandez')

ruta = 'c:/Users/Javier/Desktop/PDF/cecilia_hernandez/'

for file in Path(ruta).iterdir():    
    doc = Article.objects.create(title=file.name, content=lorem)
    doc.created_by = cecilia_hernandez
    doc.pdf.save(file.name, File(open(file, 'rb')))
    doc.save()  

gonzalo_rojas = User.objects.get(username='gonzalo_rojas')

ruta = 'c:/Users/Javier/Desktop/PDF/gonzalo_rojas/'

for file in Path(ruta).iterdir():    
    doc = Article.objects.create(title=file.name, content=lorem)
    doc.created_by = gonzalo_rojas
    doc.pdf.save(file.name, File(open(file, 'rb')))
    doc.save()  


     










