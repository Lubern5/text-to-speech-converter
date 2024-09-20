Text-to-Speech Converter
This project utilizes AWS Lambda and Amazon Polly to convert text into speech, providing a simple web interface for users. It demonstrates how to create a serverless application using AWS services, allowing easy text-to-speech conversion.

Features
Converts user-provided text into spoken audio.
Outputs audio in various formats via AWS Polly.
Utilizes AWS API Gateway for seamless integration.
Responsive web interface for easy interaction.
Table of Contents
Prerequisites
Setup
Usage
Deployment
Testing
Troubleshooting
Contributing
License
Prerequisites
Before you begin, ensure you have the following:

An AWS account.
Basic knowledge of AWS services (Lambda, API Gateway, S3).
Installed Node.js and npm (if you plan to modify the frontend).
Access to a terminal or command line.
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/Lubern5/text-to-speech-converter.git
cd text-to-speech-converter
Set up AWS Lambda:

Create a new Lambda function in the AWS Management Console.
Use a Python runtime (e.g., Python 3.8).
Add the necessary IAM permissions for Lambda to access Amazon Polly and S3.
Copy and paste the Lambda function code provided in the repository.
Configure API Gateway:

Create a new API in API Gateway.
Create a POST method linked to your Lambda function.
Enable CORS on the method:
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Content-Type
S3 Bucket Configuration:

Create an S3 bucket for storing audio files.
Ensure that the bucket policy allows public access if you want to directly share audio files via URLs.
Usage
Run the Application:

Open the index.html file in a web browser.
Enter your text in the textarea provided.
Click the "Convert to Speech" button.
The audio player will display once the audio is generated, allowing playback of the converted text.
API Testing:

You can also test the API using CURL:

bash
Copy code
curl -X POST https://your-api-gateway-url/dev/TTS -H "Content-Type: application/json" -d '{"text": "Hello, world!"}'
Replace your-api-gateway-url with your actual API Gateway URL.

Deployment
Ensure all configurations are correctly set in AWS.
Deploy your API in API Gateway.
Update the frontend URL in your code if necessary to point to the deployed API.
Testing
Frontend Testing:

Open index.html in a browser and check for console errors.
Validate audio playback after submitting text.
API Testing:

Use CURL or Postman to test the API endpoint directly.
Verify that the response contains an audio_url.
Troubleshooting
CORS Issues:

If you encounter CORS-related errors, ensure that your API Gateway has CORS enabled with the correct headers.
Authentication Errors:

Check if your API requires an API key or other authentication mechanisms. Update your request headers accordingly.
Missing Authentication Token:

Verify that the API URL is correct and matches the deployment stage. Make sure the endpoint is active.
Failed to Fetch Errors:

Check for network issues or incorrect API configurations. Ensure the API is deployed and accessible.
Lambda Execution Errors:

Review the AWS Lambda logs in CloudWatch to troubleshoot any runtime errors.
Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bugs.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to modify or add any specific sections that might be relevant to your project!
