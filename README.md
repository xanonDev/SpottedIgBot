# SpottedIgBot

SpottedIgBot is a bot designed to automatically post anonymous entries from [tellonym.me](https://tellonym.me) to Instagram. Please note that this bot was developed solely for educational purposes, and using it may result in a ban on both Instagram and Tellonyme platforms. Therefore, you should use it at your own risk.

## How to Use

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Download the files from this repository.
3. Open a command prompt on Windows or a terminal on Linux and run the following command to install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    If this command doesn't work, try one of the following:
    ```
    py -m pip install -r requirements.txt
    ```
    ```
    python -m pip install -r requirements.txt
    ```
4. Open the website [tellonym.me](https://tellonym.me).
5. Log in to your Tellonym account.
6. Open the file named "GetTellToken.js".
7. Copy the code from the "GetTellToken.js" file.
8. Open your web browser's console by pressing "Ctrl + Shift + C" (or right-click and select "Inspect" or "Developer Tools," then navigate to the "Console" tab).
9. Paste the copied code into the console.
10. After executing the code, you will receive a token.
11. Copy the generated token.
12. Open the `main.py` file and make the following replacements:
    - Replace "IG USERNAME" with your Instagram username.
    - Replace "IG PASSWORD" with your Instagram password.
    - Replace "TOKEN" with the previously copied token.
    - Optionally, you can change the "post description" to have a description of your posts.
13. Run `main.py` using one of the following commands:
    ```
    py main.py
    ```
    ```
    python main.py
    ```
14. If the script gives the "429 Too Many Requests" error, it is recommended to replace the `api.py` file in the `%appdata%\..\Local\Programs\Python\Python310\lib\site-packages\instabot\api` directory with the `api.py` file in the "insta bot modified api" directory.

## Platforms

The script has been tested on Windows and [replit.com](https://replit.com), but it should work fine on Linux as well.

## Configuration

To configure the script, you can change the variables at the top of the `main.py` file. Here are the variables you can modify:

1. `username`: Your Instagram username.
2. `password`: Your Instagram password.
3. `tellTOKEN`: Tellonym API token.
4. `description`: Description of posts on Instagram.
5. `delay`: Time interval between each request for a new tell, specified in seconds. It is recommended to set it to at least 10 seconds.

## Libraries Used

The following libraries are used in SpottedIgBot:

- `os`: Execution of system commands.
- `time`: Pausing the program for a specific duration using the sleep function.
- `requests`: Communicating with the Tellonym API.
- `Pillow`: Generating graphics.
- `instabot`: Logging into Instagram and posting.
- `json`: Information management with the Tellonym API.
