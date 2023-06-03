~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                         REPLICPY

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<--------------------------REPLICPY CREATED BY SUDHEESH S------------------------------->


1) installation

pip install replicpy

+--------------------------------------------+
Create a main.py File and copy past this code
+--------------------------------------------+

from replicpydemo.core import defaultsetups
import sys

if __name__ == "__main__":
    '''
    Main file
    '''
    defaultsetups(sys.argv)



+--------------------------------------------+
urls.py file
+--------------------------------------------+

URLLIST = [
	('',function)
]



+-------------------------------------------+
View.py
+-------------------------------------------+

from replicpy.core import Response,JsonResponse

def index(param):

	# do code here!	

	return Response('index.html',context={key:value})
	or
	return JsonResponse({key:value})



+--------------------------------------------+
Templates -> Create one templates directory
+--------------------------------------------+

* create html file inside this directory

>templates
	>index.html
	>about.html
	>demo.html


2) Linkes:-




========================================================
------------------------END-----------------------------
========================================================
	