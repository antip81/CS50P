from fpdf import FPDF


def main():
    shirtificate_create(input("Name: "))


def shirtificate_create(name: str):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_margin(0)
    pdf.add_page()

    pdf.image("shirtificate.png", w=194, x=9, y=82)
    # should set up new_x and new_y coordinates in order to create another cell right after this one
    pdf.set_font('helvetica', size=50)
    pdf.cell(210, 107, txt="CS50 Shirtificate", align="C", fill=False, new_y="NEXT", new_x="LEFT")

    pdf.set_font('helvetica', size=25)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(210, 88, txt=f"{name} took CS50P", align="C", fill=False)

    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()
