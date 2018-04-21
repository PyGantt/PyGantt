.. image:: https://img.shields.io/pypi/v/pygantt.svg
        :target: https://pypi.python.org/pypi/pygantt

.. image:: https://img.shields.io/travis/PyGantt/PyGantt.svg
        :target: https://travis-ci.org/PyGantt/PyGantt

.. image:: https://readthedocs.org/projects/pygantt/badge/?version=latest
        :target: https://pygantt.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

=======
PyGantt
=======

Easy Gantt and waterfall charts in python.

This module uses Gantt type charts to plot event data characterized by a start and an end. 
It naturally applies to scheduling but it is well suited in financial applications, e.g. plotting positions/weights in a portfolio alongside the portfolio index, in medical application, e.g. the raster plot of neuron impulses, or in waterfall usage plots, e.g. the evolution of your monthly earnings and expenses.

* Free software: BSD license
* Documentation: https://pygantt.readthedocs.io.

Installation
--------
The easiest way to install PyGantt is using ``pip``::

    pip install -U pygantt

or ``conda``::

    conda install -c mriduls pygantt


Features
--------

The canonical scheduling example:

.. image:: https://github.com/PyGantt/PyGantt/blob/master/images/concert.png


Display portfolio positions alongside the realized index:

.. image:: https://github.com/PyGantt/PyGantt/blob/master/images/strategy.png


Freelancers ups and downs:

.. image:: https://github.com/PyGantt/PyGantt/blob/master/images/freelancer.png


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
