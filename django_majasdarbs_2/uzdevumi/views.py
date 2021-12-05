from django.shortcuts import render
from django.http import HttpResponse
from .models import Juzeru_klase



# CSV --------------------------------------------------------

from .forms import UploadCsvForm
from .csv_handler import read_and_decode_csv, csv_rows_to_db

def upload_csv_to_db(request):

	form = UploadCsvForm(request.POST or None, request.FILES or None)

	if request.method == 'POST':
		if form.is_valid():
			decoded_file = read_and_decode_csv(request.FILES['izvēlies_csv_failu'])
			csv_rows_to_db(decoded_file)
			return HttpResponse('Dati no *.csv faila veiksmīgi pievienoti datubāzei <br><br> (!) Refrešojot šo lapu, dati tiek vēlreiz pievienoti')


	return render(
		request,
		template_name='csv_upload_form.html',
		context={'form': form }
	)





# --------------------------------------------------------


def md4_skats_viens_juzeris(request, user_id):

	user = Juzeru_klase.objects.get(id=user_id)

	return render(
		request,
		template_name='md4_viens_juzeris.html',
		context={
			'user': user,
		}
	)



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

juzeru_saraksts = []

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

