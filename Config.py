import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20137765"))
    API_HASH = os.environ.get("API_HASH", "461d1c1a84566a810b38145947b29e83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945870221:AAGDEnUVK6L-akYoATq7r8eQ3bcC5SzpbtA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJsBu7_wmWqpOlkyyVSpLXtWs2NN88UZb8RB5ZPaOlVcFS-8M3SNjctyv3P3IHe7qtozptjOIGMzfPsRVqErnzu_5D71Odwkfmew79bSAPc6IfOR0zT8V6ejdeA8UQWbehC-PT-iTIFQNWcX1rBfy_Kx2l0O08q4G7t4_gNuj_qcnSuerDvtBBPnKZ-1CfOguBwDyaT81MNu8Mk7Jnw0k_WwWmW_MB2M7opbnsrsFhWLXSuVX3YKW3VRawsBiq9QdwQ1f0UnfsdD1cC3gkUivAICk8UkFBWoqz19AfY7kgaT6L2T29hr0gjXJPbKm4kOpKzWFslElhKq5cBWbDSomMFskKI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Trumusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5691601913")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
