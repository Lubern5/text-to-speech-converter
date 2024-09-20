import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError

polly_client = boto3.client('polly')
s3_client = boto3.client('s3')

S3_BUCKET_NAME = 'S3 BUCKET HERE'
AUDIO_FORMAT = 'mp3'

def lambda_handler(event, context):
    try:
        # Log the incoming event for debugging
        print('Received event:', json.dumps(event))

        # Access the text input directly from the event
        text_input = event.get('text', None)

        if not text_input:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Text input is required.'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST',
                    'Access-Control-Allow-Headers': 'Content-Type'
                }
            }

        response = polly_client.synthesize_speech(
            Text=text_input,
            OutputFormat=AUDIO_FORMAT,
            VoiceId='Joanna'
        )

        s3_key = f"tts_output_{context.aws_request_id}.{AUDIO_FORMAT}"

        if 'AudioStream' in response:
            with open('/tmp/output.mp3', 'wb') as audio_file:
                audio_file.write(response['AudioStream'].read())

            s3_client.upload_file('/tmp/output.mp3', S3_BUCKET_NAME, s3_key)

            presigned_url = s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': S3_BUCKET_NAME, 'Key': s3_key},
                ExpiresIn=3600
            )

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Text-to-speech conversion successful!',
                    'audio_url': presigned_url
                }),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST',
                    'Access-Control-Allow-Headers': 'Content-Type'
                }
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error: No audio stream returned from Polly.'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST',
                    'Access-Control-Allow-Headers': 'Content-Type'
                }
            }

    except (BotoCoreError, ClientError) as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error occurred: {str(error)}"}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }
