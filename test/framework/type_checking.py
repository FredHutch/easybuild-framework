# #
# Copyright 2015-2015 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
# #
"""
Unit tests for easyconfig/types.py

@author: Kenneth Hoste (Ghent University)
"""
from test.framework.utilities import EnhancedTestCase
from unittest import TestLoader, main

from easybuild.framework.easyconfig.types import check_type_of_param_value


class TypeCheckingTest(EnhancedTestCase):
    """Tests for value type checking of easyconfig parameters."""

    def test_check_type_of_param_value(self):
        """Test check_type_of_param_value function."""
        # check selected values that should be strings
        for key in ['name', 'version']:
            self.assertTrue(check_type_of_param_value(key, 'foo'))
            for not_a_string in [100, 1.5, ('bar',), ['baz'], None]:
                self.assertFalse(check_type_of_param_value(key, not_a_string))
            # value doesn't matter, only type does
            self.assertTrue(check_type_of_param_value(key, ''))

        # parameters with no type specification always pass the check
        key = 'nosucheasyconfigparametereverhopefully'
        for val in ['foo', 100, 1.5, ('bar',), ['baz'], '', None]:
            self.assertTrue(check_type_of_param_value(key, val))


def suite():
    """ returns all the testcases in this module """
    return TestLoader().loadTestsFromTestCase(TypeCheckingTest)


if __name__ == '__main__':
    main()
