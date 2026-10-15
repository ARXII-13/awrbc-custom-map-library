"""Write a one-page index beside the published catalog.

The published site holds one data file, so its root answered 404 - which is
honest and still alarming to meet. Anyone who finds this URL deserves a
sentence saying what it is rather than a GitHub error page.

Takes the directory to write into; reads the catalog that is already there.
"""
import datetime
import json
import os
import sys

REPO = "https://github.com/ARXII-13/awrbc-custom-map-library"

PAGE = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AWRBC map archive index</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{
    font: 16px/1.6 system-ui, sans-serif; max-width: 42rem;
    margin: 4rem auto; padding: 0 1rem;
  }}
  code {{ font-size: .95em; }}
  dt {{ font-weight: 600; margin-top: 1rem; }}
  dd {{ margin: .2rem 0 0; }}
  .muted {{ opacity: .7; font-size: .9em; }}
</style>

<h1>AWRBC map archive index</h1>

<p>A generated index of the custom maps in
<a href="{repo}">awrbc-custom-map-library</a>, so a client can search the
archive without cloning it.</p>

<dl>
  <dt><a href="catalog.json">catalog.json</a></dt>
  <dd>{count} map{plural}. Rebuilt and republished whenever something is
      merged into the archive.</dd>
</dl>

<p>Everything in it is recomputed from the map files, which are the actual
source: it is a cache, never the authority. The one thing it carries that
cannot be recomputed - when each version was submitted - is stored beside
each map in its own <code>meta.json</code> and read back in here.</p>

<p class="muted">Built {generated}. There is no website here; the maps live
in <a href="{repo}">the repository</a>.</p>
</html>
"""


def main(argv):
    out = argv[1] if len(argv) > 1 else "site"
    with open(os.path.join(out, "catalog.json"), encoding="utf-8") as fh:
        index = json.load(fh)
    count = len(index.get("maps", {}))
    page = PAGE.format(
        repo=REPO,
        count=count,
        plural="" if count == 1 else "s",
        generated=index.get("generated")
        or datetime.date.today().isoformat(),
    )
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print("wrote index.html for %d map%s" % (count, "" if count == 1 else "s"))


if __name__ == "__main__":
    main(sys.argv)
