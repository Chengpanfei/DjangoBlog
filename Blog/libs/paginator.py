from django.core.paginator import (
	Paginator,
	EmptyPage,
	PageNotAnInteger
	)


def paginate(objects, current_page, num_per_page=5):
	'''
	对传入的对象进行分页，并返回指定分页
	'''
	paginator = Paginator(objects,num_per_page)
	#下面代码来自官方教程
	
	try:
		items = paginator.page(current_page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		items = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		items = paginator.page(paginator.num_pages)

	return items