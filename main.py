from PIL import Image, ImageDraw, ImageFont
import os

def read_text_from_file(filename):
    """ อ่านข้อความจากไฟล์ """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("Warning: The file is empty.")
            return lines
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def create_a4_image_with_text(text_lines, output_filename):
    """ สร้างภาพ A4 และใส่ข้อความลงในภาพ """
    # ขนาด A4 ที่ 300 DPI
    width, height = 2480, 3508
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # โหลดฟอนต์
    try:
        font = ImageFont.truetype('arial.ttf', size=32)  # ฟอนต์ arial.ttf ต้องอยู่ในโฟลเดอร์เดียวกับสคริปต์
        print("Loaded font 'arial.ttf'.")
    except IOError:
        print("Warning: 'arial.ttf' font not found. Using default font.")
        font = ImageFont.load_default()

    # ตำแหน่งเริ่มต้นของข้อความ
    text_x, text_y = 100, 100
    line_spacing = 50  # ระยะห่างระหว่างบรรทัด

    # เขียนข้อความลงในภาพ
    print("Drawing text onto the image...")
    for line in text_lines:
        draw.text((text_x, text_y), line.strip(), font=font, fill=(0, 0, 0))
        text_y += line_spacing  # ย้ายตำแหน่งข้อความลงไป

    # สร้างโฟลเดอร์ output หากยังไม่มี
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Output folder '{output_folder}' created.")

    # บันทึกภาพ
    output_path = os.path.join(output_folder, output_filename)
    try:
        image.save(output_path)
        print(f"Image saved as {output_path}")
        image.show()  # แสดงภาพ
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")

# เริ่มต้นโปรแกรม
if __name__ == '__main__':
    print("Reading text from file...")
    text_lines = read_text_from_file('annotations.txt')
    if text_lines:
        print(f"Text read successfully. Number of lines: {len(text_lines)}")
        create_a4_image_with_text(text_lines, 'output_image.png')
    else:
        print("No text found in the input file or the file could not be read.")
