import pypandoc

print("Starting conversion - this tends to be slower than what you would expect")

pdoc_args = ['-V','geometry:margin=3cm','-V','linkcolor:blue']

output = pypandoc.convert_file('../dime-data-nda.md',
                               'pdf',
                               outputfile='../dime-data-nda.pdf',
                               extra_args=pdoc_args
                               )
assert output == ""

print("Conversion successfull")
