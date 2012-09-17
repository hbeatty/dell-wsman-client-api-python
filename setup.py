"""
Setup file for egg builds

@copyright: 2010-2012
@author: Joseph Tallieu <joseph_tallieu@dell.com>
@author: Vijay Halaharvi <vijay_halaharvi@dell.com>
@organization: Dell Inc. - PG Validation
@license: GNU LGLP v2.1
"""
#    This file is part of WSManAPI.
#
#    WSManAPI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 2.1 of the License, or
#    (at your option) any later version.
#
#    WSManAPI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with WSManAPI.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

# setup meta data and entry points
setup(
    name='wsman',
    version="0.9.19",
    description="Web Services Management",
    author="Vijay Halaharvi, Joseph Tallieu",
    author_email="Vijay_Halaharvi@dell.com, joseph_tallieu@dell.com",
    license="Dell Software License",
    packages=find_packages(),
    package_data={'wsman':['transport/dummy/responses/winrm/*', 
                           'transport/dummy/responses/wsmancli/*',
                           'loghandlers/templates/*']},
    include_package_data=True    
    )
