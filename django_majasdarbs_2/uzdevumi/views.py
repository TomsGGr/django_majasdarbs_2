from django.shortcuts import render
from django.http import HttpResponse
# from .forms import UserEmailForm


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
