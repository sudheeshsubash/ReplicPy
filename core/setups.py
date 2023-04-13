from .server import runserver
import os,sys
from datetime import datetime

class CheckArgument:
    '''
    check argume or terminal commad
    '''
    def check_runserver(self,argv:list):
        '''
        This Function is check argument and filename
        '''
        if argv[0] != 'main.py':
            print("main file name Error")
            return
        try:
            if argv[1] == 'runserver':
                return 'runserver'
        except Exception:
            print('argument error')
            return



def run_all_user_files():
    '''
    check urls.py and view.py files
    '''
    sys.path.append(os.getcwd())
    import urls
    print("Check Status ...")
    print("Version - 0.0.1")
    print(f"Date - {datetime.today().date()}")
    runserver(urls.urllist,PORT=8000)



def defaultsetups(argv:list):
    '''
    this is default setups here we check the all files and termainal commads
    '''
    check_argument_object = CheckArgument()
    if len(argv)==2 and check_argument_object.check_runserver(argv) == 'runserver':
        run_all_user_files()