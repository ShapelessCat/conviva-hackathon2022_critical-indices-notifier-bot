import json
import logging
import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from configuration import path2tokens, path2reports_folder


def generate_path2report() -> str:
    # TODO: This should be from the cloud, and in reality the report_name should
    #       be in a pattern "report_[client_name]_[current_date].[extension]".
    #       We hard code it here to basic functionality testing.
    report_name = "file4test.jpeg"
    return os.path.join(path2reports_folder, report_name)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)

    SLACK_SIGNING_SECRET = "SLACK_SIGNING_SECRET"
    SLACK_BOT_TOKEN = "SLACK_BOT_TOKEN"

    # TODO: In reality, we should fetch these tokens from a service,
    #       instead of saving them in a file, which is bad for the
    #       security concern.
    tokens = json.load(open(path2tokens))

    # WebClient instantiates a client that can call API methods
    # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
    client = WebClient(token=tokens["SLACK_BOT_TOKEN"])

    # The name of the file you're going to upload
    path2report = generate_path2report()
    # ID of channel that you want to upload file to
    # TODO: This should be configurable in a complete bot.
    #       Hardcode it here for testing.
    channel_name = "2022-conviva-hackathon"
    channel_id = "C04D0SFQ64X"

    try:
        # Call the files.upload method using the WebClient
        # Uploading files requires the `files:write` scope
        # result = client.files_upload(
        #     channels=channel_id,
        #     initial_comment="Here are the critical indices from Conviva",
        #     file=file_name,
        # )
        result = client.files_upload_v2(
            file=path2report,
            channel=channel_id,
            initial_comment="Here are the critical indices from Conviva",
        )
        # Log the result
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error uploading file: {}".format(e))
