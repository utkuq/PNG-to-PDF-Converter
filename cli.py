from PIL import Image
import os
import glob
import sys

def convert_pngs_to_pdf(png_dir, pdf_path):
    # Get list of file paths in the PNG directory
    file_paths = glob.glob(png_dir + "/*.png")

    # Sort file paths numerically by file name
    file_paths = sorted(file_paths, key=lambda path: int(os.path.basename(path).split(".")[0]))

    # Open each PNG file and append to list of images
    images = []
    for file_path in file_paths:
        image = Image.open(file_path).convert("RGB")
        images.append(image)

    # Convert list of images to PDF and save
    images[0].save(pdf_path, save_all=True, append_images=images[1:])


# png_dir = 'C:\\Users\\User\\Desktop\\WEEK1'
# pdf_path = 'C:\\Users\\User\\Desktop\\merged.pdf'

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf.py <PNG directory> <PDF file path>")
        print("Example: python pdf.py 'C:/Users/<Your Username>/Desktop/WEEK1' 'C:/Users/<Your Username>/Desktop/merged.pdf'")
    else:
        png_dir = sys.argv[1]
        pdf_path = sys.argv[2]
        convert_pngs_to_pdf(png_dir, pdf_path)





