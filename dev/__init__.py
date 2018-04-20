# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import os


package_name = "oscrypto"

other_packages = [
    "certbuilder",
    "certvalidator",
    "crlbuilder",
    "csrbuilder",
    "ocspbuilder"
]

package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
build_root = os.path.abspath(os.path.join(package_root, '..'))
