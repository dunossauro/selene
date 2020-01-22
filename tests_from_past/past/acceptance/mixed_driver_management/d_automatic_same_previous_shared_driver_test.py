# MIT License
#
# Copyright (c) 2015-2020 Iakiv Kramarenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from selenium.common.exceptions import TimeoutException

from selene.api.past import browser, config
from selene.support.conditions import have

from selene.support.jquery_style_selectors import s, ss


todomvc_url = 'https://todomvc4tasj.herokuapp.com/'
is_TodoMVC_loaded = 'return (Object.keys(require.s.contexts._.defined).length === 39)'

original_timeout = config.timeout


def teardown_module(m):
    config.timeout = original_timeout

#todo: enable test
def xtest_add_tasks():
    browser.open_url(todomvc_url)
    browser.should(have.js_returned_true(is_TodoMVC_loaded))

    s('#new-todo').set_value('a').press_enter()
    s('#new-todo').set_value('b').press_enter()
    s('#new-todo').set_value('c').press_enter()

    config.timeout = 0.5
    with pytest.raises(TimeoutException) as ex:
        ss("#todo-list>li").should(have.size(3))

    assert "actual: 6" in ex.value.msg