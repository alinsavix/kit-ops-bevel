# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    'name': 'KIT OPS BEVEL',
    'author': 'Chipp Walters, bonjorno7',
    'description': 'Bake rendered bevels on KIT OPS created objects that work for EEVEE',
    'blender': (2, 83, 0),
    'version': (1, 1, 8),
    'category': '3D View',
    'location': 'View3D',
}


from . import addon


def register():
    addon.register()


def unregister():
    addon.unregister()
