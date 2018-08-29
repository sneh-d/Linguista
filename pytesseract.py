#!/usr/bin/env python

'''
Python-tesseract. For more information: https://github.com/madmaze/pytesseract

'''

try:
    import Image
except ImportError:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

import os
import sys
import subprocess
import tempfile
import shlex

#self modules
import translate
import image_capture
import image_features


# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
tesseract_cmd = 'tesseract'

__all__ = ['image_to_string']


def run_tesseract(input_filename, output_filename_base, lang=None, boxes=False,
                  config=None):
    '''
    runs the command:
        `tesseract_cmd` `input_filename` `output_filename_base`

    returns the exit status of tesseract, as well as tesseract's stderr output

    '''
    command = [tesseract_cmd, input_filename, output_filename_base]

    if lang is not None:
        command += ['-l', lang]

    if boxes:
        command += ['batch.nochop', 'makebox']

    if config:
        command += shlex.split(config)

    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    status = proc.wait()
    error_string = proc.stderr.read()
    proc.stderr.close()
    return status, error_string


def cleanup(filename):
    ''' tries to remove the given filename. Ignores non-existent files '''
    try:
        os.remove(filename)
    except OSError:
        pass


def get_errors(error_string):
    '''
    returns all lines in the error_string that start with the string "error"

    '''

    error_string = error_string.decode('utf-8')
    lines = error_string.splitlines()
    error_lines = tuple(line for line in lines if line.find(u'Error') >= 0)
    if len(error_lines) > 0:
        return u'\n'.join(error_lines)
    else:
        return error_string.strip()


def tempnam():
    ''' returns a temporary file-name '''
    tmpfile = tempfile.NamedTemporaryFile(prefix="tess_")
    return tmpfile.name


class TesseractError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        self.args = (status, message)


def image_to_string(image, lang=None, boxes=False, config=None):
    '''
    Runs tesseract on the specified image. First, the image is written to disk,
    and then the tesseract command is run on the image. Tesseract's result is
    read, and the temporary files are erased.

    Also supports boxes and config:

    if boxes=True
        "batch.nochop makebox" gets added to the tesseract call

    if config is set, the config gets appended to the command.
        ex: config="-psm 6"
    '''

    if len(image.split()) == 4:
        # In case we have 4 channels, lets discard the Alpha.
        # Kind of a hack, should fix in the future some time.
        r, g, b, a = image.split()
        image = Image.merge("RGB", (r, g, b))

    input_file_name = '%s.bmp' % tempnam()
    output_file_name_base = tempnam()
    if not boxes:
        output_file_name = '%s.txt' % output_file_name_base
    else:
        output_file_name = '%s.box' % output_file_name_base
    try:
        image.save(input_file_name)
        status, error_string = run_tesseract(input_file_name,
                                             output_file_name_base,
                                             lang=lang,
                                             boxes=boxes,
                                             config=config)
        if status:
            errors = get_errors(error_string)
            raise TesseractError(status, errors)
        f = open(output_file_name, 'rb')
        try:
            return f.read().decode('utf-8').strip()
        finally:
            f.close()
    finally:
        cleanup(input_file_name)
        cleanup(output_file_name)


"""def main():
    if len(sys.argv) == 1:
        #print("One argument")
        filename = image_capture.take_image()
        try:
            image = Image.open(filename)
            if len(image.split()) == 4:
                # In case we have 4 channels, lets discard the Alpha.
                # Kind of a hack, should fix in the future some time.
                r, g, b, a = image.split()
                image = Image.merge("RGB", (r, g, b))
        except IOError:
            sys.stderr.write('ERROR: Could not open file "%s"\n' % filename)
            exit(1)
        output_text = image_to_string(image)
        print(output_text)
        src = ""
        print(src)
        dest = 'hi'
        translated_text = translate.translate(src,dest,output_text)
        translated_text = translated_text.decode('utf8')
        image_features.image_f(filename, translated_text, dest)
        #image.show()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            image = Image.open(filename)
            if len(image.split()) == 4:
                # In case we have 4 channels, lets discard the Alpha.
                # Kind of a hack, should fix in the future some time.
                r, g, b, a = image.split()
                image = Image.merge("RGB", (r, g, b))
        except IOError:
            sys.stderr.write('ERROR: Could not open file "%s"\n' % filename)
            exit(1)
        output_text = image_to_string(image)
        print(output_text)
        src = ""
        dest = 'en'
        translated_text = translate.translate(src,dest,output_text)
        #print(translated_text)
        translated_text = translated_text.decode('utf8')
        image_features.image_f(filename, translated_text, dest)
    elif len(sys.argv) == 4 and sys.argv[1] == '-l':
        lang = sys.argv[2]
        filename = sys.argv[3]
        try:
            image = Image.open(filename)
        except IOError:
            sys.stderr.write('ERROR: Could not open file "%s"\n' % filename)
            exit(1)
        output_text = image_to_string(image, lang=lang)
        print(output_text)
        output_text = output_text.encode('utf8')
        fin_file = open("dest1.txt", "w")
        fin_file.write(output_text)
        fin_file.close()
        fin_file = open("dest1.txt", "r")
        output_text2 = fin_file.readline()
        print(output_text2)
        src = ''
        dest = 'en'
        translated_text = translate.translate(src,dest,output_text2)
        print(translated_text)
        translated_text = translated_text.decode('utf8')
        image_features.image_f(filename, translated_text, dest)
    else:
        sys.stderr.write('Usage: python pytesseract.py [-l lang] input_file\n')
        exit(2)"""


def func(filename, src_lang, dst_lang):
    lang = src_lang
    #lang = 'tam'
    filename = filename
    #filename = "Images/spa2.png"
    try:
        image = Image.open(filename)
    except IOError:
        sys.stderr.write('ERROR: Could not open file "%s"\n' % filename)
        exit(1)
    print(lang)
    output_text = image_to_string(image, lang=lang)
    print('output in pytesseract')
    print(output_text)
    src = 'en'
    if lang=='eng':
        src = 'en'
    elif lang == 'spa':
        src = 'es'
    elif lang == 'deu':
        src = 'de'
    elif lang == 'fra':
        src = 'fr'
    elif lang == 'ita':
        src = 'it'
    elif lang == 'ben':
        src = 'bn'
    elif lang == 'tam':
        src = 'ta'
    elif lang == 'hin':
        src = 'hi'
    elif lang == 'pan':
        src = 'pa'
    dest = dst_lang
    #dest = 'ta'
    translated_text = translate.translate(src,dest,output_text)
    print(translated_text)
    translated_text = translated_text.decode('utf8')
    file = image_features.image_f(filename, translated_text, dest)
    return file


"""if __name__ == '__main__':
    main()"""