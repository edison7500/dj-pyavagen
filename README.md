# Django-PyAvagen

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8f84ba60672049eeac0728d4d983875b)](https://www.codacy.com/manual/edison7500/dj-pyavagen?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edison7500/dj-pyavagen&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/edison7500/dj-pyavagen.svg?branch=master)](https://travis-ci.org/edison7500/dj-pyavagen)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


## Quick Start

### Install
```.shell script
git clone https://github.com/edison7500/dj-pyavagen.git
cd dj-pyavagen
python setup.py install
```

### Configuration
```.python

# settings.py
INSTALLED_APPS = [
    'dj_pyavagen',
]


# urls.py
urlpatterns = [
    url(r"^avatar/", include("dj_pyavagen.urls", namespace="pyavagen")),
]

```