import sys
import logging

def error_msg_detail(error, error_detail:sys):
    _,_,ext_tb = error_detail.exc_info()

    filename = ext_tb.tb_frame.f_code.co_filename

    error_msg = "Error occured in file [{0}], line no [{1}], and error msg is [{2}]".format(
        filename, ext_tb.tb_lineno, str(error)
    )
    return error_msg

class custom_exception(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(error_msg, error_detail=error_detail)

    
    def __str__(self):
        return self.error_msg

"""
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Logging has started")
        raise custom_exception(e, sys)
"""