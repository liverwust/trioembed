#!/home/dh_fwkigp/trioembed-venv/bin/python3
# 
# Triangle oEmbed wrapper
# Copyright (C) 2020 Louis Wust
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Contact Louis Wust <louiswust@fastmail.fm>

# The "shebang" line at the beginning of the file, and the script as a whole,
# are tailored for a specific DreamHost Virtual Private Server (VPS). Changes
# would need to be made for any permanent solution.

import cgi
import cgitb
cgitb.enable()

import sys
sys.path.insert(0, "/home/dh_fwkigp/trioembed")
import trioembed.oldsite

embedder = trioembed.oldsite.OldSiteEmbedder()
output = embedder.go()

print("Content-Type: text/html")
print()
print(output)
