django-admin
#!/home/user/Desktop/coursera/workspace/capstone/little-lemon/workspace/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from django.core.management import execute_from_command_line
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(execute_from_command_line())