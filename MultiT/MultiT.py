from frameT import frameT
from restfulT import restfulT
import _thread


def multiTmain():
    try:
        _thread.start_new_thread(frameT.frameTmain, ())
    except:
        print("Err")
    restfulT.restfulTmain()
