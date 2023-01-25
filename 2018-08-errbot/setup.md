# Setup instructions

1. Install the dependencies:

    ```bash
    python3 -m venv errbot.venv
    sh errbot.venv/bin/activate  # bash
    # vox activate errbot.venv  # xonsh
    pip install errbot==5.2.0 slackclient==1.2.1
    ```

2. Bootstrap the errbot install:

    ```bash
    errbot --init
    ```

3. Update/Create the following configuration entries (carefully filling out placeholders):

    ```python
    BACKEND = 'Slack'
    BOT_IDENTITY = {
        'token': 'Get it from Slack!',
    }
    BOT_ADMINS = ('@change-to-your-slack-handle',)
    CHATROOM_PRESENCE = ()
    CHATROOM_FN = 'errbot'
    BOT_PREFIX = '!'
    BOT_ALT_PREFIXES = ('@errbot',)
    ```
