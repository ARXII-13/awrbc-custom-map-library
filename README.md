# Advance Wars 1+2: Re-Boot Camp — custom map library

Custom maps people have made, in a format the
[manager tool](https://github.com/ARXII-13/awrbc-custom-map-manager) can put
into your save.

**Not affiliated with Nintendo or WayForward.** This holds map data that
players wrote — grids of numbers describing terrain and ownership. No game
assets, no code from the game, nothing extracted from a cartridge.

## Getting a map

```bash
awrbc search "4p fog"      # find one
awrbc show daibi           # look at it
awrbc import daibi         # put it in your save
```

Or browse `maps/` — every map folder has a README with a picture of it.

## Adding one

Build it in the editor, hit **Export bundle**, and submit. See
[CONTRIBUTING.md](CONTRIBUTING.md) — including what you're agreeing to, which
matters because this repository is public and permanent.

## How it's laid out

```
maps/4p/twin-rivers/
├── README.md     generated - the picture and the facts
├── v1.json       the map
├── v1.png        a preview, drawn by the editor
└── v2.json       a later revision by the same author
```

- The **category** folder is the map's player count, worked out from its HQs
  rather than declared — so it can't disagree with the map. `special/` is for
  maps where player count isn't the point.
- The **slug** folder is the map, and stays put across revisions.
- Each **`vN.json`** is one published version. Both stay downloadable; that is
  why versions are files and not git history.

`catalog.json` is a generated index of everything, so a client can search
without cloning. It and the folder READMEs are rebuilt by CI on merge — don't
edit them by hand.

## Identity

A map's identity is a hash of its *content* — terrain, ownership, units. Name,
author, tags and version are excluded, which has two consequences worth
knowing:

- Renaming a map doesn't make it a new one.
- Re-uploading someone else's map under a different name is still detected as
  a duplicate, and so is a "new version" that didn't actually change anything.

## Licence

Maps are contributed under [CC BY 4.0](LICENSE): share and adapt freely, with
credit to the author. Each map's author is in its folder README and in
`catalog.json`.
