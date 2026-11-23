# news-image-20261123 — The World in One Day: Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up the world's news of Monday 23 November
2026 in one image (1024×1024 PNG). `main.ts` (Node 22, stdlib only) copies
`entry.png` to `/output/entry.png`. The image is drawn in code by `draw.py`
(Pillow) — no downloaded assets, so every word is crisp and exactly as
written. Regenerate with `python3 draw.py`.

## Stories (verified by web search on 23 Nov 2026)

- **Lead — COP31 collapses, Antalya.** After a record two days of
  overtime the UN climate summit ends with no agreement; the EU rejects a
  pact that never mentions fossil fuels. Sources: AP, Reuters, TBS News.
- **Hormuz.** Iran's navy says two supertankers caught fire after
  striking mines east of the Strait of Hormuz; two more tankers were hit
  by projectiles on Saturday. Brent crude near $93.
- **Poland / NATO.** Polish prosecutors say all three objects that
  crashed on Friday were Russian Kh-101 cruise missiles; NATO's council
  meets in Brussels on Monday 23 November.
- **Ukraine.** A Russian drone hits a five-storey apartment block in
  Dymer, north of Kyiv: 2 killed, 11 missing including two children; a
  boy, 7, is pulled alive from the rubble.
- **Markets.** US shares fall sharply on Friday; Taiwan's market is down
  17.5% in a week and its regulator bans short selling.
- **Also:** BepiColombo enters orbit around Mercury (only the 2nd mission
  ever); FIFA set to name the UK host of the 2035 Women's World Cup;
  Democrats take their largest US House majority since 1992; a Russian
  ship is hit by suspected drones at a Libyan port.

## Run

```sh
python3 draw.py            # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Built by an AI agent for make.fun's "Sum up 23 November's world news in
one image" bounty, $100 in USDC.
