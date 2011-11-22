# Copyright (C) 2009 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Emit commands needed for Prime during OTA installation
(installing the bootloader and radio images)."""

import common

def FormatPartition(self, partition):
    """Format the given partition, specified by its mount point (eg,
    "/system")."""

    reserve_size = 0
    fstab = self.info.get("fstab", None)
    if fstab:
      p = fstab[partition]
      #self.script.append('format("%s", "%s", "%s", "%s");' %
      #                   (p.fs_type, common.PARTITION_TYPES[p.fs_type],
      #                    p.device, p.length))
      self.script.append('delete_recursive("/system");')  
