# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Module for cloud ops."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.util.all_util import remove_undocumented

# pylint: disable=line-too-long,wildcard-import,g-import-not-at-top
from tensorflow_io.gcs.python.ops.gcs_config_ops import *

_allowed_symbols = [
    'configure_colab_session',
    'configure_gcs',
    'BlockCacheParams',
    'ConfigureGcsHook',
]
remove_undocumented(__name__, _allowed_symbols)
