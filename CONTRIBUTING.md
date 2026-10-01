# Contributing a map

## The short version

1. Build your map in the editor and use **Export bundle**, which gives you a
   `.zip` holding the map and a picture of it.
2. Run `awrbc publish yourmap.zip --library .` from a clone of this repo. It
   puts the files where they belong and prints the git commands to run.
3. Open a pull request.

If you don't use git, you don't have to — that's what the submission page is
for. These instructions are for people who prefer the command line.

## What you are agreeing to

**By opening a pull request you confirm that:**

- The map is **your own work**. Not copied from another game, another player's
  map, or anywhere else — a layout you recreated from memory of an official
  Advance Wars map is not your own work.
- You license it under **[CC BY 4.0](LICENSE)**, which lets anyone share and
  adapt it as long as they credit you.
- You're happy for your chosen author name to appear publicly, forever.

That last point is worth reading twice. This is a public git repository: once a
map is merged, it stays in the history even if the file is later deleted.
Deleting a file fixes what the archive serves; it does not reach the clone
somebody already made. Use a name you're comfortable having attached to this
permanently, and don't put anything in a map name or description you wouldn't
want to be permanent.

## What CI checks

Every pull request is checked automatically. It is not a judgement of your map
— it's looking for things that would break the archive:

| | |
|---|---|
| The map parses, and is playable | Two armies or more, each with an HQ and a way to act |
| Size | Up to 64×64. Past 30×20 plays fine but can't be opened in the in-game editor |
| Units | At most 50 per army |
| The path matches the map | A 4-army map belongs in `maps/4p/`, and `version` has to match the filename |
| It isn't already here | Identity is a hash of the map's content, so a re-upload under a new name is still a duplicate |
| The preview is a real image of the right size | See below |
| Names | Obvious abuse is rejected |

**One map per pull request.** It keeps review quick and makes reverting a
single merge rather than a surgery.

## About previews

Your bundle's `preview.png` is copied into the archive as-is, so it's checked
like any other file from outside: it has to be a plain PNG, with nothing hidden
after the end of the image, at exactly the size your map renders at — the
editor draws one tile at 16 pixels, so a 30×20 map is 480×320 and nothing else.

What that *can't* check is whether the picture is actually of your map. A human
looks at it in the pull request, which is also why a preview that doesn't match
will be spotted.

If you submit without a preview the map still publishes; its page just has no
picture. Re-exporting as a bundle is the fix.

## Where a map lives

```
maps/<category>/<slug>/v1.json
```

- **category** is your map's player count — `2p`, `3p`, `4p`, `5p` — worked out
  from its HQs, not something you choose. `special/` is for maps where player
  count isn't the point.
- **slug** is your map, and stays the same across revisions.
- **vN.json** is one published version. A new version of an existing map goes
  in the same folder: `awrbc publish yourmap.zip --library . --update 2p/yourmap`.

The archive assigns the version number — you don't pick it. And because
identity is a content hash that ignores name, author and tags, a "new version"
that doesn't actually change the map is rejected as a duplicate.

## Updating someone else's map

Don't open a revision on a map you didn't publish. Make your own, and credit
the original in its description. If you've genuinely taken over maintenance of
a map, say so in the pull request and a maintainer will sort it out.

## If your pull request is rejected

Most rejections are mechanical and the CI output says exactly what to change.
If it's a judgement call, you'll get a reason. Maps are rejected for breaking
the checks above, for abusive content, and for being someone else's work —
not for being bad maps. A confusing map that someone enjoyed building belongs
here.
