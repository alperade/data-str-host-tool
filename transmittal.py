import requests
from fpdf import FPDF
import boto3

def generate_pdf():
    # Make a GET request to get the RFI information
    response = requests.get('http://localhost:8000/api/rfis/643892176b36fea316123b45')
    rfi_info = response.json()

    # Create the PDF object
    pdf = FPDF(orientation='P', unit='in', format='letter')

    # Add a page
    pdf.add_page()

    # Set font and font size
    pdf.set_font("Arial", size=12)

    # Print the RFI information
    pdf.cell(0, 0.5, f"RFI Number: {rfi_info['rfi_num']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Subject: {rfi_info['subject']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Question: {rfi_info['question']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Response: {rfi_info['response']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Status: {rfi_info['status']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"RFI From: {rfi_info['rfi_from']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"RFI To: {rfi_info['rfi_to']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Created On: {rfi_info['created_on']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Sent: {rfi_info['sent']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Division Code: {rfi_info['division_code']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Division Name: {rfi_info['division_name']}")
    pdf.ln()
    pdf.cell(0, 0.5, f"Project ID: {rfi_info['project_id']}")
    pdf.ln()
    pdf.cell(0, 0.5, "File URLs:")
    pdf.ln()
    for url in rfi_info['file_urls']:
        pdf.cell(0, 0.5, url)
        pdf.ln()

    # Upload the PDF to S3
    key = 'rfi_info.pdf'  # the filename to use in S3

    bucket_name = 'bucket_name'  # replace with your bucket name
    s3_resource = boto3.resource('s3',
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
    )
    bucket = s3_resource.Bucket(bucket_name)
    bucket.put_object(Key=key, Body=pdf.output(dest='S').encode('latin1'))

    print(f"PDF uploaded to S3 bucket '{bucket_name}' with key '{key}'")

generate_pdf()
