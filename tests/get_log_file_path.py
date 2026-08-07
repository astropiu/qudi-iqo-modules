import os
from qudi.util.paths import get_default_log_dir


log_path = os.path.join(get_default_log_dir(), 'qudi.log')
print(log_path)