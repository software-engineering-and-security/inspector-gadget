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

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ROOT_DIR="${SCRIPT_DIR}/../"

${ROOT_DIR}/ig.sh -a x86-64 -b ${ROOT_DIR}/bin/print -minlen 1 -maxlen 1 -arg 2 -o ${ROOT_DIR}/bin/ -p 1

