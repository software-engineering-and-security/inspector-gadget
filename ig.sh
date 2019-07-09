#!/bin/bash
# 
# (c) 2019 University of Luxembourg - Interdisciplinary Centre for
# Security Reliability and Trust (SnT) - All rights reserved
# Alexandre Bartel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Lesser Public License for more details.
#
# You should have received a copy of the GNU General Lesser Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/lgpl-2.1.html>.
#
# ex: ./ig.sh -b ./input/comm -maxlen 10 -arg 2 -o ./output/dir/

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PYTHONPATH=$PYTHONPATH:$SCRIPT_DIR
python3 "${SCRIPT_DIR}/inspectorgadget/InspectorGadget.py" "$@"

