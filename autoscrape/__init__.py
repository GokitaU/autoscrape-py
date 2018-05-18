"""
                   initialize & get entry point
                               │
                               ↓
                           load page    🠤───────────────────┐
                               │                            │
                               │            click a link based on likelihood
                               │               of finding a search form
                               ↓                            │
       ┌────🠦 look for search form (possibly classifier) ───┘
       │                       │
       │                       │ FOUND
       │                       ↓
       │         identify forms on page that require input
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
                   enter data into form inputs 🠤───────┐
                               │                       │
                               ↓                       │
                  submit form and load next page       │
                               │                       │
                               ↓                       │
               ┌──────🠦 scrape the page                │
               │               │                       │
               │               ↓                       │
               │     look for a next button ───────────┘
               │         (classifier)        NOT FOUND
               │               │
               │               │ YES
               │               ↓
               └─── click the next button & load page
"""
class AutoScraper(object):
    pass
