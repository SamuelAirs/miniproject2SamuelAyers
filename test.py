import json
import boto3
import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    
    # 1. Extract URL from API Gateway payload
    article_url = event['body']['article_url'] 

    # 2. Download & Extract Simplified Article Contents
    try:
        response = requests.get(article_url)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        # Basic extraction (caution: website dependent)
        title = soup.find('title').text 
        article_text = "\n".join([p.text for p in soup.find_all('p')]) 

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing article: {str(e)}')
        }

    # 3. Rudimentary PDF Generation (replace with full conversion later)
    pdf_content = f"<h1>{title}</h1>\n\n{article_text}".encode('utf-8') 

    # 4. Store the PDF in S3 
    s3 = boto3.client('s3')
    bucket_name = 'your-pdf-storage-bucket'  # Replace with actual bucket
    file_key = 'temp_article.pdf' 
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=pdf_content) 

    # 5. Trigger Kindle Sender
    try:
        lambda_client = boto3.client('lambda')
        response = lambda_client.invoke(
            # Replace with your Kindle sender Lambda's name
            # If the Kindle sender has more complex PDF handling, 
            # ...consider changing the payload structure
            
            Payload=json.dumps({'s3_bucket': bucket_name, 's3_key': file_key}) 
        )   
        return {
            'statusCode': 200,
            'body': json.dumps('Article PDF generation and Kindle send initiated.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error sending PDF to Kindle: {str(e)}')
        }
