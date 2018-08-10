# -*- coding: UTF-8 -*-
import logging

from .scrapers.manual import ManualControlScraper
from .scrapers.test import TestScraper
from .scrapers.ml import MLAutoScraper
from .scrapers.null import NullScraper


"""
COMMAND        Logical Control Flow Step
--------       ---------------------------------------------------------------
INIT (url)               initialize & get entry point
                                     │
                                     ↓
                                 load page    🠤───────────────────┐
                                     │                            │
GET_CLICKABLE                        │        click a link based on likelihood
SELECT_LINK (index)                  │               of finding a search form
                                     ↓                            │
GET_FORMS    ┌────🠦 look for search form (possibly classifier) ───┘
             │                       │
             │                       │ FOUND
             │                       ↓
GET_INPUTS   │         identify forms on page that require input
             │     (begin with config then move to heuristic then ML)
             │                       │
             │                       ↓
             │      initialize iterators for required inputs
             │      (begin with config/brute force, then RL)
             │                       │
             │                       ↓
             └─────── are we at the end of our iterators?
                YES                  │
                                     ↓
INPUT (index, chars)     enter data into form inputs 🠤───────┐
                                     │                       │
                                     ↓                       │
SUBMIT (index)          submit form and load next page       │
                                     │                       │
                                     ↓                       │
                     ┌──────🠦 scrape the page                │
                     │               │                       │
                     │               ↓                       │
GET_LINKS            │     look for a next button ───────────┘
                     │         (classifier)        NOT FOUND
                     │               │
                     │               │ YES
                     │               ↓
SELECT_LINK (index)  └─── click the next button & load page
"""

