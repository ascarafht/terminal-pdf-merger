#!/usr/bin/env python3

import os
from argparse import ArgumentParser
import PyPDF2

parser = ArgumentParser(
    prog='mpdf',
    description='Merge a list of PDF files.'
)

parser.add_argument('files', nargs='+', help='List of PDF files.')
parser.add_argument('dest', help='Destination path and file name for merged file.')
args = parser.parse_args()
pdf_files = args.files
path, suffix = os.path.splitext(args.dest)
if len(suffix) == 0:
    suffix = '.pdf'

merger = PyPDF2.PdfMerger()
try:
    for file in pdf_files:
        merger.append(file)
    merger.write(f'{path}{suffix}')
except PyPDF2.errors.PdfReadError as e:
    print('Error: Cannot create PDF')
except Exception as e:
    print(f'Error: {e}, {type(e)}')
finally:
    merger.close()