# Earth AI

## Script that

1. Calculate area given two corners of a square in WGS 84 coordinates
2. Finds rows that contain a given point

## Requirements

1. Requires Python 3.6 or higher
2. Clone the repo and create virtual environment
3. Run

    $ pip install -r requirements.txt

## Usage

One can run the script by using `python -m script`. For instance, to
get general help

    $ python -m script --help

To get help on an available command

    $ python -m script area --help

### Calculating approximate area

Given two corners in WGS84 coordinates, it calculates the area using
a very simple approximation valid only for small angle differences.
Example usage:

    $ python -m script area 142.5 143 11.5- 11-

Note the sign goes at the end, as the script follows POSIX standards and
a hyphen (-) indicates a command option. Alternatively, again based on
POSIX standards, one can use '--' to stop processing options and the signs
will be interpreted properly.

    $ python -m script area -- 142.5 143 -11.5 -11

### Finding locations containing a point

Given a coordinate file and a coordinated in WGS 84 coordinates, it lists
all the entries in the file that contain the given point. For example

    $ python -m script find-rows AU_proj_coords.csv -- 142.6 -11.2

The first parameter is the path to the file and the next are the longitude
and latitude of the point of interest.
