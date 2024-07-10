import os
from dotenv import load_dotenv
load_dotenv()

###########
#   Auth  #
############
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")