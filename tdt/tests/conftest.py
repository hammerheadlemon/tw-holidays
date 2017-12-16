import pytest

test_file = """###############################################################################
# International Holiday Data provided by Holidata.net
# http://holidata.net/en-GB/2015.json
# http://holidata.net/en-GB/2016.json
#
# Copyright 2006 - 2016, Paul Beckingham, Federico Hernandez.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php
#
###############################################################################

holiday.en-GB1.name=New Year's Day
holiday.en-GB1.date=20150101
holiday.en-GB2.name=Good Friday
holiday.en-GB2.date=20150403
holiday.en-GB3.name=Easter Monday
holiday.en-GB3.date=20150406
holiday.en-GB4.name=Early May Bank Holiday
holiday.en-GB4.date=20150504
holiday.en-GB5.name=Spring Bank Holiday
holiday.en-GB5.date=20150525
holiday.en-GB6.name=August Bank Holiday
holiday.en-GB6.date=20150831
holiday.en-GB7.name=Christmas Day
holiday.en-GB7.date=20151225
holiday.en-GB8.name=Boxing Day
holiday.en-GB8.date=20151226
holiday.en-GB9.name=New Year's Day
holiday.en-GB9.date=20160101
holiday.en-GB10.name=Good Friday
holiday.en-GB10.date=20160325
holiday.en-GB11.name=Easter Monday
holiday.en-GB11.date=20160328
holiday.en-GB12.name=Early May Bank Holiday
holiday.en-GB12.date=20160502
holiday.en-GB13.name=Spring Bank Holiday
holiday.en-GB13.date=20160530
holiday.en-GB14.name=August Bank Holiday
holiday.en-GB14.date=20160829
holiday.en-GB15.name=Christmas Day
holiday.en-GB15.date=20161225
holiday.en-GB16.name=Boxing Day
holiday.en-GB16.date=20161226
"""


@pytest.fixture
def holiday_rc_file(tmpdir):
    t_file = tmpdir.join('test_holiday_rc_file')
    t_file.write(test_file)
    return t_file
