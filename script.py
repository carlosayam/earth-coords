import atexit
import math
import sys

from datetime import datetime

import click
import pandas as pd

from pyproj import Proj


class ReverseFloat(click.ParamType):
    """A custom click type to parse floats with a trailing sign, like 1.23-"""

    name = "float-"

    def convert(self, value, param, ctx):
        try:
            if value[-1] == "-":
                return -float(value[:-1])
            if value[-1] == "+":
                return float(value[:-1])
            return float(value)
        except TypeError:
            self.fail(
                "expected float like 1.23 or 1.23-, got "
                f"{value!r} of type {type(value).__name__}",
                param,
                ctx,
            )
        except ValueError:
            self.fail(f"{value!r} is not a valid float", param, ctx)

reverse_float = ReverseFloat()

@click.group()
def main():
    pass

@main.command()
@click.argument('min_long', type=reverse_float)
@click.argument('max_long', type=reverse_float)
@click.argument('min_lat', type=reverse_float)
@click.argument('max_lat', type=reverse_float)
def area(min_long, max_long, min_lat, max_lat):
    """Calculates the approximate area between given
    WGS84 coordinates. The value is an approximation
    and only reasonable for small degrees of
    difference."""
    proj = Proj(proj='utm', ellps='WGS84')
    x0, y0 = proj(min_long, min_lat)
    x1, y1 = proj(max_long, max_lat)
    area = (x1 - x0) * (y1 - y0) / 1000000
    print('%0.4f Km2' % area)


@main.command()
@click.argument('file', type=click.Path(exists=True, dir_okay=False))
@click.argument('long', type=reverse_float)
@click.argument('lat', type=reverse_float)
def find_rows(file, long, lat):
    """Find the rows in the projection file that contain the given coordinates."""

    pd.set_option('display.max_rows', None)
    df = pd.read_csv(file)
    filter = ((df.MIN_longitude <= long)
              & (df.MAX_longitude >= long)
              & (df.MIN_latitude <= lat)
              & (df.MAX_latitude >= lat))
    print(df[filter])


if __name__ == "__main__":
    click.echo("RUNNING python " + " ".join(sys.argv), err=True)
    def wtime(t0):
        secs = (datetime.now() - t0)
        click.echo("[walltime %s]" % str(secs), err=True)
    atexit.register(wtime, datetime.now())
    main()
