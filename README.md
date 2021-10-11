#  Report of Racing (report)

This application read data from 2 files, order racers 
by time and print report that shows the top 15 
racers and the rest after underline, for example:

For example:

1. Daniel Ricciardo      | RED BULL RACING TAG HEUER     | 1:12.013

2. Sebastian Vettel      | FERRARI  | 1:12.415

3. ...

_____________________________________________________________

16. Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 1:13.179

17. Marcus Ericsson  | SAUBER FERRARI  | 1:13.265"


This module(report) has a command-line interface.
The application has to have a few parameters. E.g.
> python report.py --files <folder_path> [--asc | --desc]  shows list of drivers and optional order (default order is asc)

> python report.py --files <folder_path> driver “Sebastian Vettel”  shows statistic about driver 
