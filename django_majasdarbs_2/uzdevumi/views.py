from django.shortcuts import render
from django.http import HttpResponse
from .models import Juzeru_klase

juzeru_saraksts = []


def md3_skats_db_forma(request):

	# šis notiek, kad spiež formas SUBMIT pogu (metode POST)
	if request.method == 'POST':

		# .						input nosaukums formā
		user_obj = Juzeru_klase(
			user=request.POST['username'],
			email=request.POST['email'],
		)

		user_obj.save() # objektu ieliek datubāzē

		lapa = render(
			request,
			template_name='md3_db_02.html',
			context={'juzeris': user_obj},
		)

		return lapa

	# šis parādās pie metodes GET (sākumā)(parāda formu)
	return render(
		request,
		template_name='django_md2_01.html',
	)

def md3_skats_db_saraksts(request):

	juuzeri = Juzeru_klase.objects.all() # Juzeru_klase.object.get(id=1)  vai Juzeru_klase.object.get(user='Toms') vai Juzeru_klase.object.filter(user='Anna') (atgriež visus, kam user='Anna')

	return render(
		request,
		template_name='md3_db_03.html',
		context={'visi_juzeri': juuzeri},
	)




# vecais mājasdarbs bez DB --------------------------------------------------------

def django_md2_skats_1(request):

	# šis notiek, kad spiež SUBMIT pogu
	if request.method == 'POST':
		# .							 input nosaukums formā
		username_return = request.POST['username']
		email_return = request.POST['email']

		konteksts = {
			'juzeris': username_return,
			'epasts': email_return,
		}

		juzeru_saraksts.append(konteksts)

		lapa = render(
			request,
			template_name='django_md2_02.html',
			context=konteksts,
		)

		return lapa

	# šis parādās pie metodes GET, kad ievada adresi (sākumā)
	return render(
		request,
		template_name='django_md2_01.html',
	)


def django_md2_skats_saraksts(request):

	saraksts_html = '<ul>'
	for list_element in juzeru_saraksts:
		saraksts_html += '<li><b>' + list_element['juzeris'] + '</b><br>E-mail: ' + list_element['epasts'] + '</li>'
	saraksts_html += '</ul><br><br><a href="add-user">Add new user</a>'

	return HttpResponse(saraksts_html)

def django_md_skats_saraksts_b(request):

	return render(
		request,
		template_name='django_md2_saraksts.html',
		context={'saraksts': juzeru_saraksts},
	)

