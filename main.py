import PyPDF2

pdfiles = ["sample1.pdf","sample.pdf", "sample2.pdf"]
merger = PyPDF2.PdfFileMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')