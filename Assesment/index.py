import boto3
import logging
import sys

key_value = "/tmp/key_value.txt"
def handler(event, context):
    logging.info("Started connecting boto3 client")
    try:
        client = boto3.client('ssm')
        s3 = boto3.client('s3')
        try:
            response = client.get_parameters(
                Names=['UserName'],
                WithDecryption=True
            )
            ssm_dict = dict()
            for parameter in response["Parameters"]:
                ssm_dict["Name"] = parameter["Name"]
                ssm_dict["Value"] = parameter["Value"]
            logging.info("Sucessfully retrieved ssm parameters")
        except Exception:
            logging.error("Failed to retrieve ssm parameters")
            sys.exit()
        try:
            f = open(key_value, "w")
            f.write(f"{ssm_dict['Name']} : {ssm_dict['Value']}")
            f.close()
            logging.info("Successfully written data into file")
        except Exception:
            logging.error(f"Failed to write content into {key_value}")
        try:
            response = s3.upload_file(key_value, "testdxc", key_value)
            logging.info(f"Successfully uploaded file - {key_value} into s3 bucket")
        except Exception:
            logging.error("Failed to write ")
    except Exception:
        logging.error("Failed to connect boto3 client")





