#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile

from scilpy.io.fetcher import get_testing_files_dict, fetch_data, get_home


# If they already exist, this only takes 5 seconds (check md5sum)
fetch_data(get_testing_files_dict(), keys=['filtering.zip'])
tmp_dir = tempfile.TemporaryDirectory()


def test_help_option(script_runner):
    ret = script_runner.run('scil_compute_qbx.py', '--help')
    assert ret.success


def test_execution_filtering(script_runner):
    os.chdir(os.path.expanduser(tmp_dir.name))
    input_bundle = os.path.join(get_home(), 'filtering',
                                'bundle_all_1mm.trk')
    ret = script_runner.run('scil_compute_qbx.py', input_bundle, '12',
                            'clusters/', '--output_centroids', 'centroids.trk')
    assert ret.success
