from dotenv import load_dotenv
import os
load_dotenv()
UTILS = os.getenv("utils")
from pathlib import Path
module_dir = Path(UTILS)
import sys
sys.path.append(str(module_dir))

from fetch import APIClient


api = APIClient("http://localhost:9000/api")




