from reportlab.pdfgen import canvas
 
 
def add_image():
 
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
 
    in_pdf_file =  str(input("Logo eklenecek pdf'in ismini giriniz. (Örnek 'satislar.pdf')"))
    out_pdf_file = "new-" + in_pdf_file
    img_file = str(input("Eklenecek logonun ismini yazınız. (Örnek: 'logo.png')"))
    img_file = "Eklenecekler/" + img_file
    inputValue = int(input("Kaç adet logo eklenecek: ")) 
    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    for i in range(inputValue):
        x = int(input("X değerini giriniz (Dikey hizanın konumu): "))
        y = int(input("Y değerini giriniz (Yatay hizanın konumu): "))
        widtH = int(input("Genişlik değerini giriniz: "))
        can.drawImage(img_file, x, y, width=widtH, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.save()
 
    packet.seek(0)
 
    new_pdf = PdfFileReader(packet)
 

    existing_pdf = PdfFileReader(open("Değişecek PDF'Ler/"+in_pdf_file, "rb"))
    output = PdfFileWriter()
    

   
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    outputStream = open("Değişen PDF'ler/"+ out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()
 
 
add_image()