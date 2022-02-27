#!/usr/bin/python

# Copyright (C) 2021 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import shutil
import os
import io

import usrse.utils as utils
import usrse.endpoints as endpoints
from usrse.main import Client

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)

tests = [(ep, item) for ep in endpoints.register_names for item in [True, False]]


@pytest.mark.parametrize("endpoint,is_live", tests)
def test_install_get(tmp_path, endpoint, is_live):
    """Test install and get"""
    client = Client(quiet=False)
    result = client.get(endpoint)
    if is_live:
        result.table_live()
    else:
        result.table()
