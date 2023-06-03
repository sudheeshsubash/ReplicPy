REPLICPY CREATED BY SUDHEESH S

ReplicPy is a user-friendly Python framework designed to simplify the development of web applications.
Inspired by Django, it offers a similar approach but focuses on providing a minimalistic and straightforward syntax.
With ReplicPy, developers can quickly build web applications without sacrificing simplicity or flexibility.


Create a "main.py" File and copy past this code

from replicpydemo.core import defaultsetups
import sys

if __name__ == "__main__":
    '''
    Main file
    '''
    defaultsetups(sys.argv)



"urls.py" file

URLLIST = [
	('',function)
]




"View.py"

from replicpy.core import Response,JsonResponse

def index(param):

	# do code here!	

	return Response('index.html',context={key:value})
	or
	return JsonResponse({key:value})
