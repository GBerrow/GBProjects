# QR generator with a couple of enhanced features:
# Option to choose the error correction level when creating the QR code.
# The user can to add a logo to the center of the QR code.


import qrcode

class MyQR:
    def __init__(self, size: int, padding: int, error_correction: str):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=padding,
        )
        self.error_correction = error_correction

    def create_qr(self, file_name: str, fg: str, bg: str, include_logo: bool, logo_path: str = None):
        user_input: str = input('Enter text: ')

        try:
            self.qr.add_data(user_input)
            self.qr.make(fit=True)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)

            if include_logo and logo_path:
                self.add_logo(qr_image, logo_path)

            qr_image.save(file_name)
            print(f'Successfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')

    def add_logo(self, qr_image, logo_path):
        try:
            logo = qrcode.image.pure.PymagingImage(logo_path)
            factor = int(qr_image.size[0] / 4)
            img_size = (factor, factor)
            logo = logo.resize(img_size)
            qr_image.paste(logo, (int((qr_image.size[0] - img_size[0]) / 2), int((qr_image.size[1] - img_size[1]) / 2)))
        except Exception as e:
            print(f'Error adding logo: {e}')

def main():
    size = 30
    padding = 2
    error_correction = input('Enter error correction level (L, M, Q, H): ').upper()
    include_logo = input('Include logo? (y/n): ').lower() == 'y'
    logo_path = input('Enter logo path (leave empty if none): ')

    myqr = MyQR(size=size, padding=padding, error_correction=error_correction)
    myqr.create_qr('sample.png', fg='black', bg='white', include_logo=include_logo, logo_path=logo_path)

if __name__ == '__main__':
    main()
