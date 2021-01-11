import pypandoc

print("Starting conversions - this tends to be slower than what you would expect")

output = pypandoc.convert_file('../dime-data-nda.md', 'pdf', outputfile='../dime-data-nda.pdf',
                                extra_args=['-V', 'geometry:margin=3cm'])
assert output == ""

print("Conversion successfull")
