"""
Packaging to go up onto PyPi
- Brett Cannon

Build Artifacts:
 - wheels (whls)
    - internally are just zipped files
    - no build step
    - *may* need to fix up some dependencies
    - Convenient and modern
    - Its really a 'prebuilt package of bits'

 - source distributions (sdists)
    - tar files; gzipped
    - if you start with this -- it will be built and converted to a whl

Introduction to Flit:
 -
"""