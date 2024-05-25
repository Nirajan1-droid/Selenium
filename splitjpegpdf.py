from wand.image import Image
 
import os

def split_pdf(pdf_path, output_dir):
    """Splits a PDF into separate PDFs with page numbers as names.
    
    Args:
        pdf_path: Path to the input PDF file.
        output_dir: Directory to save the split PDFs and JPEGs.
        svg_path: Path to the SVG image file.
    """
    with Image(filename=pdf_path, resolution=150) as image:
        image.compression_quality = 60
        for page_num, page in enumerate(image.sequence):
            # Convert PDF page to JPEG
            jpeg_output_filename = f"{output_dir}/{page_num + 1}.jpg"
            with Image(page) as img_page:
                # Place SVG image in center and blend
                 
                img_page.save(filename=jpeg_output_filename)

    print(f"PDF split and converted to JPEG successfully! Files saved in {output_dir}")



def split_pdf_directory(input_dir, output_dir):
    """Traverses through each PDF document in the input directory, splits each PDF file,
    and saves the split pages in the output directory with managed file names.
    
    Args:
        input_dir: Directory containing PDF documents to split.
        output_dir: Directory to save the split PDF pages.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Traverse through each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            # Full path of the input PDF file
            pdf_path = os.path.join(input_dir, filename)
            
            # Output directory specific to each PDF document
            doc_output_dir = os.path.join(output_dir, os.path.splitext(filename)[0])
            os.makedirs(doc_output_dir, exist_ok=True)
            
            # Split the PDF document and save pages in the output directory
            split_pdf(pdf_path, doc_output_dir)

# Example usage
input_dir = "C:/pdffilter"  # Directory containing PDF documents to split
output_dir = "C:/pdffilter/split_output"  # Directory to save the split PDF pages

split_pdf_directory(input_dir, output_dir)

