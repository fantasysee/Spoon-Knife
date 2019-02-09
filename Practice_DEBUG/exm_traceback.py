import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def test_traceback():
    try:
        raise Exception('This is a test of error message.')
    except:
        errorFile.write(traceback.format_exc())
        logging.debug(traceback.format_exc())
        print('The traceback info was written to error_Info_of_exm_traceback.txt')
        # Amazing! The order of these two above are in random order. Why?


errorFile = open('error_Info_of_exm_traceback.txt', 'w')
for i in range(10):
    test_traceback()
errorFile.close()
